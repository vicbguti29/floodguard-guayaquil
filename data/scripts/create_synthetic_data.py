"""
Generar datos sintéticos para MVP mientras conseguimos datos reales
Esto permite desarrollar y validar la arquitectura del modelo
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from pathlib import Path

class SyntheticDataGenerator:
    """Genera datos sintéticos realistas para entrenamiento inicial"""

    def __init__(self, output_dir='../processed'):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

        # Parámetros realistas para Guayaquil
        self.rain_threshold_flood = 40  # mm/hora que típicamente causa inundaciones

    def generate_rainfall_timeseries(self, start_date='2023-01-01', end_date='2024-12-31', freq='1h'):
        """
        Genera series temporales de lluvia sintéticas
        Simula temporada invernal (Enero-Mayo) con más lluvia
        """
        print("Generando series temporales de lluvia sintéticas...")

        dates = pd.date_range(start=start_date, end=end_date, freq=freq)
        n_points = len(dates)

        # Base de lluvia (muy baja en seco, más alta en invierno)
        months = pd.DatetimeIndex(dates).month

        # Temporada invernal (Enero-Mayo) tiene más lluvia
        base_rain = np.where(
            (months >= 1) & (months <= 5),
            np.random.gamma(2, 3, n_points),  # Temporada lluviosa
            np.random.gamma(0.5, 0.5, n_points)  # Temporada seca
        )

        # Agregar eventos extremos (inundaciones)
        # ~12 eventos por año en temporada invernal
        n_flood_events = 24  # 2 años
        flood_indices = np.random.choice(
            np.where((months >= 1) & (months <= 5))[0],
            size=n_flood_events,
            replace=False
        )

        for idx in flood_indices:
            # Evento de lluvia intensa (3-6 horas)
            duration = np.random.randint(3, 7)
            peak_rain = np.random.uniform(50, 120)  # mm/hora

            for i in range(duration):
                if idx + i < n_points:
                    base_rain[idx + i] = peak_rain * np.exp(-i/2)  # Decae exponencialmente

        df = pd.DataFrame({
            'timestamp': dates,
            'precipitation_mm': np.clip(base_rain, 0, None),  # No negativos
            'temperature_c': 25 + np.random.normal(0, 3, n_points),  # ~25°C promedio
            'humidity_percent': 70 + np.random.normal(0, 10, n_points),
            'wind_speed_kmh': np.abs(np.random.normal(10, 5, n_points))
        })

        # Marcar eventos de inundación (cuando lluvia > threshold por 2+ horas consecutivas)
        df['flood_event'] = 0
        for idx in flood_indices:
            if idx < n_points - 2:
                df.loc[idx:idx+5, 'flood_event'] = 1

        filepath = self.output_dir / 'synthetic_rainfall_timeseries.parquet'
        df.to_parquet(filepath, index=False)
        print(f"[OK] Series temporales guardadas: {filepath}")
        print(f"  - {len(df)} registros ({len(df)/24:.0f} días)")
        print(f"  - {df['flood_event'].sum()} horas con inundación")
        print(f"  - {len(flood_indices)} eventos distintos")

        return df

    def generate_zone_flood_labels(self, n_zones=50, n_events=24):
        """
        Genera labels de qué zonas se inundaron en cada evento
        Simula propagación espacial realista
        """
        print(f"Generando labels de inundación para {n_zones} zonas...")

        events = []
        base_date = datetime(2023, 1, 1)

        # Zonas vulnerables (siempre se inundan)
        vulnerable_zones = np.random.choice(n_zones, size=int(n_zones*0.2), replace=False)

        for i in range(n_events):
            # Fecha aleatoria en temporada invernal
            month = np.random.randint(1, 6)  # Enero-Mayo
            day = np.random.randint(1, 28)
            event_date = datetime(2023 + i//12, month, day)

            # Severidad del evento
            severity = np.random.choice(['low', 'medium', 'high'], p=[0.5, 0.35, 0.15])

            # Zonas afectadas según severidad
            if severity == 'low':
                affected_zones = vulnerable_zones[:int(len(vulnerable_zones)*0.3)]
            elif severity == 'medium':
                affected_zones = vulnerable_zones
            else:  # high
                affected_zones = np.concatenate([
                    vulnerable_zones,
                    np.random.choice(
                        [z for z in range(n_zones) if z not in vulnerable_zones],
                        size=int(n_zones*0.3),
                        replace=False
                    )
                ])

            for zone in affected_zones:
                events.append({
                    'event_id': f'EVT{i:03d}',
                    'timestamp': event_date,
                    'zone_id': f'Z{zone:03d}',
                    'severity': severity,
                    'flooded': 1
                })

        df = pd.DataFrame(events)

        filepath = self.output_dir / 'synthetic_flood_labels.parquet'
        df.to_parquet(filepath, index=False)
        print(f"[OK] Labels de inundacion guardados: {filepath}")
        print(f"  - {n_events} eventos totales")
        print(f"  - {len(df)} registros zona-evento")

        return df

    def generate_all(self):
        """Genera todos los datos sintéticos necesarios para MVP"""
        print("="*60)
        print("GENERANDO DATOS SINTÉTICOS PARA MVP")
        print("="*60)

        # 1. Series temporales de lluvia
        rainfall = self.generate_rainfall_timeseries()

        # 2. Labels de zonas inundadas
        labels = self.generate_zone_flood_labels()

        print("\n" + "="*60)
        print("[OK] GENERACION COMPLETADA")
        print("="*60)
        print("\n[INFO] Estos datos sinteticos permiten:")
        print("   - Desarrollar y probar arquitectura del modelo")
        print("   - Validar pipeline de entrenamiento")
        print("   - Crear UI/UX funcional")
        print("\n[INFO] Despues del MVP, reemplazar con datos reales")

        return {
            'rainfall': rainfall,
            'labels': labels
        }

if __name__ == '__main__':
    generator = SyntheticDataGenerator()
    data = generator.generate_all()
