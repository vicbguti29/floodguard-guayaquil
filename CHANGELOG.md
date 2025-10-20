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

### 🚧 En Progreso
- MVP deployable (landing page + mapa interactivo)
- Deploy en Vercel para URL pública

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
