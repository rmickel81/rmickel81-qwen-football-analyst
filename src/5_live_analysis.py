import time
import os
from openai import OpenAI
from config import DASHSCOPE_API_KEY

client = OpenAI(
    api_key=DASHSCOPE_API_KEY,
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)

def analyze_live_clip(clip_path: str, minute: int, current_score: str) -> str:
    """Analiza un clip de 30 segundos como si fuera en vivo."""
    prompt = f"""
    Eres el analista en vivo del equipo. Estás viendo el minuto {minute} (resultado: {current_score}).
    Analiza este clip de 30 segundos y da un RESUMEN TÁCTICO EN TIEMPO REAL en 3 líneas:
    - Lo que está funcionando / fallando
    - Una recomendación inmediata para el banquillo
    - Un jugador a vigilar (propio o rival)
    
    Sé conciso, urgente y útil. Usa lenguaje de vestuario.
    """
    
    response = client.chat.completions.create(
        model="qwen-vl-plus",
        messages=[{
            "role": "user",
            "content": [
                {"type": "text", "text": prompt},
                {"type": "video_url", "video_url": {"url": clip_path}}
            ]
        }]
    )
    return response.choices[0].message.content

def simulate_live_analysis():
    """Simula un análisis en vivo minuto a minuto."""
    # Asegúrate de que la carpeta exista
    os.makedirs("reports/live", exist_ok=True)
    
    # Configuración del partido
    current_score = "1-0"
    clips = [
        ("video/clip_min15.mp4", 15),
        ("video/clip_min30.mp4", 30),
        ("video/clip_min45.mp4", 45),
    ]
    
    print("📡 INICIANDO ANÁLISIS EN VIVO...")
    print(f"Resultado actual: {current_score}\n")
    
    for clip_path, minute in clips:
        if not os.path.exists(clip_path):
            print(f"⚠️  Clip no encontrado: {clip_path}. Saltando...")
            continue
            
        print(f"[Minuto {minute}] Analizando...")
        insight = analyze_live_clip(clip_path, minute, current_score)
        
        # Guardar en archivo
        with open(f"reports/live/minute_{minute}.md", "w") as f:
            f.write(f"## Minuto {minute}\n\n{insight}")
        
        # Mostrar en consola con estilo "en vivo"
        print(f"✅ [MINUTO {minute}] {insight.replace(chr(10), ' | ')}\n")
        
        # Pausa simulada (en un sistema real, esto sería en tiempo real)
        time.sleep(2)
    
    print("🔚 Análisis en vivo completado. Archivos guardados en /reports/live/")

if __name__ == "__main__":
    simulate_live_analysis()
