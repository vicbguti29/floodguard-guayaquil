# 🏃 Plan de Sprints - FloodGuard

## Metodología Ágil - 6 Semanas a MVP

### Sprint 1: Fundación de Datos (Semana 1)
**Objetivo**: Obtener y limpiar datasets necesarios

#### User Stories
- [ ] Como científico de datos, necesito datos meteorológicos históricos de Guayaquil para entrenar el modelo
- [ ] Como científico de datos, necesito eventos históricos de inundaciones para labels de entrenamiento
- [ ] Como desarrollador, necesito datos geoespaciales de Guayaquil para el componente GNN

#### Tareas Técnicas
1. **Datos Meteorológicos** (2 días)
   - [ ] Investigar API/scraping de INAMHI
   - [ ] Implementar scraper para estaciones de Guayaquil
   - [ ] Descargar datos 2018-2025
   - [ ] Validar completitud de datos

2. **Datos de Inundaciones** (2 días)
   - [ ] Scraping de noticias El Universo/El Comercio
   - [ ] Extracción de fechas, zonas afectadas
   - [ ] Crear dataset de eventos históricos
   - [ ] Etiquetar severidad (manual + regex)

3. **Datos Geoespaciales** (1 día)
   - [ ] Descargar mapa de Guayaquil desde OpenStreetMap
   - [ ] Extraer red de alcantarillado, ríos, esteros
   - [ ] Obtener modelo digital de elevación (SRTM)
   - [ ] Dividir Guayaquil en grid/zonas

4. **EDA** (2 días)
   - [ ] Análisis exploratorio de series temporales
   - [ ] Correlaciones lluvia-inundaciones
   - [ ] Visualizaciones en Jupyter
   - [ ] Documentar insights

#### Criterios de Aceptación
- ✅ Dataset de lluvia con al menos 2 años de datos horarios
- ✅ Mínimo 50 eventos de inundación etiquetados
- ✅ Mapa de Guayaquil con 20+ zonas identificadas
- ✅ Notebook de EDA con visualizaciones claras

#### Entregables
- `data/raw/inamhi_2018_2025.parquet`
- `data/raw/flood_events.parquet`
- `data/raw/guayaquil_map.gpkg`
- `notebooks/01_eda.ipynb`

---

### Sprint 2: Modelo Transformer Temporal (Semana 2)
**Objetivo**: Implementar predictor de series temporales con Transformer

#### User Stories
- [ ] Como ML engineer, necesito un modelo que prediga lluvia futura basándose en histórico
- [ ] Como desarrollador, necesito código modular y reutilizable para el Transformer

#### Tareas Técnicas
1. **Arquitectura Transformer** (3 días)
   - [ ] Implementar Multi-Head Attention desde cero
   - [ ] Implementar Positional Encoding temporal
   - [ ] Implementar Encoder stack
   - [ ] Implementar Decoder con autoregressive prediction
   - [ ] Unit tests para cada componente

2. **Preparación de Datos** (1 día)
   - [ ] Pipeline de preprocessamiento
   - [ ] Normalización de features
   - [ ] Creación de sequences (ventanas temporales)
   - [ ] Train/val/test split temporal

3. **Entrenamiento** (2 días)
   - [ ] Configuración de hiperparámetros
   - [ ] Training loop con validación
   - [ ] Integración con Weights & Biases
   - [ ] Early stopping y checkpointing

4. **Evaluación** (1 día)
   - [ ] Métricas: RMSE, MAE, R²
   - [ ] Visualizaciones de predicciones
   - [ ] Análisis de errores
   - [ ] Comparación con baseline (ARIMA/LSTM simple)

#### Criterios de Aceptación
- ✅ Transformer implementado sin usar librerías de alto nivel (solo torch.nn básicos)
- ✅ RMSE en test set < 5mm en predicción de lluvia a 6h
- ✅ Experimentos loggeados en W&B
- ✅ Código documentado y con tests

#### Entregables
- `models/transformer/architecture.py`
- `models/transformer/train.py`
- `models/checkpoints/transformer_v1.pth`
- `notebooks/02_transformer_evaluation.ipynb`

