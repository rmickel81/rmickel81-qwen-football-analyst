import os
from dotenv import load_dotenv

load_dotenv()

DASHSCOPE_API_KEY = os.getenv("DASHSCOPE_API_KEY")
VIDEO_PATH = os.getenv("VIDEO_PATH", "video/sample_match_clip.mp4")
DATA_PATH = os.getenv("DATA_PATH", "data/sample_match_events.csv")

# Idiomas soportados
LANGUAGES = ["ES", "EN", "ZH"]
