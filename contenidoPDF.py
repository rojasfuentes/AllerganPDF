import PyPDF2

# Abrir el archivo PDF
with open(r'C:\Users\JFROJAS\Desktop\CarlosPDF\510793162.pdf', 'rb') as pdf_file:
    # Crear un objeto PDFReader para leer el archivo PDF
    pdf_reader = PyPDF2.PdfReader(pdf_file)

    # Crear un objeto para escribir el contenido extraído en un archivo de texto
    with open(r'C:\Users\JFROJAS\Desktop\CarlosPDF\contenido.txt', 'w', encoding='utf-8') as text_file:
        # Iterar sobre todas las páginas del PDF
        for page_num in range(len(pdf_reader.pages)):
            # Obtener la página actual
            page = pdf_reader.pages[page_num]

            # Extraer el texto de la página actual
            page_text = page.extract_text()

            # Escribir el texto extraído en el archivo de texto
            text_file.write(page_text)
