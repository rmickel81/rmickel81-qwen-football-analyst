# 🧠⚽ rmickel81-qwen-football-analyst
**The elite tactical analysis system with Qwen—from the locker room to the cloud.**

> *"I don't automate the analysis. I augment it with cutting-edge Chinese AI."*
> — **Roberto Mickel**, Football Analyst & AI Specialist

This repository is a **comprehensive football analysis system** that combines **computer vision, tactical reasoning, simulation, and visualization** using Alibaba Cloud's **Qwen** family of models.

Designed by an analyst, for analysts.

---

## 🌍 Mission
To connect Europe, Latin America, and China through AI applied to football, demonstrating that **elite Chinese technology is a strategic tool for global sport**.

---

## 🚀 System Capabilities

### 1. **Multimodal Video Analysis** (`1_analyze_video.py`)
- Process match videos with **Qwen-VL**.
- Detect formations, pressing, turnovers, and key movements.
- **Output**: Plain text tactical analysis.

### 2. **Data Enrichment** (`2_enrich_with_data.py`)
- Combine visual analysis with statistics (CSV).
- Use **Chain-of-Thought** to generate actionable conclusions.
- **Output**: `enriched_analysis.txt`

### 3. **Multilingual Reports** (`3_generate_report.py`)
- Generate professional reports in **Spanish, English, and Chinese**.
- Precise tactical terminology:
- ES: *"high press"*, *"breaking lines"*
- EN: *"high press"*, *"breaking lines"*
- ZH: **"高位逼抢 (gāowèi bī qiǎng)"**, **"穿透防线 (chuān tòu fáng xiàn)"**
- **Output**: `tactical_report_{ES,EN,ZH}.md`

### 4. **Tactical Simulation** (`4_simulate_tactics.py`)
- Answers: *"What if...?"*
- *"Switch to a false 9?"*
- *"How to neutralize their central midfielder?"*
- **Output**: `tactical_simulation.md` with advantages, risks, and adjustments.

### 5. **Live Analysis** (`5_live_analysis.py`)
- Simulates a tactical operations center in real time.
- Processes 30-second clips during the match.
- **Output**: `reports/live/minute_XX.md`

### 6. **Tactical Visualization** (`6_visualize_heatmaps.py`)
- Generates professional **heatmaps** from tracking data.
- Includes a drawing of the football pitch.
- **Output**: `reports/figures/heatmap_*.png`

### 7. **Conversational Tactical Assistant** (`7_agent_coach.py`)
- An AI agent that answers coaching questions in real time.
- Understands match context, statistics, and tactics.
- Supports **Spanish, English, and Chinese**.
- **Run**: `python src/7_agent_coach.py`

---

## 📊 Typical Workflow

```bash
# 1. Analyze the video
python src/1_analyze_video.py

# 2. Enrich with data
python src/2_enrich_with_data.py

# 3. Generate multilingual reports
python src/3_generate_report.py

# 4. Simulate tactical scenarios
python src/4_simulate_tactics.py

# 5. Visualize with heatmaps
python src/6_visualize_heatmaps.py

# 6. Activate the tactical wizard
python src/7_agent_coach.py
