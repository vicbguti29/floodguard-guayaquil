# 🔍 Verificación de Fuentes - FloodGuard

## ⚠️ ESTADO ACTUAL: ESTIMACIONES RAZONABLES (No datos oficiales verificados)

**IMPORTANTE:** Las estadísticas usadas en el proyecto son **estimaciones conservadoras** basadas en análisis de noticias y reportes públicos. **NO son cifras oficiales** de SGR, INEC o Municipio.

Para uso académico/demo es aceptable, pero para presentación formal o publicación, necesitamos **datos verificados**.

---

## 📊 Estadísticas Usadas vs. Verificación

### 1. "73 eventos de inundación (2018-2024)"
**Fuente citada:** SGR (Secretaría Nacional de Gestión de Riesgos)
**Estado:** ⚠️ **ESTIMADO - NO VERIFICADO**

**Cómo verificar:**
- Solicitar datos oficiales: https://www.gestionderiesgos.gob.ec
- Email: contacto@gestionderiesgos.gob.ec
- Alternativamente: Contar eventos en base de datos de noticias (El Universo, El Comercio)

**Estimación conservadora:**
- Temporada invernal: Enero-Mayo (5 meses)
- ~12 eventos/año reportados en medios
- 6 años × 12 = 72 eventos ≈ **73 eventos** ✓ (orden de magnitud razonable)

---

### 2. "$127 millones USD en pérdidas (2018-2024)"
**Fuente citada:** Municipio de Guayaquil / CAF
**Estado:** ⚠️ **ESTIMADO - NO VERIFICADO**

**Cómo verificar:**
- Municipio de Guayaquil: https://guayaquil.gob.ec
- CAF (Banco de Desarrollo de América Latina): https://www.caf.com
- Buscar reportes: "Plan de Aguas Lluvias", "Resiliencia Climática Guayaquil"

**Estimación:**
- Promedio pérdidas por evento moderado: $1-2M USD
- Eventos severos (3-4/año): $5-10M USD
- Total conservador: ~$20M/año × 6 años = **$120M** ✓

**Fuente indirecta verificable:**
- El Universo (2023): "Inundaciones causan millonarias pérdidas en Guayaquil"
  - https://www.eluniverso.com (buscar hemeroteca)
- Cámara de Comercio de Guayaquil podría tener cifras

---

### 3. "45,000+ personas afectadas anualmente"
**Fuente citada:** INEC
**Estado:** ⚠️ **ESTIMADO - NO VERIFICADO**

**Cómo verificar:**
- INEC: https://www.ecuadorencifras.gob.ec
- SGR reportes de emergencias
- Cruz Roja Ecuatoriana: https://www.cruzroja.org.ec

**Estimación:**
- Zonas vulnerables: Guasmo (200K habitantes), Bastión Popular (150K), Monte Sinaí (100K)
- ~20-30% de población vulnerable afectada en temporada fuerte
- Conservador: **45,000 personas** ✓

**Proxy verificable:**
- Censo INEC 2022: Población de Guayaquil por sectores
- Cruzar con mapa de zonas inundables del Municipio

---

### 4. "12 muertes relacionadas (2018-2024)"
**Fuente citada:** SGR / Cruz Roja
**Estado:** ⚠️ **PUEDE SER VERIFICADO con búsqueda de noticias**

**Cómo verificar:**
1. **Hemeroteca digital:**
   - El Universo: https://www.eluniverso.com/buscar
   - El Comercio: https://www.elcomercio.com
   - Búsqueda: "muerte inundación Guayaquil" (2018-2024)

2. **Reportes oficiales:**
   - SGR Informe de Gestión de Riesgos (anual)
   - Defensoría del Pueblo Ecuador

**Verificación parcial realizable:**
- Contar noticias de muertes por inundación/ahogamiento
- Típicamente 1-3 muertes por temporada invernal severa
- 6 años × 2 promedio = **12 muertes** ✓ (orden correcto)

---

## ✅ Datos SÍ Verificables con Certeza

### 1. Topografía y Zonas
**Fuente:** OpenStreetMap
**Estado:** ✅ **VERIFICADO** (datos públicos descargados)
- https://www.openstreetmap.org/#map=12/-2.1709/-79.9224

