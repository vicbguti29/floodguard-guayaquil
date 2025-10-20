# 🌊 FloodGuard - Sistema de Predicción de Inundaciones para Guayaquil

## 📋 Visión General

Sistema de alerta temprana de inundaciones para Guayaquil, Ecuador, utilizando arquitecturas avanzadas de Deep Learning (Transformers + Graph Neural Networks) para predecir eventos de inundación con 2-6 horas de anticipación.

## 🎯 Problema a Resolver

### Magnitud del Problema (Datos Reales)
- **73 eventos de inundación** en Guayaquil (2018-2024) - Fuente: SGR
- **$127 millones USD** en pérdidas económicas (2018-2024) - Fuente: Municipio/CAF
- **12 muertes** relacionadas con inundaciones en 6 años - Fuente: SGR/Cruz Roja
- **45,000+ personas afectadas** anualmente - Fuente: INEC

### Gap Tecnológico Actual
- **Sistemas actuales**: Reactivos (1-3h después del evento)
- **INAMHI**: Pronóstico genérico de 24-48h, ~65% precisión, sin granularidad por zonas
- **Municipio**: Sin predicción, solo respuesta a emergencias

### Nuestra Solución
- **Predicción anticipada**: 2-6 horas antes del evento
- **Granularidad espacial**: Por zona específica de Guayaquil
- **Meta de precisión**: >75% (F1-score)
- **Impacto estimado**: Reducir pérdidas en 20% = **$4.2M USD/año ahorrados**

📊 **Ver justificación completa con fuentes**: [docs/JUSTIFICACION_PROBLEMA.md](docs/JUSTIFICACION_PROBLEMA.md)

## 🏗️ Arquitectura Técnica

### Stack Tecnológico (100% Gratuito)

**Backend:**
- Python 3.10+
- PyTorch (deep learning framework)
- FastAPI (REST API)
- PostgreSQL + TimescaleDB (series temporales)

**Frontend:**
- React + Vite
- Mapbox GL JS (mapas interactivos - tier gratuito)
- Tailwind CSS (estilos)
- Recharts (gráficos)

**MLOps & Deployment:**
- Hugging Face Spaces (modelo deployment - gratis)
- Vercel (frontend - gratis)
- Supabase (PostgreSQL + storage - tier gratuito)
- GitHub Actions (CI/CD)

**Monitoreo:**
- Weights & Biases (tracking experimentos - gratis)
- Sentry (error tracking - tier gratuito)

### Arquitectura de Modelos

```
┌─────────────────────────────────────────────────────┐
│              INPUT: Datos Multi-Fuente              │
├─────────────────────────────────────────────────────┤
│ • Series temporales de lluvia (INAMHI/INOCAR)      │
│ • Topografía y red de drenaje (OpenStreetMap)      │
│ • Histórico de inundaciones (noticias/reportes)    │
└──────────────────┬──────────────────────────────────┘
                   │
        ┌──────────┴──────────┐
        ▼                     ▼
┌───────────────┐    ┌────────────────┐
│  TRANSFORMER  │    │  GRAPH NEURAL  │
│   TEMPORAL    │    │    NETWORK     │
├───────────────┤    ├────────────────┤
│ • Atención    │    │ • Relaciones   │
│   temporal    │    │   espaciales   │
│ • Predicción  │    │ • Propagación  │
│   series      │    │   inundación   │
└───────┬───────┘    └────────┬───────┘
        │                     │
        └──────────┬──────────┘
                   ▼
        ┌────────────────────┐
        │  FUSION LAYER      │
        │  (Atención Cruzada)│
        └──────────┬─────────┘
                   ▼
        ┌────────────────────┐
        │  OUTPUT            │
        ├────────────────────┤
        │ • Probabilidad     │
        │   inundación/zona  │
        │ • Tiempo estimado  │
        │ • Nivel de riesgo  │
        └────────────────────┘
```

## 📊 Fuentes de Datos

### Datos Meteorológicos
- **INAMHI**: Estaciones meteorológicas (precipitación, temperatura)
- **INOCAR**: Datos de mareas, nivel del mar
- API gratuita o web scraping de datos públicos

### Datos Geoespaciales
- **OpenStreetMap**: Topografía, red de alcantarillado, elevación
- **SRTM**: Modelo digital de elevación

### Datos Históricos
- **Web scraping**: El Universo, El Comercio (noticias de inundaciones)
- **SGR**: Reportes de emergencias (datos abiertos)
- **Twitter/X**: Reportes ciudadanos con geolocalización

## 🎨 UI/UX - Dashboard de Alertas

### Funcionalidades Principales

**1. Mapa Interactivo**
- Visualización en tiempo real de zonas de riesgo
- Código de colores: Verde (bajo), Amarillo (medio), Naranja (alto), Rojo (crítico)
- Click en zona para detalles específicos

**2. Panel de Predicción**
- Countdown a próxima posible inundación
- Nivel de confianza del modelo
- Historial de alertas recientes

**3. Gráficos Temporales**
- Precipitación últimas 24h vs predicción próximas 6h
- Tendencias históricas

**4. Notificaciones**
- Sistema de alertas push (navegador)
- Configuración por zona de interés

## 🚀 Roadmap Ágil (Sprints de 1 semana)

### Sprint 1: Fundación de Datos ✅ (Semana 1)
- [ ] Scraping de datos INAMHI/INOCAR
- [ ] Descarga de datos OpenStreetMap Guayaquil
- [ ] Web scraping de noticias históricas (2018-2025)
- [ ] Limpieza y estructuración de datasets
- [ ] EDA (Exploratory Data Analysis)

**Entregable**: Dataset limpio en formato CSV/Parquet

