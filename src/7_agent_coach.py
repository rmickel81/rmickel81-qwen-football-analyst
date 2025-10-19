import os
from openai import OpenAI
from config import DASHSCOPE_API_KEY

client = OpenAI(
    api_key=DASHSCOPE_API_KEY,
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)

class TacticalAgent:
    def __init__(self):
        self.context = self._load_context()
        self.conversation_history = [
            {"role": "system", "content": self._get_system_prompt()}
        ]
    
    def _load_context(self) -> str:
        """Carga el contexto del partido desde los informes generados."""
        context_parts = []
        
        # Cargar análisis enriquecido
        if os.path.exists("reports/enriched_analysis.txt"):
            with open("reports/enriched_analysis.txt", "r") as f:
                context_parts.append("ANÁLISIS TÁCTICO:\n" + f.read())
        
        # Cargar simulación táctica
        if os.path.exists("reports/tactical_simulation.md"):
            with open("reports/tactical_simulation.md", "r") as f:
                content = f.read().replace("# Simulación Táctica", "")
                context_parts.append("SIMULACIÓN TÁCTICA:\n" + content)
        
        return "\n\n".join(context_parts) if context_parts else "No hay datos del partido disponibles."
    
    def _get_system_prompt(self) -> str:
        return f"""
Eres 'TactiQwen', el asistente táctico del cuerpo técnico. 
Tu conocimiento se basa en este contexto del partido actual:

{self.context}

REGLAS:
- Responde como un analista de élite: conciso, técnico y orientado a la acción.
- Si no sabes algo, di "No tengo datos suficientes sobre eso".
- Usa terminología futbolística precisa (ej.: 'presión alta', 'romper líneas', 'salida de balón').
- En chino, usa términos como '高位逼抢' o '穿透防线'.
- Máximo 3 oraciones por respuesta.
"""
    
    def ask(self, question: str) -> str:
        """Responde a una pregunta táctica del cuerpo técnico."""
        # Añadir pregunta al historial
        self.conversation_history.append({"role": "user", "content": question})
        
        # Obtener respuesta
        response = client.chat.completions.create(
            model="qwen3-max",
            messages=self.conversation_history,
            temperature=0.3  # Menos creatividad, más precisión
        )
        
        answer = response.choices[0].message.content
        self.conversation_history.append({"role": "assistant", "content": answer})
        
        return answer

def main():
    print("🧠 TACTIQWEN - Asistente Táctico en Vivo")
    print("=" * 50)
    print("Escribe tus preguntas tácticas. Escribe 'salir' para terminar.\n")
    
    agent = TacticalAgent()
    
    while True:
        question = input("❓ Pregunta del DT: ").strip()
        if question.lower() in ["salir", "exit", "quit"]:
            print("\n👋 ¡Hasta el próximo partido!")
            break
        
        if not question:
            continue
            
        answer = agent.ask(question)
        print(f"\n💡 TactiQwen: {answer}\n")

if __name__ == "__main__":
    main()
