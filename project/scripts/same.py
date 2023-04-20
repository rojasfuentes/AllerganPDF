import os
import re

# Listas para almacenar los resultados
matches_noCliente_list = []
nombreCliente_list = []
direccionCliente_list = []
colCliente_list = []
zipcodeCliente_list = []
ciudad_cliente_list = []

consignatario_list = []
direccionConsig_list = []
colConsig_list = []
ciudad_consig_list = []
zipcodeConsig_list = []

clave_list = []
descripcion_list = []
cantidad_list = []
lote_list = []

# Ruta de la carpeta PDF
carpeta_pdf = r'C:\Users\JFROJAS\Desktop\CarlosPDF\project\PDF'

# Obtener la lista de archivos .txt en la carpeta PDF
archivos_txt = [archivo for archivo in os.listdir(carpeta_pdf) if archivo.endswith('.txt')]

# Lista para almacenar los resultados de cada archivo
resultados = []

# Ciclo para procesar cada archivo .txt
for archivo in archivos_txt:
    # Ruta completa del archivo
    ruta_archivo = os.path.join(carpeta_pdf, archivo)
    
    with open(ruta_archivo, 'r', encoding='utf-8') as f:
        text = f.read()

        #Datos del cliente
        #No. Cliente
        regEx_noCliente = r'\b\d{8}\b'
        matches_noCliente = re.findall(regEx_noCliente, text)
        matches_noCliente = matches_noCliente[0]

        #Ciudad del cliente
        regEx_ciudadCliente = r'(\w+?)Número'
        match_ciudadCliente = re.search(regEx_ciudadCliente, text)


        if match_ciudadCliente:
            #Ciudad
            ciudad_cliente = match_ciudadCliente.group(1)
            # Zip Code
            index_ciudad_cliente = match_ciudadCliente.start(1)
            palabras = text[:index_ciudad_cliente].split()
            zipcodeCliente = palabras[-1] if len(palabras) > 0 else None

            # Colonia
            index_zipcode_cliente = text.index(zipcodeCliente)
            palabras_antes_zipcode = text[:index_zipcode_cliente].split()
            colCliente = palabras_antes_zipcode[-1] if len(palabras_antes_zipcode) > 0 else None


        #Consigantario
        #Ciudad consignatario
        regEx_ciudadConsig = r'(\w+?)Cliente'
        match_ciudadConsig = re.search(regEx_ciudadConsig, text)


        if match_ciudadConsig:
            ciudad_consig =  match_ciudadConsig.group(1)
            # Zip Code
            index_ciudad_consig = match_ciudadConsig.start(1)
            palabras = text[:index_ciudad_consig].split()
            zipcodeConsig = palabras[-1] if len(palabras) > 0 else None

            # Colonia
            index_zipcode_cliente = text.index(zipcodeConsig)
            palabras_antes_zipcode = text[:index_zipcode_cliente].split()
            colConsig = palabras_antes_zipcode[-1] if len(palabras_antes_zipcode) > 0 else None

            # Dirección
            lineas = text.split('\n')
            for i, linea in enumerate(lineas):
                if colConsig in linea:
                    direccionConsig = linea.split(colConsig)[0].split()
                    direccionConsig = ' '.join(direccionConsig)  # Une las palabras anteriores en una cadena de texto
                    break
        else:
            ciudad_consig = None
            zipcodeConsig = None
            ciudadConsig = None
            direccionConsig = None


        #Arreglando variables dinamicas
        buscarCliente = ciudad_cliente + "Cliente"
        buscarDireccionCliente = ciudad_cliente + "Número"

        #este pedazo de codigo es para obtener el nombre del cliente
        next_line = None
        lines = text.split('\n')
        for i, line in enumerate(lines):
            if 'Consignatario' in line:
                consignatario = lines[i + 1] if i + 1 < len(lines) else None
                break
            
        # Nombre del cliente
        index_cliente = text.split().index(buscarCliente)
        nombreCliente = text.split()[index_cliente + 1:index_cliente + 5]
        for i, palabra in enumerate(nombreCliente):
            if palabra in nombreCliente:
                nombreCliente = ' '.join(nombreCliente)  # Une las palabras anteriores en una cadena de texto
                break
            
        linea_cliente = None
        for i, line in enumerate(lines):
            if buscarDireccionCliente in line:
                linea_cliente = line
                break
        resultado = re.sub(r'(\d+).*', r'\1', linea_cliente)
        direccionCliente = resultado.replace(nombreCliente, "")



        ########Info 
        info = text.find("Lote")
        next_info = text.find("\n", info) + 1

        # Obtener el renglón siguiente al renglón donde se encuentra la palabra "Lote"
        #Descipcion
        next_info = (text[next_info:text.find("\n", next_info)] ).split()  #.split() separa las palabras en una lista
        clave = next_info[1]
        descripcion = next_info[2:len(next_info)]
        descripcion = ' '.join(descripcion)  # Une las palabras anteriores en una cadena de texto

        #Cantidad
        regEx_cantidad1 = r'(\w+?)EA'
        regEx_cantidad2 = r"(\S+) EA"
        regEx_cantidad = regEx_cantidad1 if re.search(regEx_cantidad1, text) else regEx_cantidad2
        cantidad = re.search(regEx_cantidad, text)
        cantidad = cantidad.group(1)

        # buscar todas las ocurrencias de "EA"
        ocurrencias_EA = [m.start() for m in re.finditer('EA', text)]

        for ocurrencia in ocurrencias_EA:
            # obtener la línea en la que se encuentra la ocurrencia de "EA"
            start_line = text.rfind('\n', 0, ocurrencia) + 1
            end_line = text.find('\n', ocurrencia)
            if end_line == -1:
                end_line = len(text)
            line = text[start_line:end_line]

            # dividir la línea en palabras
            palabras = line.split()

            # obtener el último elemento de la línea (que sería el lote)
            lote = palabras[-1]
        
    """
        # Añadir los resultados a la lista
    resultados.append({
        'nombre_archivo': archivo,
        'matches_noCliente': matches_noCliente,
        'ciudad_cliente': ciudad_cliente,
        'zipcodeCliente': zipcodeCliente,
        'colCliente': colCliente,
        'ciudad_consig': ciudad_consig,
        'zipcodeConsig': zipcodeConsig,
        'colConsig': colConsig,
        'direccionConsig': direccionConsig,
        'nombreCliente': nombreCliente,
        'direccionCliente': direccionCliente,
        'clave': clave,
        'descripcion': descripcion,
        'cantidad': cantidad,
        'lote': lote
    })
    """
    matches_noCliente_list.append(matches_noCliente)
    nombreCliente_list.append(nombreCliente)
    direccionCliente_list.append(direccionCliente)
    colCliente_list.append(colCliente)
    zipcodeCliente_list.append(zipcodeCliente)
    ciudad_cliente_list.append(ciudad_cliente)
    consignatario_list.append(consignatario)
    direccionConsig_list.append(direccionConsig)
    colConsig_list.append(colConsig)
    ciudad_consig_list.append(ciudad_consig)
    zipcodeConsig_list.append(zipcodeConsig)
    clave_list.append(clave)
    descripcion_list.append(descripcion)
    cantidad_list.append(cantidad)
    lote_list.append(lote)

