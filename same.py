import re

with open(r'C:\Users\JFROJAS\Desktop\CarlosPDF\project\PDF\contenido.txt', 'r', encoding='utf-8') as f:
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

#lOTE
regEx_lote = r'EA\s+(\w+)'
match_lote = re.search(regEx_lote, text)

if match_lote:
    lote = match_lote.group(1)

lote = lote.replace(cantidad, "")

"""
print("Lote: " + lote)
print("Clave:" + clave)
print("Descripcion:" +descripcion)
print("Cantidad:" +cantidad)
#####ClIENTE########
print("")
print("No. Cliente: " + matches_noCliente)
print("Nombre del cliente: " + nombreCliente)
print("Ciudad del cliente: " + ciudad_cliente)
print("Zip Code del cliente: " + zipcodeCliente)
print("Colonia del cliente: " + colCliente)
print("Direccion del cliente: " + direccionCliente)

#####CONSIGNATARIO########
print("")
print("Nombre del consignatario: " + consignatario)
print("Ciudad del consignatario: " + ciudad_consig)
print("Zip Code del consignatario: " + zipcodeConsig)
print("Colonia del consignatario: " + colConsig)
print("Direccion del consignatario: " + direccionConsig)
"""

