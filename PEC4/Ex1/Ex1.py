# LIBRERÍAS
import pandas as pd


# FUNCIONES
def ex1():
    '''
    Resolución del ejercicio 3.1, en el que se pide:
    - Importación del dataset.
    - Análisis exploratorio de datos (EDA).
        
    Salida:
    - Primeras 5 filas del dataset.
    - Columnas del dataset.
    - Número total de ciclistas.
    - Tamaño del dataset (número total de elementos).
   
    Además, devuelve el dataset para usarlo posteriormente.
    '''
    # Nombre del ejercicio:
    print("\n--- Ejercicio 1: Importación y análisis inicial del dataset ---")

    # Rutas relativas:
    nombre = 'dataset.csv'
    ruta = './data/' + nombre

    # Carga de los datos:
    try:
        data = pd.read_csv(ruta, sep = ';')
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo en la ruta {ruta}")
        return None

    # Mostramos el EDA:
    print("\n* Primeras 5 filas del dataset: \n", data.head())
    print("\n* Columnas: \t", data.columns.to_list())
    print("\n* Número de ciclistas que participaron en la prueba: \t", data.shape[0])
    print("\n* Tamaño total del dataset: \t", data.size)

    # Devolvemos el dataset para su posterior manejo:
    return data

