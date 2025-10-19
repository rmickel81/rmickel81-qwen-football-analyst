from openai import OpenAI
from config import DASHSCOPE_API_KEY, VIDEO_PATH

client = OpenAI(
    api_key=DASHSCOPE_API_KEY,
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)

def analyze_video(video_path: str) -> str:
    with open("prompts/prompt_video_analysis.txt", "r") as f:
        prompt_text = f.read()
    
    response = client.chat.completions.create(
        model="qwen-vl-plus",
        messages=[{
            "role": "user",
            "content": [
                {"type": "text", "text": prompt_text},
                {"type": "video_url", "video_url": {"url": video_path}}
            ]
        }]
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    result = analyze_video(VIDEO_PATH)
    with open("reports/video_analysis_raw.txt", "w") as f:
        f.write(result)
    print("✅ Análisis de video completado. Guardado en reports/video_analysis_raw.txt")
