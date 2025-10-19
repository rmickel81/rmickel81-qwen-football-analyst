from openai import OpenAI
from config import DASHSCOPE_API_KEY, LANGUAGES

client = OpenAI(
    api_key=DASHSCOPE_API_KEY,
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)

def translate_report(content: str, lang: str) -> str:
    language_prompts = {
        "ES": "Escribe un informe táctico profesional en español. Usa términos como 'presión alta', 'romper líneas', 'salida de balón'.",
        "EN": "Write a professional tactical report in English. Use terms like 'high press', 'breaking lines', 'build-up play'.",
        "ZH": "用专业足球术语撰写中文战术报告。使用术语如'高位逼抢'、'穿透防线'、'后场组织'。"
    }
    
    prompt = f"""
    {language_prompts[lang]}
    
    Basado en este análisis:
    {content}
    
    Formato:
    - Título: 'Informe Táctico Post-Partido'
    - Secciones: 'Observaciones Clave', 'Recomendaciones'
    - Máximo 200 palabras.
    """
    
    response = client.chat.completions.create(
        model="qwen3-max",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    # Cargar análisis enriquecido
    with open("reports/enriched_analysis.txt", "r") as f:
        content = f.read()
    
    # Generar informes en cada idioma
    for lang in LANGUAGES:
        report = translate_report(content, lang)
        ext = {"ES": "ES", "EN": "EN", "ZH": "ZH"}[lang]
        with open(f"reports/tactical_report_{ext}.md", "w") as f:
            f.write(report)
        print(f"✅ Informe en {lang} guardado: reports/tactical_report_{ext}.md")
    
    print("\n🎉 ¡Flujo completado! Tus informes están listos en /reports/")
