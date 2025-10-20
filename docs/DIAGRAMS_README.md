# 📐 Diagramas de Arquitectura FloodGuard

## Archivos PlantUML Incluidos

Este documento contiene 4 diagramas PlantUML que explican la arquitectura de FloodGuard:

### 1. **FloodGuard_Architecture_Complete**
Diagrama completo del sistema mostrando:
- Inputs: Series temporales + datos geoespaciales
- Transformer temporal con mecanismo de atención
- Graph Neural Network para propagación espacial
- Fusion layer que combina ambos
- Outputs: Predicciones por zona

**Uso:** Presentaciones técnicas, paper, documentación completa

---

### 2. **Transformer_Attention_Mechanism**
Detalle del mecanismo de atención:
- Query, Key, Value matrices
- Cálculo de attention scores
- Softmax y weighted values
- Intuición de cómo funciona

**Uso:** Explicar cómo el Transformer captura patrones temporales en lluvia

---

### 3. **GNN_Message_Passing**
Explicación de Graph Neural Network:
- Grafo de zonas de Guayaquil
- Message passing entre nodos
- Actualización de probabilidades por propagación
- Ejemplo concreto con 4 zonas

**Uso:** Mostrar cómo se modela la propagación espacial del agua

---

### 4. **FloodGuard_Simple_Flow**
Versión simplificada para audiencia no técnica:
- Flujo lineal: Input → Transformer → GNN → Fusión → Output
- Sin detalles matemáticos
- Enfocado en qué hace cada componente

**Uso:** TikTok, pitch a no-técnicos, redes sociales

---

## Cómo Renderizar los Diagramas

### Opción 1: Online (Más fácil)
1. Ve a: http://www.plantuml.com/plantuml/uml/
2. Copia y pega el contenido de `architecture_diagrams.puml`
3. Click en "Submit" para generar la imagen
4. Descarga como PNG/SVG

### Opción 2: VS Code (Recomendado para editar)
1. Instala extensión "PlantUML" en VS Code
2. Abre `architecture_diagrams.puml`
3. Presiona `Alt+D` para preview
4. Click derecho → "Export Current Diagram" para guardar

### Opción 3: CLI (Para automatizar)
```bash
# Instalar PlantUML
npm install -g node-plantuml

# Generar PNG
puml generate architecture_diagrams.puml -o output.png

# Generar SVG (mejor para slides)
puml generate architecture_diagrams.puml -o output.svg
```

### Opción 4: Docker (Sin instalación local)
```bash
docker run -v $(pwd):/data plantuml/plantuml architecture_diagrams.puml
```

---

## Uso en Presentaciones

### PowerPoint/Keynote
- Exportar como **SVG** (escalable, mejor calidad)
- Importar directamente en slides

### LaTeX/Paper
```latex
\begin{figure}[h]
\centering
\includegraphics[width=0.8\textwidth]{architecture_diagrams.png}
\caption{Arquitectura FloodGuard: Transformer + GNN}
\label{fig:architecture}
\end{figure}
```

### Markdown/GitHub
```markdown
![FloodGuard Architecture](docs/architecture_diagrams.png)
```

---

## Uso en TikTok Video

### Recomendación:
Usar **FloodGuard_Simple_Flow** (el último diagrama)

**Pasos:**
1. Renderizar como PNG alta resolución (1080x1080)
2. Animar con CapCut:
   - Mostrar cada sección progresivamente
   - Zoom in en partes clave
   - Overlay de texto explicativo
3. Duración: 10-15 segundos del video

**Script sugerido:**
```
[Mostrar INPUT]
"Analizamos las últimas 24 horas de lluvia..."

[Mostrar TRANSFORMER]
"El Transformer predice cuándo lloverá usando atención temporal..."

[Mostrar GNN]
"El Graph Neural Network modela cómo se propaga el agua entre zonas..."

[Mostrar FUSION]
"Combinamos ambas predicciones..."

[Mostrar OUTPUT]
"Y obtenemos alertas específicas por sector, 2-6 horas antes."
```

---

## Personalización

### Cambiar colores
```plantuml
skinparam backgroundColor #FFFFFF
skinparam componentBackgroundColor #LightBlue
skinparam componentBorderColor #Navy
```

### Cambiar fuente
```plantuml
skinparam defaultFontName Helvetica
skinparam defaultFontSize 14
```

### Agregar logo
```plantuml
sprite $logo [16x16/16] {
    0000000000000000
    0001111111110000
    ...
}

title <$logo> FloodGuard Architecture
```

---

## Exportar para Paper Académico

### Formato recomendado:
- **Vector:** PDF o SVG (mejor calidad)
- **Raster:** PNG a 300 DPI mínimo

### Comando:
```bash
plantuml -tsvg architecture_diagrams.puml
plantuml -tpdf architecture_diagrams.puml
```

---

## Troubleshooting

### "Graphviz not found"
```bash
# Ubuntu/Debian
sudo apt-get install graphviz

# macOS
brew install graphviz

# Windows
choco install graphviz
```

### "Syntax error in PlantUML"
- Verificar que todas las comillas sean rectas (" no ")
- Verificar balance de {} y []
- Usar preview online para debug

---

## Recursos Adicionales

- **PlantUML Documentation:** https://plantuml.com/
- **Gallery de ejemplos:** https://real-world-plantuml.com/
- **Cheatsheet:** https://plantuml.com/guide

---

## Para el Video de TikTok

**Diagrama recomendado:** `FloodGuard_Simple_Flow`

**Resolución sugerida:** 1080x1350 (vertical)

**Pasos para crear versión vertical:**
1. Renderizar diagrama
2. Abrir en Photoshop/Canva
3. Canvas 1080x1350
4. Agregar:
   - Logo FloodGuard arriba
   - Diagrama en centro
   - Texto explicativo abajo
   - Colores: Azul (#2563eb) y gradientes

**Ejemplo de layout:**
```
┌─────────────────┐
│  🌊 FloodGuard  │ ← Logo + título
├─────────────────┤
│                 │
│   [DIAGRAMA]    │ ← Diagrama centrado
│                 │
├─────────────────┤
│ "Predice        │
│  inundaciones   │ ← Texto explicativo
│  2-6h antes"    │
└─────────────────┘
```

---

**Actualizado:** 2025-10-19
**Autor:** Victor Borja Gutierrez
**Licencia:** MIT (igual que el proyecto)
