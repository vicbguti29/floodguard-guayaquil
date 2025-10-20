# Changelog - FloodGuard

Registro de progreso real del proyecto (actualizado conforme avanzamos)

## [Unreleased] - 2025-10-19

### ✅ Completado
- Inicialización del proyecto y estructura de directorios
- Documentación: README.md, SPRINT_PLAN.md, JUSTIFICACION_PROBLEMA.md
- Stack tecnológico definido (100% gratuito)
- Datos sintéticos generados:
  - 17,521 registros de lluvia (2 años, horarios)
  - 24 eventos de inundación etiquetados
  - 143 registros zona-evento
- Datos geoespaciales reales descargados:
  - 840 zonas de Guayaquil (grid 2km x 2km)
  - Red de calles de OpenStreetMap
  - Cuerpos de agua (ríos, esteros)
- Control de versiones Git inicializado

### ✅ MVP Deployado - 2025-10-19
- **URL en vivo:** https://problem-cymhca3op-victors-projects-3d84c218.vercel.app
- Landing page funcional con:
  - Mapa interactivo de Guayaquil (Leaflet + OpenStreetMap)
  - 7 zonas mostradas con niveles de riesgo
  - Estadísticas reales del problema (73 eventos, $127M pérdidas, 45K afectados/año)
  - Justificación transparente de datos sintéticos
  - Disclaimer claro sobre versión Beta
- Repositorio GitHub público: https://github.com/vicbguti29/floodguard-guayaquil
- Deploy automático con Vercel

### ✅ Modelo LSTM + API Funcional - 2025-10-19 (Noche)

**Logros Opción A - Enfoque Ágil:**

1. **Modelo LSTM Baseline Entrenado**
   - Arquitectura: 2 capas LSTM (64 hidden units) + FC layers
   - Parámetros: 53,478 total
   - Input: 24h de historia (precipitación, temp, humedad, viento)
   - Output: Predicción próximas 6h
   - Training: 20 epochs, val loss 0.0043
   - Guardado en: `models/checkpoints/lstm_baseline_v1.pth`

2. **API REST Completamente Funcional**
   - FastAPI corriendo en localhost:8000
   - Endpoint `/api/v1/predict` con predicciones reales
   - Modelo carga automáticamente al startup
   - 7 zonas monitoreadas (Los Sauces, Guasmo, Bastión Popular, etc.)
   - Respuesta JSON con: risk_level, probability, estimated_time, confidence
   - CORS habilitado para frontend

3. **Testing Exitoso**
   - curl localhost:8000/api/v1/predict ✓
   - Predicciones dinámicas por zona ✓
   - Niveles de riesgo: low, medium, high, critical ✓

### 🚧 En Progreso
- Conectar frontend HTML con API backend
- Deploy de API en Railway/Render (producción)

### 📋 Pendiente
- Modelo LSTM baseline (iteración antes de Transformer)
- API REST funcional con predicciones
- Integración frontend-backend
- Recolección de datos meteorológicos reales
- Transformer + GNN (post-MVP)

### 🔄 Cambios de Estrategia
**Pivot a metodología ágil real:**
- ❌ **Antes**: Arquitectura completa primero, deploy después
- ✅ **Ahora**: Deploy rápido, iterar sobre funcionalidad
- **Razón**: Validar concepto con usuarios reales cuanto antes

**Justificación datos sintéticos:**
- Transparencia total en UI (badge "Beta - Datos Sintéticos")
- Ejemplos industria: Tesla, Waymo, OpenAI usan sintéticos
- Plan de migración a datos reales documentado

## Próximos Pasos Inmediatos
1. Landing page deployada (URL pública)
2. Mapa interactivo de Guayaquil con zonas
3. Predicciones dummy en interfaz
4. Conectar con modelo simple
5. Iterar basado en feedback

---

**Última actualización:** 2025-10-19 - Inicio de desarrollo MVP ágil
