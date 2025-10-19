import pandas as pd
from openai import OpenAI
from config import DASHSCOPE_API_KEY, DATA_PATH

client = OpenAI(
    api_key=DASHSCOPE_API_KEY,
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)

def load_match_data(data_path: str) -> str:
    """Carga y resume datos del partido en texto plano."""
    df = pd.read_csv(data_path)
    summary = f"""
    Datos del partido:
    - Total de pases: {len(df[df['action'] == 'pass'])}
    - Duelos ganados: {len(df[df['outcome'] == 'won'])}
    - Pérdidas en campo rival: {len(df[(df['action'] == 'loss') & (df['zone'] == 'opponent_half')])}
    - Jugador con más recuperaciones: {df[df['action'] == 'recovery']['player'].mode().iloc[0] if not df[df['action'] == 'recovery'].empty else 'N/A'}
    """
    return summary.strip()

def enrich_analysis(video_analysis: str, data_summary: str) -> str:
    prompt = f"""
    Eres un analista táctico de élite. Combina el siguiente análisis visual y datos estadísticos para generar conclusiones accionables.

    ANÁLISIS VISUAL:
    {video_analysis}

    DATOS ESTADÍSTICOS:
    {data_summary}

    Instrucciones:
    - Identifica patrones entre lo que se ve y lo que dicen los números.
    - Sé conciso, técnico y orientado a la acción.
    - No repitas información; sintetiza.
    """
    
    response = client.chat.completions.create(
        model="qwen3-max",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    # Cargar análisis de video
    with open("reports/video_analysis_raw.txt", "r") as f:
        video_analysis = f.read()
    
    # Cargar y resumir datos
    data_summary = load_match_data(DATA_PATH)
    
    # Enriquecer con Qwen3-Max
    enriched_analysis = enrich_analysis(video_analysis, data_summary)
    
    # Guardar resultado
    with open("reports/enriched_analysis.txt", "w") as f:
        f.write(enriched_analysis)
    
    print("✅ Análisis enriquecido guardado en reports/enriched_analysis.txt")