---

### Sprint 3: Graph Neural Network Espacial (Semana 3)
**Objetivo**: Modelar propagación espacial de inundaciones

#### User Stories
- [ ] Como ML engineer, necesito capturar relaciones espaciales entre zonas de Guayaquil
- [ ] Como científico, necesito modelar cómo el agua se propaga de una zona a otra

#### Tareas Técnicas
1. **Construcción del Grafo** (2 días)
   - [ ] Definir nodos (zonas de Guayaquil)
   - [ ] Definir edges (conexiones hidrológicas)
   - [ ] Features de nodos (elevación, área, población)
   - [ ] Pesos de edges (distancia, pendiente, alcantarillado)

2. **Arquitectura GNN** (3 días)
   - [ ] Implementar Graph Convolution Layer (GCN)
   - [ ] Implementar Graph Attention Network (GAT) opcional
   - [ ] Message passing para propagación de agua
   - [ ] Integrar features temporales (del Transformer)

3. **Entrenamiento** (1 día)
   - [ ] Preparar labels (zonas inundadas por evento)
   - [ ] Training con eventos históricos
   - [ ] Validación cruzada espacial

4. **Evaluación** (1 día)
   - [ ] Precisión por zona
   - [ ] Matriz de confusión
   - [ ] Visualización en mapa

#### Criterios de Aceptación
- ✅ GNN con al menos 3 capas de convolución
- ✅ Accuracy > 70% en predicción de zonas afectadas
- ✅ Visualización de predicciones en mapa interactivo

#### Entregables
- `models/gnn/graph_builder.py`
- `models/gnn/architecture.py`
- `models/checkpoints/gnn_v1.pth`
- `notebooks/03_gnn_evaluation.ipynb`

---

### Sprint 4: Integración y API (Semana 4)
**Objetivo**: Fusionar modelos y crear API REST

#### User Stories
- [ ] Como desarrollador frontend, necesito una API para obtener predicciones
- [ ] Como data scientist, necesito integrar Transformer + GNN en pipeline único

#### Tareas Técnicas
1. **Fusión de Modelos** (2 días)
   - [ ] Arquitectura de fusión (attention-based)
   - [ ] Pipeline end-to-end: datos → Transformer → GNN → predicción
   - [ ] Fine-tuning conjunto
   - [ ] Optimización de inferencia

2. **API REST** (2 días)
   - [ ] Endpoints principales (ver README)
   - [ ] Schemas con Pydantic
   - [ ] Carga de modelos al startup
   - [ ] Caché de predicciones

3. **Base de Datos** (1 día)
   - [ ] Setup PostgreSQL + TimescaleDB
   - [ ] Tablas: zonas, predicciones, eventos
   - [ ] Queries optimizadas

4. **Testing** (2 días)
   - [ ] Unit tests para endpoints
   - [ ] Integration tests
   - [ ] Load testing básico
   - [ ] Documentación con Swagger

#### Criterios de Aceptación
- ✅ API funcionando localmente
- ✅ Latencia < 500ms para `/predict`
- ✅ Coverage de tests > 80%
- ✅ Documentación completa en Swagger

#### Entregables
- `models/fusion/integrated_model.py`
- `api/main.py` (completo)
- `api/routers/` (todos los endpoints)
- `tests/test_api.py`

---

### Sprint 5: Frontend Dashboard (Semana 5)
**Objetivo**: Crear interfaz de usuario intuitiva

#### User Stories
- [ ] Como ciudadano, necesito ver en un mapa qué zonas están en riesgo
- [ ] Como usuario, necesito entender el nivel de riesgo sin conocimientos técnicos
- [ ] Como residente de una zona, necesito recibir alertas cuando mi sector esté en riesgo

#### Tareas Técnicas
1. **Setup Frontend** (1 día)
   - [ ] Vite + React + TypeScript
   - [ ] Tailwind CSS
   - [ ] Axios para API calls
   - [ ] Routing con React Router

