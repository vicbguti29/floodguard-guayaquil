# 🎬 Script TikTok - FloodGuard Guayaquil

## Versión 1: Impacto del Problema (60 seg)

**[0-5s] HOOK:**
"¿Sabías que Guayaquil pierde $127 MILLONES de dólares cada 6 años por inundaciones?"

**[5-15s] PROBLEMA:**
"73 eventos de inundación desde 2018. 45 MIL personas afectadas CADA AÑO. 12 vidas perdidas. Y el sistema actual solo reacciona DESPUÉS de que ya inundó."

**[15-30s] SOLUCIÓN:**
"Estoy desarrollando FloodGuard: un sistema que predice inundaciones con 2-6 HORAS de anticipación usando Deep Learning. Transformer + Graph Neural Networks analizando lluvia en tiempo real y propagación espacial."

**[30-45s] DEMOSTRACIÓN:**
"[Mostrar mapa en pantalla] Este mapa muestra zonas de Guayaquil con niveles de riesgo. Verde = seguro. Amarillo = alerta. Rojo = evacuación inmediata. Actualizado cada 30 minutos."

**[45-60s] CALL TO ACTION:**
"Todavía está en Beta, pero podría salvar vidas en la próxima temporada invernal (enero-mayo). Link en bio para ver el demo. ¿Crees que algo así debería existir? Comenta 👇"

---

## Versión 2: Storytelling Personal (60 seg)

**[0-5s] HOOK:**
"Mi ciudad se inunda cada año y nadie hace nada al respecto... hasta ahora."

**[5-20s] PROBLEMA PERSONAL:**
"Soy de Guayaquil, Ecuador. Cada temporada invernal vemos las mismas noticias: calles inundadas, carros varados, familias perdiendo todo. 73 eventos en 6 años. Mi tesis en ESPOL: cambiar eso."

**[20-40s] LA SOLUCIÓN:**
"FloodGuard usa la misma tecnología que Tesla y Waymo para predecir inundaciones ANTES de que pasen. Transformer neural networks + datos meteorológicos = alertas 2-6 horas antes. Tiempo suficiente para evacuar y salvar vidas."

**[40-55s] EL RESULTADO:**
"[Mostrar demo en pantalla] Ya está funcionando en beta. Este mapa te dice exactamente qué sectores están en peligro. Gratis, open source, hecho en Ecuador."

**[55-60s] CTA:**
"Link en bio. Si conoces a alguien en Guayaquil, comparte esto. Podría salvarlo. 🌊"

---

## Versión 3: Técnico (Para audiencia tech) (60 seg)

**[0-5s] HOOK:**
"Construyendo un sistema de early warning con Transformers y GNNs. Les muestro el stack."

**[5-20s] EL PROBLEMA:**
"Guayaquil, Ecuador: 73 inundaciones en 6 años. $127M en pérdidas. Sistema actual: INAMHI predice lluvia genérica a 24-48h con ~65% accuracy. Sin granularidad espacial. Sin modelado de propagación."

**[20-45s] LA ARQUITECTURA:**
"Mi solución:
- Transformer temporal para series de precipitación (self-attention sobre ventanas de 24h)
- Graph Neural Network para propagación espacial (nodos = zonas, edges = flujo hidrológico)
- Fusion layer con cross-attention
- FastAPI backend, React frontend, deploy en Vercel
- 100% gratis: OSMnx, Leaflet, Hugging Face Spaces"

**[45-60s] RESULTADOS Y CTA:**
"MVP ya deployado. Datos sintéticos ahora (como Tesla/Waymo para training). Próximo paso: LSTM baseline → Transformer → integración datos reales INAMHI. Repo en GitHub (link en bio). ¿Sugerencias de arquitectura? Comenta."

---

## 🎯 Estrategia de Contenido

### Hashtags sugeridos:
- **Generales:** #tech #ai #deeplearning #machinelearning
- **Locales:** #guayaquil #ecuador #espol #inundaciones
- **Técnicos:** #transformer #neuralnetworks #pytorch #gnn
- **Impacto:** #socialimpact #climatetech #disasterprevention

### Formato visual:
1. **Versión 1 & 2:** B-roll de inundaciones reales en Guayaquil + screen recording del dashboard
2. **Versión 3:** Screen recording de código + arquitectura + terminal + dashboard

### Timing:
- **Publicar:** Noviembre-Diciembre (antes de temporada invernal enero-mayo)
- **Frecuencia:** 1 video/semana mientras desarrollas, mostrando progreso
- **Series:** "Construyendo FloodGuard - Día X"

---

## 📊 Métricas de Éxito (Validación de Interés)

### KPIs a medir:
1. **Engagement rate** > 5% = hay interés
2. **Shares** (especialmente de cuentas de Guayaquil) = validación local
3. **Comentarios preguntando "¿cuándo estará listo?"** = demand real
4. **Clicks al link** (trackeable con UTM en bio)

### Pivot si:
- < 100 views: Problema de alcance, mejorar hooks
- Alto views, bajo engagement: Contenido no conecta, cambiar ángulo
- Engagement alto pero cero shares: No ven utilidad práctica, enfocar en caso de uso

### Validación positiva si:
- Municipio/SGR/medios contactan
- Estudiantes/profes de ESPOL comparten
- Residentes de zonas vulnerables preguntan cómo usarlo

---

## 💡 Ideas de Follow-up Content

1. **"Así entrené el modelo"** - Mostrar training loop en vivo
2. **"Comparando mi modelo vs. INAMHI"** - Side by side de predicciones
3. **"Día que implementé el GNN"** - Explicar propagación espacial visual
4. **"Testing en inundación real"** - Si hay evento durante desarrollo
5. **"Open sourcing el proyecto"** - Call para colaboradores

---

## ⚠️ IMPORTANTE: Disclaimers

**SIEMPRE incluir en caption:**
> ⚠️ Proyecto académico/investigación en desarrollo. NO reemplaza alertas oficiales de INAMHI/SGR. Versión Beta con datos sintéticos. Sigue fuentes oficiales para emergencias reales.

**Evitar:**
- Prometer accuracy específica sin validación
- Decir "mejor que INAMHI" sin pruebas
- Generar pánico o falsa sensación de seguridad
- Monetización antes de validación

---

## 🎥 Producción Básica

**Equipo mínimo:**
- Smartphone con buena cámara
- Micrófono de solapa (calidad de audio > video)
- Grabador de pantalla (OBS/QuickTime)
- Editor simple (CapCut/iMovie)

**Tips:**
- Habla como si le explicaras a un amigo, no como paper académico
- Subtítulos SIEMPRE (80% ven sin sonido)
- Primera toma casi nunca es la buena, graba 3-5 versiones
- Engancha en primeros 3 segundos o pierdes al viewer

---

**Éxito del TikTok = Validación de problema real + Generación de expectativa + Posible colaboración/funding**
