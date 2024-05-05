import os 
import getpass
from colorama import Fore

nombre_usuario=getpass.getuser()

print(Fore.CYAN+f"Usted es el Usuario: {nombre_usuario}")

directorio='C:\\Users\\'+nombre_usuario+'\\Downloads'
# Obtener la lista de archivos en el directorio
archivos_en_directorio = os.listdir(directorio)

def borrar():
# Iterar sobre los archivos en el directorio y eliminarlos uno por uno
    for archivo in archivos_en_directorio:
        # Formar la ruta completa de cada archivo
        ruta_archivo = os.path.join(directorio, archivo)
        # Verificar si el elemento es un archivo
        if os.path.isfile(ruta_archivo):
            # Eliminar el archivo
            os.remove(ruta_archivo)

opcion=input(Fore.CYAN+"¿Esta seguro de borrar la carpeta de Descargas por completo? SI/NO :")

if opcion=='SI'or 'si':
    borrar()
    print(Fore.WHITE+"Carpeta Vaciada")
else:
    exit