# Imprimir las listas
"""
print(matches_noCliente_list)
print(nombreCliente_list)
print(direccionCliente_list)
print(colCliente_list)
print(zipcodeCliente_list)
print(ciudad_cliente_list)
print(consignatario_list)
print(direccionConsig_list)
print(colConsig_list)
print(ciudad_consig_list)
print(zipcodeConsig_list)
print(clave_list)
print(descripcion_list)
print(cantidad_list)
print(lote_list)
"""

"""
# Imprimir los resultados
for resultado in resultados:
    print('Archivo:', resultado['nombre_archivo'])
    print('No. Cliente:', resultado['matches_noCliente'])
    print('Ciudad Cliente:', resultado['ciudad_cliente'])
    print('Zip Code Cliente:', resultado['zipcodeCliente'])
    print('Colonia Cliente:', resultado['colCliente'])
    print('Ciudad Consignatario:', resultado['ciudad_consig'])
    print('Zip Code Consignatario:', resultado['zipcodeConsig'])
    print('Colonia Consignatario:', resultado['colConsig'])
    print('Dirección Consignatario:', resultado['direccionConsig'])
    print('Nombre Cliente:', resultado['nombreCliente'])
    print('Dirección Cliente:', resultado['direccionCliente'])
    print('Clave:', resultado['clave'])
    print('Descripción:', resultado['descripcion'])
    print('Cantidad:', resultado['cantidad'])
    print('Lote:', resultado['lote'])
    print('---')
"""