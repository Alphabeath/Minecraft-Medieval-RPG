import os
import sys
from pathlib import Path

def eliminar_archivos_identifier(directorio_raiz):
    """
    Busca y elimina todos los archivos .Identifier en el directorio raíz y sus subcarpetas
    
    Args:
        directorio_raiz: Ruta del directorio donde buscar
        
    Returns:
        int: Cantidad de archivos eliminados
    """
    if not os.path.exists(directorio_raiz):
        print(f"Error: El directorio {directorio_raiz} no existe")
        return 0
        
    contador = 0
    for ruta_actual, _, archivos in os.walk(directorio_raiz):
        for archivo in archivos:
            if archivo.endswith('.Identifier'):
                ruta_completa = os.path.join(ruta_actual, archivo)
                try:
                    os.remove(ruta_completa)
                    print(f"Archivo eliminado exitosamente: {ruta_completa}")
                    contador += 1
                except Exception as e:
                    print(f"Error al eliminar {ruta_completa}: {str(e)}")
    
    return contador

if __name__ == "__main__":
    # Usar el directorio actual si no se proporciona uno como argumento
    if len(sys.argv) > 1:
        directorio_raiz = sys.argv[1]
    else:
        # Cambia esto a la ruta de tu proyecto Minecraft-Medieval
        directorio_raiz = "/home/bryan/Minecraft-Medieval"
    
    print(f"Iniciando búsqueda y eliminación de archivos .Identifier en: {directorio_raiz}")
    
    if not os.path.isdir(directorio_raiz):
        print(f"Error: {directorio_raiz} no es un directorio válido")
        sys.exit(1)
    
    total_eliminados = eliminar_archivos_identifier(directorio_raiz)
    print(f"Proceso completado. Se eliminaron {total_eliminados} archivos .Identifier")