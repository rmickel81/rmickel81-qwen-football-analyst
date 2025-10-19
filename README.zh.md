# 🧠⚽ rmickel81-qwen-football-analyst
**Qwen 打造的精英战术分析系统——从更衣室到云端。**

> *“我不自动化分析，而是用中国尖端的人工智能技术来增强分析。”*
> — **Roberto Mickel**，足球分析师兼人工智能专家

这个代码库是一个**综合性的足球分析系统**，它结合了**计算机视觉、战术推理、模拟和可视化**，使用了阿里云的**Qwen**系列模型。

由分析师设计，服务于分析师。

---

## 🌍 使命
通过将人工智能应用于足球，连接欧洲、拉丁美洲和中国，证明**中国顶尖技术是全球体育的战略工具**。

---

## 🚀 系统功能

### 1. **多模态视频分析** (`1_analyze_video.py`)
- 使用 **Qwen-VL** 处理比赛视频。
- 检测阵型、逼抢、失误和关键跑动。
- **输出**：纯文本战术分析。

### 2. **数据丰富** (`2_enrich_with_data.py`)
- 将可视化分析与统计数据 (CSV) 相结合。
- 使用 **思路链** 生成可操作的结论。
- **输出**：`enriched_analysis.txt`

### 3. **多语言报告** (`3_generate_report.py`)
- 生成**西班牙语、英语和中文**的专业报告。
- 精确的战术术语：
- 西语：*“high press”（高压逼抢），*“breaking lines”（突破防线）*
- 英语：*“high press”（高压逼抢），*“breaking lines”（突破防线）*
- 中语：**“高位逼抢”，**“穿透防线”**
- **输出**：`tactical_report_{ES,EN,ZH}.md`

### 4. **战术模拟** (`4_simulate_tactics.py`)
- 答案：*“如果……会怎样？”*
- *“换上伪9号位？”*
- *“如何压制对方的中场球员？”*
- **输出**：`tactical_simulation.md`，其中包含优势、风险和调整方案。

### 5. **实时分析** (`5_live_analysis.py`)
- 实时模拟战术指挥中心。
- 处理比赛期间的 30 秒片段。
- **输出**：`reports/live/minute_XX.md`

### 6. **战术可视化** (`6_visualize_heatmaps.py`)
- 根据追踪数据生成专业的**热图**。
- 包含足球场的绘图。
- **输出**：`reports/figures/heatmap_*.png`

### 7. **对话式战术助手** (`7_agent_coach.py​​`)
- 一个实时回答教练问题的 AI 代理。
- 了解比赛背景、统计数据和战术。
- 支持**西班牙语、英语和中文**。
- **运行**：`python src/7_agent_coach.py​​`

---

## 📊 典型工作流程

```bash
# 1. 分析视频
python src/1_analyze_video.py

# 2. 数据丰富
python src/2_enrich_with_data.py

# 3. 生成多语言报告
python src/3_generate_report.py

# 4. 模拟战术场景
python src/4_simulate_tactics.py

# 5. 使用热图进行可视化
python src/6_visualize_heatmaps.py

# 6. 激活战术向导
python src/7_agent_coach.py
