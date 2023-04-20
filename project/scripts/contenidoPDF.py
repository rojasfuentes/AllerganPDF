import os
import PyPDF2

# Directorio de los archivos PDF
directorio_pdf = r'C:\Users\JFROJAS\Desktop\CarlosPDF\project\PDF'

# Obtener lista de archivos PDF en el directorio
archivos_pdf = [f for f in os.listdir(directorio_pdf) if f.endswith('.pdf')]

# Recorrer cada archivo PDF y extraer el texto
for archivo_pdf in archivos_pdf:
    # Crear un objeto de lectura de PDF
    pdf_reader = PyPDF2.PdfReader(os.path.join(directorio_pdf, archivo_pdf))
    
    # Extraer el texto del PDF
    texto = ''
    for page in pdf_reader.pages:
        texto += page.extract_text()
    
    # Crear un archivo contenido.txt con el mismo nombre que el archivo PDF
    archivo_txt = archivo_pdf.replace('.pdf', '_contenido.txt')
    ruta_archivo_txt = os.path.join(directorio_pdf, archivo_txt)
    
    # Guardar el texto extraído en el archivo contenido.txt
    with open(ruta_archivo_txt, 'w', encoding='utf-8') as f:
        f.write(texto)
    
    print(f'Se ha guardado el texto del archivo PDF {archivo_pdf} en {ruta_archivo_txt}')
