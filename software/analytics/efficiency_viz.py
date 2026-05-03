import pandas as pd

def generate_performance_report(file_path):
    df = pd.read_csv(file_path)
    
    avg_trad = df['Metodo_Tradicional_min'].mean()
    avg_ser = df['Sistema_SER_01_min'].mean()
    total_ahorro = df['Ahorro_Tiempo_min'].sum()
    
    print("--- REPORTE DE IMPACTO 888=SER ---")
    print(f"Tiempo Promedio Tradicional: {avg_trad:.2f} min")
    print(f"Tiempo Promedio SER-01: {avg_ser:.2f} min")
    print(f"Mejora de Eficiencia: {((avg_trad - avg_ser)/avg_trad)*100:.2f}%")
    print(f"Tiempo Total Recuperado en 100 Operaciones: {total_ahorro:.2f} min")
    print("-----------------------------------")

# Ejecución de análisis
generate_performance_report('data/efficiency_log.csv')
