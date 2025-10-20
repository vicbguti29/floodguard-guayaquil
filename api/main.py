"""
FloodGuard API - FastAPI Backend
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
import uvicorn

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

@app.get("/api/v1/predict", response_model=List[PredictionResponse])
async def get_predictions():
    """
    Obtener predicciones actuales para todas las zonas
    """
    # TODO: Cargar modelo y generar predicciones reales

    # Placeholder response
    mock_predictions = [
        PredictionResponse(
            zone_id="Z001",
            zone_name="Los Sauces",
            risk_level="medium",
            probability=0.45,
            estimated_time_hours=3.5,
            confidence=0.82,
            timestamp=datetime.now()
        ),
        PredictionResponse(
            zone_id="Z002",
            zone_name="Alborada",
            risk_level="low",
            probability=0.15,
            estimated_time_hours=None,
            confidence=0.91,
            timestamp=datetime.now()
        )
    ]

    return mock_predictions

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