### Sprint 2: Modelo Transformer Temporal (Semana 2)
- [ ] Implementación de Transformer encoder desde cero
- [ ] Mecanismo de atención temporal
- [ ] Entrenamiento con series de precipitación
- [ ] Evaluación baseline (RMSE, MAE)

**Entregable**: Modelo predictor de lluvia funcional

### Sprint 3: Graph Neural Network (Semana 3)
- [ ] Construcción de grafo espacial de Guayaquil
- [ ] Implementación de GCN/GAT layers
- [ ] Modelado de propagación de agua
- [ ] Integración con topografía

**Entregable**: Modelo GNN de relaciones espaciales

### Sprint 4: Integración y API (Semana 4)
- [ ] Fusión de modelos Transformer + GNN
- [ ] Fine-tuning end-to-end
- [ ] Desarrollo de FastAPI REST API
- [ ] Endpoints: `/predict`, `/risk-zones`, `/historical`
- [ ] Documentación con Swagger

**Entregable**: API funcional en local

### Sprint 5: Frontend Dashboard (Semana 5)
- [ ] Setup React + Vite + Tailwind
- [ ] Integración Mapbox para mapa interactivo
- [ ] Componentes de visualización
- [ ] Conexión con API backend
- [ ] Diseño responsive (mobile-first)

**Entregable**: Dashboard funcional en local

### Sprint 6: Deployment & MVP (Semana 6)
- [ ] Deploy modelo en Hugging Face Spaces
- [ ] Deploy API en Railway/Render (gratis)
- [ ] Deploy frontend en Vercel
- [ ] Configuración CI/CD con GitHub Actions
- [ ] Testing end-to-end
- [ ] Documentación de usuario

**Entregable**: MVP en producción con URL pública

## 📈 Métricas de Éxito

### Técnicas
- **Precisión**: F1-score > 0.75 en detección de eventos de inundación
- **Anticipación**: Predicciones correctas con 2-6h de antelación
- **Falsos Positivos**: < 20% (para no desensibilizar a usuarios)

### Negocio/Impacto
- **Cobertura**: 80%+ de zonas críticas de Guayaquil monitoreadas
- **Latencia**: Predicción actualizada cada 30 minutos
- **Usuarios**: 100+ usuarios beta en primer mes

## 🔐 Consideraciones Éticas

- **Privacidad**: No se recopilan datos personales
- **Transparencia**: Modelo explicable, se muestran niveles de confianza
- **Accesibilidad**: Interfaz simple, alertas claras
- **Responsabilidad**: Disclaimers claros (herramienta de apoyo, no reemplaza autoridades)

## 📂 Estructura del Proyecto

```
floodguard/
├── data/
│   ├── raw/              # Datos sin procesar
│   ├── processed/        # Datos limpios
│   └── scripts/          # Scripts de scraping
├── models/
│   ├── transformer/      # Implementación Transformer
│   ├── gnn/              # Implementación GNN
│   ├── fusion/           # Modelo integrado
│   └── training/         # Scripts de entrenamiento
├── api/
│   ├── main.py           # FastAPI app
│   ├── routers/          # Endpoints
│   └── schemas/          # Pydantic models
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   └── services/
│   └── public/
├── notebooks/            # Jupyter notebooks (EDA, experimentos)
├── tests/                # Unit & integration tests
├── docs/                 # Documentación adicional
├── .github/workflows/    # CI/CD pipelines
├── requirements.txt      # Python dependencies
├── package.json          # Node dependencies
└── README.md             # Este archivo
```

## 🛠️ Setup Local

### Prerrequisitos
- Python 3.10+
- Node.js 18+
- Git

### Instalación

```bash
# Clonar repositorio
git clone https://github.com/tu-usuario/floodguard.git
cd floodguard

# Backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

# Frontend
cd frontend
npm install

# Variables de entorno
cp .env.example .env
# Configurar API keys en .env
```

### Ejecutar en desarrollo

```bash
# Terminal 1 - Backend
uvicorn api.main:app --reload

# Terminal 2 - Frontend
cd frontend
npm run dev
```

## 🤝 Contribuciones

Contactar a vborborgutierrez@gmail.com para colaboraciones.

## 📄 Licencia

MIT License - Uso libre con atribución

## 🙏 Agradecimientos

- INAMHI/INOCAR por datos meteorológicos públicos
- Comunidad de Guayaquil por retroalimentación

---

**Desarrollado con ❤️ para prevenir desastres y salvar vidas en Guayaquil**

---

## 📝 Estado Actual del Proyecto

**Versión:** MVP v0.1 (Deployado)
**Última actualización:** 2025-10-19
**🚀 DEMO EN VIVO:** https://problem-cymhca3op-victors-projects-3d84c218.vercel.app

### ✅ Completado
- [x] Estructura del proyecto y documentación
- [x] Datos sintéticos generados (lluvia + eventos)
- [x] Datos geoespaciales de Guayaquil (OpenStreetMap)
- [x] Control de versiones Git + GitHub
- [x] Landing page con mapa interactivo (MVP visual)
- [x] Deploy en Vercel (URL pública funcionando)

### 🚧 En Progreso
- [ ] Modelo LSTM baseline
- [ ] API REST con predicciones

### 📋 Roadmap Corto Plazo
1. **Hoy**: MVP deployado con mapa de zonas
2. **Mañana**: Modelo LSTM baseline + API
3. **Día 3**: Frontend conectado a predicciones reales
4. **Semana 2**: Mejorar a Transformer + datos reales

**Ver progreso detallado:** [CHANGELOG.md](CHANGELOG.md)

*Última actualización: 2025-10-19*
