from openai import OpenAI
from config import DASHSCOPE_API_KEY

client = OpenAI(
    api_key=DASHSCOPE_API_KEY,
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)

def simulate_tactical_scenario(scenario: str, opponent_profile: str) -> str:
    """
    Simula un escenario táctico usando Chain-of-Thought y conocimiento futbolístico.
    
    Args:
        scenario: Ej. "Cambiar a falso 9", "Presión ultra alta", "Defensa de 3"
        opponent_profile: Perfil del rival (puede venir de enriched_analysis.txt)
    """
    prompt = f"""
    Eres un analista táctico de élite con experiencia en LaLiga, Premier League y Superliga China.
    Simula el impacto del siguiente escenario táctico contra un rival con este perfil:
    
    PERFIL DEL RIVAL:
    {opponent_profile}
    
    ESCENARIO A SIMULAR:
    {scenario}
    
    Responde en este formato:
    1. **Ventajas**: Máximo 3 puntos.
    2. **Riesgos**: Máximo 3 puntos.
    3. **Ajustes clave**: 2-3 instrucciones específicas para los jugadores.
    4. **Probabilidad de éxito**: Alta / Media / Baja (justifica en 10 palabras).
    
    Sé preciso, realista y basado en principios tácticos modernos.
    """
    
    response = client.chat.completions.create(
        model="qwen3-max",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    # Cargar perfil del rival (del análisis enriquecido)
    try:
        with open("reports/enriched_analysis.txt", "r") as f:
            opponent_profile = f.read()[:1500]  # Tomamos los primeros 1500 caracteres
    except FileNotFoundError:
        opponent_profile = "Rival con mediocentro que rompe líneas y defensa alta."
    
    # Escenario a simular (¡puedes cambiarlo!)
    scenario = "Cambiar a un falso 9 para atraer a la defensa rival y crear espacios"
    
    # Simular
    simulation = simulate_tactical_scenario(scenario, opponent_profile)
    
    # Guardar resultado
    with open("reports/tactical_simulation.md", "w") as f:
        f.write(f"# Simulación Táctica\n\n**Escenario**: {scenario}\n\n{simulation}")
    
    print("✅ Simulación táctica guardada en reports/tactical_simulation.md")
    print("\n" + "="*50)
    print(simulation)
