# 🧠⚽ rmickel81-qwen-football-analyst  
**El sistema de análisis táctico de élite con Qwen —desde el vestuario hasta la nube.**

> *"No automatizo el análisis. Lo aumento con IA china de vanguardia."*  
> — **Roberto Mickel**, Analista de Fútbol & Especialista en IA

Este repositorio es un **sistema integral de análisis futbolístico** que combina **visión por ordenador, razonamiento táctico, simulación y visualización** usando la familia de modelos **Qwen** de Alibaba Cloud.  
Diseñado por un analista, para analistas.

---

## 🌍 Misión
Conectar Europa, Latinoamérica y China a través de la IA aplicada al fútbol, demostrando que **la tecnología china de élite es una herramienta estratégica para el deporte global**.

---

## 🚀 Capacidades del sistema

### 1. **Análisis multimodal de video** (`1_analyze_video.py`)
- Procesa videos de partidos con **Qwen-VL**.
- Detecta formaciones, presión, pérdidas y movimientos clave.
- **Salida**: Análisis táctico en texto plano.

### 2. **Enriquecimiento con datos** (`2_enrich_with_data.py`)
- Combina el análisis visual con estadísticas (CSV).
- Usa **Chain-of-Thought** para generar conclusiones accionables.
- **Salida**: `enriched_analysis.txt`

### 3. **Informes multilingües** (`3_generate_report.py`)
- Genera informes profesionales en **español, inglés y chino**.
- Terminología táctica precisa:  
  - ES: *"presión alta"*, *"romper líneas"*  
  - EN: *"high press"*, *"breaking lines"*  
  - ZH: **"高位逼抢 (gāowèi bī qiǎng)"**, **"穿透防线 (chuān tòu fáng xiàn)"**
- **Salida**: `tactical_report_{ES,EN,ZH}.md`

### 4. **Simulación táctica** (`4_simulate_tactics.py`)
- Responde: *"¿Qué pasa si...?"*  
  - *"¿Cambiamos a falso 9?"*  
  - *"¿Cómo neutralizar a su mediocentro?"*
- **Salida**: `tactical_simulation.md` con ventajas, riesgos y ajustes.

### 5. **Análisis en vivo** (`5_live_analysis.py`)
- Simula un centro de operaciones táctico en tiempo real.
- Procesa clips de 30 segundos durante el partido.
- **Salida**: `reports/live/minute_XX.md`

### 6. **Visualización táctica** (`6_visualize_heatmaps.py`)
- Genera **mapas de calor** profesionales a partir de datos de tracking.
- Incluye dibujo del campo de fútbol.
- **Salida**: `reports/figures/heatmap_*.png`

### 7. **Asistente táctico conversacional** (`7_agent_coach.py`)
- Un agente de IA que responde preguntas del cuerpo técnico en tiempo real.
- Entiende contexto del partido, estadísticas y táctica.
- Soporta **español, inglés y chino**.
- **Ejecuta**: `python src/7_agent_coach.py`

---

## 📊 Flujo de trabajo típico

```bash
# 1. Analiza el video
python src/1_analyze_video.py

# 2. Enriquece con datos
python src/2_enrich_with_data.py

# 3. Genera informes multilingües
python src/3_generate_report.py

# 4. Simula escenarios tácticos
python src/4_simulate_tactics.py

# 5. Visualiza con mapas de calor
python src/6_visualize_heatmaps.py

# 6. Activa el asistente táctico
python src/7_agent_coach.py
