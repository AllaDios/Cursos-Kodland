from transformers import pipeline

def summarization(text, num_sentences):
    # Inicializar el pipeline de resumen
    summarizer = pipeline("summarization")
    
    # Generar el resumen
    summary = summarizer(text, max_length=num_sentences * 30, min_length=10, do_sample=False)
    
    # Extraer el texto resumido
    summarized_text = summary[0]['summary_text']
    
    return summarized_text

# Ejemplo de uso
texto_ejemplo = """La inteligencia artificial (IA) es la simulación de procesos de inteligencia humana por parte de máquinas, especialmente sistemas informáticos. Estos procesos incluyen el aprendizaje (la adquisición de información y reglas para el uso de la información), el razonamiento (usando las reglas para llegar a conclusiones aproximadas o definitivas) y la autocorrección. Las aplicaciones particulares de la IA incluyen sistemas expertos, procesamiento del lenguaje natural, reconocimiento del habla y visión artificial."""

# Obtener un resumen de 2 frases
resumen = summarization(texto_ejemplo, 2)
print("Resumen:", resumen)