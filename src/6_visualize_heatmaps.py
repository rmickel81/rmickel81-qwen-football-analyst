import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os

def create_heatmap(data_path: str, output_path: str, title: str = "Mapa de Calor Táctico"):
    """
    Genera un mapa de calor de posiciones de jugadores a partir de datos de tracking.
    
    Formato esperado en CSV:
    - columns: minute, player, action, x, y
    - x: 0-100 (del 0% al 100% del campo)
    - y: 0-100 (del 0% al 100% del campo)
    """
    # Cargar datos
    df = pd.read_csv(data_path)
    
    # Validar columnas
    required_cols = {'x', 'y'}
    if not required_cols.issubset(df.columns):
        raise ValueError(f"El CSV debe contener columnas: {required_cols}")
    
    # Crear grilla 20x20 para el heatmap
    x_bins = np.linspace(0, 100, 21)
    y_bins = np.linspace(0, 100, 21)
    
    # Calcular histograma 2D
    heatmap, x_edges, y_edges = np.histogram2d(df['x'], df['y'], bins=[x_bins, y_bins])
    
    # Normalizar para que los valores estén entre 0 y 1
    heatmap = heatmap / heatmap.max() if heatmap.max() > 0 else heatmap
    
    # Crear figura
    plt.figure(figsize=(12, 8))
    
    # Dibujar el campo de fútbol como fondo
    draw_soccer_field(plt.gca())
    
    # Superponer el heatmap
    sns.heatmap(
        heatmap.T, 
        cmap="YlOrRd", 
        alpha=0.7,
        cbar_kws={'label': 'Intensidad de actividad'},
        square=True,
        linewidths=0,
        xticklabels=False,
        yticklabels=False
    )
    
    plt.title(title, fontsize=16, fontweight='bold', pad=20)
    plt.xlim(0, 20)
    plt.ylim(0, 20)
    
    # Guardar
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    
    print(f"✅ Mapa de calor guardado: {output_path}")

def draw_soccer_field(ax):
    """Dibuja un campo de fútbol simplificado como fondo."""
    # Dimensiones normalizadas (0-100 en datos → 0-20 en grilla)
    # Pasto
    ax.add_patch(plt.Rectangle((0, 0), 20, 20, color="#2c6f36", zorder=0))
    
    # Líneas del campo
    ax.plot([0, 20], [10, 10], color='white', linewidth=1)  # Línea central
    ax.add_patch(plt.Circle((10, 10), 2, color='white', fill=False, linewidth=1))  # Círculo central
    
    # Áreas
    ax.add_patch(plt.Rectangle((0, 6), 2, 8, color='white', fill=False, linewidth=1))   # Área pequeña local
    ax.add_patch(plt.Rectangle((18, 6), 2, 8, color='white', fill=False, linewidth=1))  # Área pequeña visitante
    ax.add_patch(plt.Rectangle((0, 3), 4, 14, color='white', fill=False, linewidth=1))  # Área grande local
    ax.add_patch(plt.Rectangle((16, 3), 4, 14, color='white', fill=False, linewidth=1)) # Área grande visitante

if __name__ == "__main__":
    # Ejemplo: generar mapa de calor para posesión ofensiva
    try:
        create_heatmap(
            data_path="data/sample_match_events.csv",
            output_path="reports/figures/heatmap_offensive.png",
            title="Mapa de Calor: Actividad en Campo Rival (Min 0-45)"
        )
    except Exception as e:
        print(f"⚠️ Error al generar mapa de calor: {e}")
        print("💡 Asegúrate de que tu CSV tenga columnas 'x' e 'y' con valores entre 0 y 100.")
