"""
Descargar datos geoespaciales de Guayaquil desde OpenStreetMap
Usando OSMnx para obtener red de calles, edificios, y características geográficas
"""

import osmnx as ox
import geopandas as gpd
from pathlib import Path
import matplotlib.pyplot as plt

class GuayaquilMapDownloader:
    """Descarga y procesa datos geoespaciales de Guayaquil"""

    def __init__(self, output_dir='../raw'):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

        # Bounding box de Guayaquil
        self.place_name = "Guayaquil, Ecuador"

        # Coordenadas aproximadas del centro de Guayaquil
        self.center_point = (-2.1709, -79.9224)
        self.radius = 15000  # 15km radio desde el centro

    def download_street_network(self):
        """Descarga red de calles"""
        print(f"Descargando red de calles de {self.place_name}...")

        try:
            # Descargar red vial
            G = ox.graph_from_place(self.place_name, network_type='drive')

            # Guardar como GeoPackage
            filepath = self.output_dir / 'guayaquil_streets.gpkg'
            ox.save_graph_geopackage(G, filepath=filepath)
            print(f"[OK] Red de calles guardada en {filepath}")

            return G
        except Exception as e:
            print(f"Error descargando calles: {e}")
            return None

    def download_buildings(self):
        """Descarga edificios y estructuras"""
        print(f"Descargando edificios de {self.place_name}...")

        try:
            tags = {'building': True}
            gdf = ox.features_from_place(self.place_name, tags=tags)

            filepath = self.output_dir / 'guayaquil_buildings.gpkg'
            gdf.to_file(filepath, driver='GPKG')
            print(f"[OK] Edificios guardados en {filepath}")

            return gdf
        except Exception as e:
            print(f"Error descargando edificios: {e}")
            return None

    def download_waterways(self):
        """Descarga ríos, esteros, cuerpos de agua"""
        print(f"Descargando cuerpos de agua de {self.place_name}...")

        try:
            tags = {'natural': ['water', 'wetland'], 'waterway': True}
            gdf = ox.features_from_place(self.place_name, tags=tags)

            filepath = self.output_dir / 'guayaquil_waterways.gpkg'
            gdf.to_file(filepath, driver='GPKG')
            print(f"[OK] Cuerpos de agua guardados en {filepath}")

            return gdf
        except Exception as e:
            print(f"Error descargando agua: {e}")
            return None

    def create_zones_grid(self, grid_size=1000):
        """
        Crear grid de zonas para monitoreo

        Args:
            grid_size: Tamaño de cada celda en metros
        """
        print(f"Creando grid de zonas ({grid_size}m x {grid_size}m)...")

        try:
            # Obtener boundary de Guayaquil
            gdf_boundary = ox.geocode_to_gdf(self.place_name)

            # Crear grid
            from shapely.geometry import box
            import numpy as np

            bounds = gdf_boundary.total_bounds  # minx, miny, maxx, maxy

            # Convertir a metros aproximados (1 grado ≈ 111km)
            x_cells = int((bounds[2] - bounds[0]) * 111000 / grid_size)
            y_cells = int((bounds[3] - bounds[1]) * 111000 / grid_size)

            # Crear celdas
            x_coords = np.linspace(bounds[0], bounds[2], x_cells)
            y_coords = np.linspace(bounds[1], bounds[3], y_cells)

            cells = []
            for i, x in enumerate(x_coords[:-1]):
                for j, y in enumerate(y_coords[:-1]):
                    cell = box(x, y, x_coords[i+1], y_coords[j+1])
                    cells.append({
                        'zone_id': f'Z{i:03d}{j:03d}',
                        'geometry': cell
                    })

            gdf_grid = gpd.GeoDataFrame(cells, crs='EPSG:4326')

            filepath = self.output_dir / f'guayaquil_zones_grid_{grid_size}m.gpkg'
            gdf_grid.to_file(filepath, driver='GPKG')
            print(f"[OK] Grid de {len(gdf_grid)} zonas guardado en {filepath}")

            return gdf_grid

        except Exception as e:
            print(f"Error creando grid: {e}")
            return None

    def download_all(self):
        """Descarga todos los datos necesarios para MVP"""
        print("="*60)
        print("DESCARGANDO DATOS GEOESPACIALES DE GUAYAQUIL")
        print("="*60)

        # 1. Red de calles
        streets = self.download_street_network()

        # 2. Edificios (opcional para MVP, comentar si es muy lento)
        # buildings = self.download_buildings()

        # 3. Cuerpos de agua (importante para modelo)
        waterways = self.download_waterways()

        # 4. Grid de zonas de monitoreo
        zones = self.create_zones_grid(grid_size=2000)  # 2km x 2km para MVP

        print("\n" + "="*60)
        print("[OK] DESCARGA COMPLETADA")
        print("="*60)

        return {
            'streets': streets,
            'waterways': waterways,
            'zones': zones
        }

if __name__ == '__main__':
    downloader = GuayaquilMapDownloader()
    data = downloader.download_all()
