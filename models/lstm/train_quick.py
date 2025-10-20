"""
Training rápido del LSTM con datos sintéticos
Para tener modelo funcional en API cuanto antes
"""

import torch
import torch.nn as nn
import torch.optim as optim
import pandas as pd
import numpy as np
from pathlib import Path
from baseline import LSTMRainPredictor, FloodRiskClassifier

def load_synthetic_data():
    """Cargar datos sintéticos generados"""
    data_path = Path(__file__).parent.parent.parent / 'data' / 'processed' / 'synthetic_rainfall_timeseries.parquet'

    if not data_path.exists():
        print(f"Error: {data_path} no existe. Ejecuta create_synthetic_data.py primero")
        return None

    df = pd.read_parquet(data_path)
    return df


def prepare_sequences(df, seq_length=24, pred_length=6):
    """
    Crear secuencias para entrenamiento

    Args:
        df: DataFrame con datos de lluvia
        seq_length: Cuántas horas usar como input (24h)
        pred_length: Cuántas horas predecir (6h)

    Returns:
        X: inputs (n_samples, seq_length, n_features)
        y: targets (n_samples, pred_length)
    """
    # Features
    features = ['precipitation_mm', 'temperature_c', 'humidity_percent', 'wind_speed_kmh']
    data = df[features].values

    # Normalizar
    mean = data.mean(axis=0)
    std = data.std(axis=0) + 1e-8
    data_norm = (data - mean) / std

    X, y = [], []

    for i in range(len(data_norm) - seq_length - pred_length):
        # Input: últimas 24h (4 features)
        X.append(data_norm[i:i+seq_length])

        # Target: próximas 6h de precipitación
        y.append(data_norm[i+seq_length:i+seq_length+pred_length, 0])  # Solo precipitación

    return np.array(X), np.array(y), mean, std


def train_quick(epochs=10):
    """Entrenamiento rápido para MVP"""
    print("="*60)
    print("TRAINING LSTM BASELINE - MODO RÁPIDO")
    print("="*60)

    # Cargar datos
    print("\n1. Cargando datos sintéticos...")
    df = load_synthetic_data()
    if df is None:
        return

    print(f"   - {len(df)} registros cargados")

    # Preparar secuencias
    print("\n2. Preparando secuencias...")
    X, y, mean, std = prepare_sequences(df)
    print(f"   - {len(X)} secuencias creadas")
    print(f"   - Input shape: {X.shape}")
    print(f"   - Target shape: {y.shape}")

    # Split train/val
    split_idx = int(len(X) * 0.8)
    X_train, X_val = X[:split_idx], X[split_idx:]
    y_train, y_val = y[:split_idx], y[split_idx:]

    # Convertir a tensors
    X_train = torch.FloatTensor(X_train)
    y_train = torch.FloatTensor(y_train)
    X_val = torch.FloatTensor(X_val)
    y_val = torch.FloatTensor(y_val)

    print(f"   - Train: {len(X_train)} samples")
    print(f"   - Val: {len(X_val)} samples")

    # Modelo
    print("\n3. Inicializando modelo...")
    model = LSTMRainPredictor(
        input_size=4,
        hidden_size=64,
        num_layers=2,
        output_size=6
    )

    criterion = nn.MSELoss()
    optimizer = optim.Adam(model.parameters(), lr=0.001)

    print(f"   - Parámetros: {sum(p.numel() for p in model.parameters()):,}")

    # Training loop
    print(f"\n4. Entrenando ({epochs} epochs)...")
    batch_size = 32

    for epoch in range(epochs):
        model.train()
        train_loss = 0

        # Mini-batches
        for i in range(0, len(X_train), batch_size):
            batch_X = X_train[i:i+batch_size]
            batch_y = y_train[i:i+batch_size]

            # Forward
            optimizer.zero_grad()
            outputs = model(batch_X)
            loss = criterion(outputs, batch_y)

            # Backward
            loss.backward()
            optimizer.step()

            train_loss += loss.item()

        # Validation
        model.eval()
        with torch.no_grad():
            val_outputs = model(X_val)
            val_loss = criterion(val_outputs, y_val)

        # Print progress
        avg_train_loss = train_loss / (len(X_train) / batch_size)
        print(f"   Epoch {epoch+1}/{epochs} - Train Loss: {avg_train_loss:.4f}, Val Loss: {val_loss:.4f}")

    # Guardar modelo
    print("\n5. Guardando modelo...")
    save_dir = Path(__file__).parent.parent / 'checkpoints'
    save_dir.mkdir(exist_ok=True)

    checkpoint = {
        'model_state_dict': model.state_dict(),
        'mean': mean,
        'std': std,
        'input_size': 4,
        'hidden_size': 64,
        'num_layers': 2,
        'output_size': 6
    }

    save_path = save_dir / 'lstm_baseline_v1.pth'
    torch.save(checkpoint, save_path)
    print(f"   - Modelo guardado en: {save_path}")

    # Test rápido
    print("\n6. Test de predicción...")
    model.eval()
    with torch.no_grad():
        test_input = X_val[0:1]  # Primera secuencia de validación
        prediction = model(test_input)

        # Desnormalizar
        prediction_denorm = prediction.numpy() * std[0] + mean[0]
        actual_denorm = y_val[0].numpy() * std[0] + mean[0]

        print(f"   - Predicción (próximas 6h): {prediction_denorm[0]}")
        print(f"   - Real (próximas 6h): {actual_denorm}")

    print("\n" + "="*60)
    print("✓ TRAINING COMPLETADO")
    print("="*60)
    print(f"\nModelo listo para usar en API: {save_path}")


if __name__ == '__main__':
    train_quick(epochs=20)