2. **Componentes Principales** (3 días)
   - [ ] Mapa interactivo con Mapbox
     - [ ] Capas de zonas con color por riesgo
     - [ ] Tooltips con detalles
     - [ ] Click para más información
   - [ ] Panel de predicciones
     - [ ] Lista de zonas de alto riesgo
     - [ ] Countdown a evento predicho
     - [ ] Nivel de confianza
   - [ ] Gráficos temporales
     - [ ] Precipitación histórica y predicha
     - [ ] Recharts para visualización
   - [ ] Sistema de notificaciones
     - [ ] Browser notifications API
     - [ ] Selector de zonas de interés

3. **UX/UI** (2 días)
   - [ ] Diseño responsive (mobile-first)
   - [ ] Paleta de colores accesible
   - [ ] Loading states
   - [ ] Error handling
   - [ ] Dark mode opcional

4. **Integración** (1 día)
   - [ ] Conectar con API backend
   - [ ] Polling automático cada 30min
   - [ ] Estado global (Context API o Zustand)

#### Criterios de Aceptación
- ✅ Dashboard funcional en desktop y mobile
- ✅ Mapa muestra todas las zonas con colores correctos
- ✅ Actualización automática cada 30 min
- ✅ Notificaciones funcionando

#### Entregables
- `frontend/src/` (código completo)
- `frontend/public/` (assets)
- Demo video del dashboard

---

### Sprint 6: Testing y Deployment (Semana 6)
**Objetivo**: Llevar a producción el MVP

#### User Stories
- [ ] Como usuario final, necesito acceder al sistema 24/7 desde internet
- [ ] Como desarrollador, necesito CI/CD automatizado
- [ ] Como equipo, necesitamos monitoring para detectar problemas

#### Tareas Técnicas
1. **Preparación para Deploy** (1 día)
   - [ ] Optimización de modelos (cuantización, ONNX)
   - [ ] Minificación de frontend
   - [ ] Variables de entorno para producción
   - [ ] Health checks

2. **Deployment Backend** (2 días)
   - [ ] Deploy modelo en Hugging Face Spaces
   - [ ] Deploy API en Railway/Render
   - [ ] Setup PostgreSQL en Supabase
   - [ ] Configurar CORS para producción

3. **Deployment Frontend** (1 día)
   - [ ] Build optimizado
   - [ ] Deploy en Vercel
   - [ ] Configurar variables de entorno
   - [ ] Custom domain (opcional)

4. **CI/CD** (1 día)
   - [ ] GitHub Actions para tests automáticos
   - [ ] Auto-deploy en push a main
   - [ ] Linting y formatting checks

5. **Monitoring** (1 día)
   - [ ] Integración con Sentry
   - [ ] Logs centralizados
   - [ ] Métricas de uso
   - [ ] Alertas por email si falla el servicio

6. **Testing Final** (1 día)
   - [ ] End-to-end testing en producción
   - [ ] Performance testing
   - [ ] Security checks básicos
   - [ ] Documentación de usuario final

#### Criterios de Aceptación
- ✅ Sistema accesible públicamente 24/7
- ✅ Uptime > 95%
- ✅ Errores monitoreados con Sentry
- ✅ CI/CD funcionando

#### Entregables
- URL pública del MVP
- Documentación de deployment
- Guía de usuario
- Presentación del proyecto (slides)

---

## Definición de "Done"

Para cada sprint, una tarea está "Done" cuando:
1. ✅ Código escrito y funcional
2. ✅ Tests pasando
3. ✅ Code review realizado (self-review mínimo)
4. ✅ Documentación actualizada
5. ✅ Merged a rama principal

## Retrospectivas

Al final de cada sprint:
- ¿Qué funcionó bien?
- ¿Qué puede mejorar?
- ¿Blockers encontrados?
- ¿Ajustes necesarios para próximo sprint?

## Notas Importantes

- **Flexibilidad**: Si un sprint se alarga, ajustar siguientes sin comprometer calidad
- **MVP First**: Si hay retrasos, priorizar funcionalidad core sobre features nice-to-have
- **Documentación continua**: No dejar para el final
- **Testing temprano**: Escribir tests desde Sprint 1

---

**¡Empecemos con Sprint 1! 🚀**
