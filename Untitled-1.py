def print():
    numero = int(input("Ingresa un numero del 1 al 10: "))
    if numero < 1 or numero > 10:
        print("el numero tiene que estar entre 1 y 10")
        return
    archivo = f"tabla_{numero}.txt"
    with open(archivo, "w") as f:
        for i in range(1, 11):
            f.write(f"{numero} por {i} es {numero * i}\n")
    print(f"La tabla se guardo en el archivo {archivo}.")

print()



def print():
    n = int(input("Numero de la tabla: "))
    archivo = f"tabla_{n}.txt"
    try:
        with open(archivo, "r") as f:
            contenido = f.read()
        print("Tabla:\n" + contenido)
    except FileNotFoundError:
        print(f"No existe el archivo {archivo}")

print()



def print():
    n = int(input("Ingresa el numero de la tabla: "))
    linea = int(input("Ingresa la linea para ver: "))
    archivo = f"tabla_{n}.txt"
    try:
        with open(archivo, "r") as f:
            filas = f.readlines()
        if 1 <= linea <= 10:
            print("Linea: " + filas[linea - 1].strip())
        else:
            print("La linea no esta en el rango")
    except FileNotFoundError:
        print("El archivo no existe")

print()



import urllib.request

def print():
    url = input("Ingresa la URL: ")
    try:
        respuesta = urllib.request.urlopen(url)
        texto = respuesta.read().decode("utf-8")
        cantidad = len(texto.split())
        print(f"el texto tiene {cantidad} palabras")
    except Exception as e:
        print("No se puede conectar a la URL")

print()



import urllib.request

def print():
    url = "https://ec.europa.eu/eurostat/estat-navtree-portlet-prod/BulkDownloadListing?file=data/sdg_08_10.tsv.gz&unzip=true"
    try:
        datos = urllib.request.urlopen(url).read().decode("utf-8")
        codigo = input("Ingresa las iniciales del pais: ")
        encontrado = False
        for fila in datos.splitlines():
            if fila.startswith(codigo):
                print("Datos del pais:")
                print(fila)
                encontrado = True
                break
        if not encontrado:
            print("No hay datos con esa inicial")
    except Exception as e:
        print("No se puede obtener la informacion")

print()



import csv

def print():
    archivo = input("Ingresa el nombre del archivo CSV: ")
    try:
        datos = {}
        with open(archivo, "r", encoding='utf-8') as f:
            lector = csv.DictReader(f, delimiter=';')
            for campo in lector.fieldnames:
                datos[campo] = []
            for fila in lector:
                for campo in lector.fieldnames:
                    datos[campo].append(fila[campo])

        with open("resumen.csv", "w", encoding='utf-8', newline='') as f_out:
            escritor = csv.writer(f_out)
            escritor.writerow(["Columna", "Mínimo", "Máximo", "Promedio"])
            for columna in datos:
                if columna.lower() == "nombre":
                    continue
                lista = [float(x.replace(",", ".")) for x in datos[columna]]
                escritor.writerow([columna, min(lista), max(lista), sum(lista)/len(lista)])
        print("el resumen de cotizaciones se guardo en resumen.csv")
    except Exception as e:
        print("No se puede leer el archivo")

print()