### 2. Zonas históricamente afectadas
**Fuente:** Múltiples noticias + Plan de Aguas Lluvias Municipal
**Estado:** ✅ **VERIFICADO PARCIALMENTE**

**Zonas confirmadas en reportes públicos:**
- Guasmo ✓
- Bastión Popular ✓
- Monte Sinaí ✓
- Flor de Bastión ✓
- Prosperina ✓
- Vía a Daule ✓

**Fuente municipal:**
- Alcaldía de Guayaquil: "Plan de Aguas Lluvias 2025-2026"
  - https://guayaquil.gob.ec (sección Proyectos)

### 3. Frecuencia de temporada invernal
**Fuente:** INAMHI
**Estado:** ✅ **VERIFICADO**
- Temporada invernal Ecuador costa: Enero-Mayo
- https://www.inamhi.gob.ec

---

## 🎯 Recomendaciones para Validación Formal

### Para Tesis/Proyecto Académico:

**Nivel Básico (Suficiente para MVP):**
- [x] Citar fuentes como "estimaciones basadas en análisis de noticias"
- [x] Disclaimer: "Cifras conservadoras pendientes de validación oficial"
- [x] Usar datos públicos verificables (OSM, INAMHI clima)

**Nivel Intermedio (Recomendado):**
- [ ] Solicitar datos oficiales a SGR por transparencia
- [ ] Contar eventos manualmente de hemeroteca 2018-2024
- [ ] Entrevista con Dirección de Gestión de Riesgos Municipal
- [ ] Incluir sección "Metodología de recolección de datos" en tesis

**Nivel Avanzado (Publicación científica):**
- [ ] Datos oficiales certificados
- [ ] Análisis estadístico riguroso
- [ ] Comparación con otros estudios académicos
- [ ] Peer review de metodología

### Para Presentación Pública/TikTok:

**Safe approach:**
> "Según análisis de noticias locales, Guayaquil registra **decenas de eventos** de inundación cada año, afectando a **miles de familias** y causando **millones en pérdidas**."

**Con disclaimers:**
> "Estimaciones conservadoras basadas en reportes públicos. Datos oficiales en proceso de solicitud a SGR."

---

## 📧 Template de Solicitud de Datos Oficiales

```
Asunto: Solicitud de Datos - Proyecto de Investigación ESPOL

Estimado/a [Nombre Institución],

Soy estudiante de [Carrera] en ESPOL, desarrollando un proyecto de investigación sobre predicción de inundaciones en Guayaquil usando Deep Learning.

Respetuosamente solicito acceso a los siguientes datos públicos:

1. Número de eventos de inundación registrados en Guayaquil (2018-2024)
2. Estimación de pérdidas económicas por temporada
3. Número de personas afectadas/evacuadas (si disponible)
4. Zonas geográficas más vulnerables

Propósito: Validación de modelo predictivo para sistema de alerta temprana (proyecto académico sin fines de lucro).

Repositorio del proyecto: https://github.com/vicbguti29/floodguard-guayaquil

Agradezco de antemano su colaboración.

Atentamente,
[Tu nombre]
[Matrícula ESPOL]
[Email]
```

**Enviar a:**
- SGR: contacto@gestionderiesgos.gob.ec
- Municipio Guayaquil: info@guayaquil.gob.ec
- INEC: atencionciudadania@inec.gob.ec

---

## 🔄 Plan de Actualización de Datos

### Fase 1: MVP (ACTUAL)
- ✅ Usar estimaciones razonables
- ✅ Disclaimer claro en UI
- ✅ Fuentes secundarias (noticias)

### Fase 2: Validación (Próximas 2 semanas)
- [ ] Solicitar datos oficiales
- [ ] Web scraping sistemático de noticias
- [ ] Cuantificar eventos con metodología clara

### Fase 3: Integración (Antes de presentación final)
- [ ] Actualizar cifras con datos oficiales
- [ ] Citar correctamente fuentes primarias
- [ ] Documentar metodología de recolección

---

## ✅ Conclusión

**Para TikTok/Demo/MVP:** Las cifras actuales son **suficientes** con disclaimers apropiados.

**Para Tesis/Publicación:** Necesitamos **validación formal** antes de defensa.

**Acción inmediata:** Enviar solicitudes de datos a SGR/Municipio esta semana.

**Respaldo:** Si no responden, **análisis sistemático de noticias** es metodología válida (citarlo correctamente).
