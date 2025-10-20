"""
LSTM Baseline para predicción de lluvia
Modelo simple antes de Transformer complejo (enfoque ágil)
"""

import torch
import torch.nn as nn
import numpy as np
from pathlib import Path

class LSTMRainPredictor(nn.Module):
    """
    LSTM simple para predecir precipitación futura

    Input: Secuencia de precipitación pasada (24h)
    Output: Predicción próximas 6h
    """

    def __init__(self, input_size=4, hidden_size=64, num_layers=2, output_size=6):
        """
        Args:
            input_size: Número de features (precipitación, temp, humedad, viento)
            hidden_size: Dimensión de hidden state
            num_layers: Número de capas LSTM
            output_size: Horas a predecir (6h)
        """
        super(LSTMRainPredictor, self).__init__()

        self.hidden_size = hidden_size
        self.num_layers = num_layers

        # LSTM layers
        self.lstm = nn.LSTM(
            input_size=input_size,
            hidden_size=hidden_size,
            num_layers=num_layers,
            batch_first=True,
            dropout=0.2 if num_layers > 1 else 0
        )

        # Fully connected layers para output
        self.fc = nn.Sequential(
            nn.Linear(hidden_size, 32),
            nn.ReLU(),
            nn.Dropout(0.2),
            nn.Linear(32, output_size)
        )

    def forward(self, x):
        """
        Forward pass

        Args:
            x: Tensor de shape (batch, seq_len, input_size)
               seq_len = 24 (últimas 24 horas)

        Returns:
            Predicción de shape (batch, output_size)
            output_size = 6 (próximas 6 horas)
        """
        # LSTM forward
        lstm_out, (hidden, cell) = self.lstm(x)

        # Tomar último hidden state
        last_hidden = lstm_out[:, -1, :]

        # Pasar por FC layers
        output = self.fc(last_hidden)

        return output


class FloodRiskClassifier(nn.Module):
    """
    Clasificador simple de riesgo de inundación

    Input: Predicción de lluvia (6h)
    Output: Probabilidad de inundación por zona
    """

    def __init__(self, input_size=6, num_zones=50, hidden_size=32):
        super(FloodRiskClassifier, self).__init__()

        self.model = nn.Sequential(
            nn.Linear(input_size, hidden_size),
            nn.ReLU(),
            nn.Dropout(0.3),
            nn.Linear(hidden_size, hidden_size),
            nn.ReLU(),
            nn.Dropout(0.3),
            nn.Linear(hidden_size, num_zones),
            nn.Sigmoid()  # Probabilidades [0, 1] por zona
        )

    def forward(self, rain_prediction):
        """
        Args:
            rain_prediction: Tensor (batch, 6) - predicción de lluvia 6h

        Returns:
            Tensor (batch, num_zones) - probabilidad de inundación por zona
        """
        return self.model(rain_prediction)


def get_risk_level(probability):
    """
    Convierte probabilidad a nivel de riesgo

    Args:
        probability: float [0, 1]

    Returns:
        str: 'low', 'medium', 'high', 'critical'
    """
    if probability < 0.25:
        return 'low'
    elif probability < 0.50:
        return 'medium'
    elif probability < 0.75:
        return 'high'
    else:
        return 'critical'


# Para testing rápido
if __name__ == '__main__':
    print("Testing LSTM Baseline...")

    # Modelo de predicción de lluvia
    rain_model = LSTMRainPredictor(
        input_size=4,  # precipitación, temp, humedad, viento
        hidden_size=64,
        num_layers=2,
        output_size=6  # predecir próximas 6h
    )

    # Input de prueba: batch de 2, 24 horas pasadas, 4 features
    test_input = torch.randn(2, 24, 4)
    rain_pred = rain_model(test_input)

    print(f"Input shape: {test_input.shape}")
    print(f"Rain prediction shape: {rain_pred.shape}")
    print(f"Sample prediction (6h): {rain_pred[0].detach().numpy()}")

    # Modelo de clasificación de riesgo
    risk_model = FloodRiskClassifier(
        input_size=6,
        num_zones=50
    )

    risk_pred = risk_model(rain_pred)
    print(f"\nRisk prediction shape: {risk_pred.shape}")
    print(f"Sample risk for zone 0: {risk_pred[0][0].item():.3f} ({get_risk_level(risk_pred[0][0].item())})")

    print("\n✓ Models initialized successfully!")
    print(f"Rain model params: {sum(p.numel() for p in rain_model.parameters()):,}")
    print(f"Risk model params: {sum(p.numel() for p in risk_model.parameters()):,}")
