"""
FloodGuard API - FastAPI Backend
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime, timedelta
import uvicorn
import torch
import numpy as np
from pathlib import Path
import sys

# Add models to path
sys.path.append(str(Path(__file__).parent.parent / 'models' / 'lstm'))

app = FastAPI(
    title="FloodGuard API",
    description="Sistema de predicción de inundaciones para Guayaquil",
    version="0.1.0"
)

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # En producción, especificar dominios
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Schemas
class PredictionResponse(BaseModel):
    zone_id: str
    zone_name: str
    risk_level: str  # low, medium, high, critical
    probability: float
    estimated_time_hours: Optional[float]
    confidence: float
    timestamp: datetime

class ZoneInfo(BaseModel):
    zone_id: str
    zone_name: str
    coordinates: List[float]
    population: Optional[int]

# Endpoints
@app.get("/")
async def root():
    return {
        "message": "FloodGuard API",
        "version": "0.1.0",
        "status": "operational"
    }

def load_model():
    """Cargar modelo LSTM entrenado"""
    try:
        from baseline import LSTMRainPredictor

        model_path = Path(__file__).parent.parent / 'models' / 'checkpoints' / 'lstm_baseline_v1.pth'

        if not model_path.exists():
            print(f"Warning: Modelo no encontrado en {model_path}")
            return None

        checkpoint = torch.load(model_path, map_location=torch.device('cpu'), weights_only=False)

        model = LSTMRainPredictor(
            input_size=checkpoint['input_size'],
            hidden_size=checkpoint['hidden_size'],
            num_layers=checkpoint['num_layers'],
            output_size=checkpoint['output_size']
        )

        model.load_state_dict(checkpoint['model_state_dict'])
        model.eval()

        print(f"[OK] Modelo cargado desde {model_path}")
        return {
            'model': model,
            'mean': checkpoint['mean'],
            'std': checkpoint['std']
        }

    except Exception as e:
        print(f"Error cargando modelo: {e}")
        return None


# Cargar modelo al iniciar
MODEL = load_model()


def get_risk_level(probability):
    """Convierte probabilidad a nivel de riesgo"""
    if probability < 0.25:
        return 'low'
    elif probability < 0.50:
        return 'medium'
    elif probability < 0.75:
        return 'high'
    else:
        return 'critical'


@app.get("/api/v1/predict", response_model=List[PredictionResponse])
async def get_predictions():
    """
    Obtener predicciones actuales para todas las zonas
    """
    # Si hay modelo, generar predicciones reales (simuladas por ahora)
    if MODEL:
        # TODO: Conectar con datos meteorológicos reales
        # Por ahora, generamos predicciones sintéticas basadas en el modelo

        # Zonas de ejemplo
        zones = [
            {"id": "Z001", "name": "Los Sauces"},
            {"id": "Z002", "name": "Alborada"},
            {"id": "Z003", "name": "Guasmo"},
            {"id": "Z004", "name": "Bastión Popular"},
            {"id": "Z005", "name": "Kennedy"},
            {"id": "Z006", "name": "Urdesa"},
            {"id": "Z007", "name": "Monte Sinaí"}
        ]

        predictions = []

        for zone in zones:
            # Generar probabilidad aleatoria (en producción: del modelo)
            probability = np.random.beta(2, 5)  # Bias hacia valores bajos

            # Tiempo estimado solo si riesgo > low
            estimated_time = None
            if probability > 0.25:
                estimated_time = np.random.uniform(2, 6)

            predictions.append(PredictionResponse(
                zone_id=zone["id"],
                zone_name=zone["name"],
                risk_level=get_risk_level(probability),
                probability=round(probability, 2),
                estimated_time_hours=round(estimated_time, 1) if estimated_time else None,
                confidence=0.75 + np.random.uniform(-0.1, 0.1),  # ~75% confidence
                timestamp=datetime.now()
            ))

        return predictions

    else:
        # Fallback si no hay modelo
        return [
            PredictionResponse(
                zone_id="Z001",
                zone_name="Los Sauces",
                risk_level="medium",
                probability=0.45,
                estimated_time_hours=3.5,
                confidence=0.82,
                timestamp=datetime.now()
            )
        ]

@app.get("/api/v1/zones", response_model=List[ZoneInfo])
async def get_zones():
    """Obtener información de todas las zonas monitoreadas"""
    # TODO: Cargar desde base de datos

    mock_zones = [
        ZoneInfo(
            zone_id="Z001",
            zone_name="Los Sauces",
            coordinates=[-2.1487, -79.8931],
            population=50000
        )
    ]

    return mock_zones

@app.get("/api/v1/historical/{zone_id}")
async def get_historical(zone_id: str, days: int = 30):
    """Obtener historial de inundaciones para una zona"""
    # TODO: Implementar query a base de datos

    return {
        "zone_id": zone_id,
        "days": days,
        "events": []
    }

@app.get("/api/v1/health")
async def health_check():
    """Health check endpoint para monitoring"""
    return {
        "status": "healthy",
        "timestamp": datetime.now(),
        "model_loaded": False  # TODO: Verificar modelo cargado
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
