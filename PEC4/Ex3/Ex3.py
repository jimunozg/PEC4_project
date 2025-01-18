# LIBRERÍAS
import pandas as pd
import os
import matplotlib.pyplot as plt


# FUNCIONES
def minutes_002040(time: str):
    """
    Trunca el tiempo dado en formato hh:mm:ss a múltiplos de 20 minutos.
    De forma que los ciclistas queden agrupados en franjas de 20 minutos.
    
    Funciones usadas:
    - split():
        Divide la cadena time en partes, utilizando ":" como separador.

    - map(int, ...):
        Aplica la función int a cada elemento de la lista resultante de split(":").
        Convierte cada parte de la cadena (por ejemplo, '06', '19', '40') en números enteros.
    
    Entrada:
    - hh:mm:ss.

    Salida:
    - hh':mm'.
    """
    try:
        # Convertir el tiempo a horas, minutos y segundos:
        hh, mm, ss = map(int, time.split(":"))
        
        # Truncar los minutos al múltiplo de 20 más cercano
        if mm < 20:
            mm = 0
        elif mm < 40:
            mm = 20
        else:
            mm = 40
        
        # Devolver el resultado:
        return f'{hh:02}:{mm:02}'
        
    except:
        return None  # Manejar valores erróneos o NaN


def img_hist(data: pd.DataFrame, x_column: str, y_column: str, output_path: str, name: str, title: str, xlabel: str, ylabel: str):
    '''
    Genera y guarda un histograma en función de los parámetros proporcionados.

    Entrada:
    - data: DataFrame con los datos a graficar.
    - x_column: nombre de la columna para el eje X.
    - y_column: nombre de la columna para el eje Y.
    - output_path: ruta relativa donde se guardará la imagen del histograma.
    - name: nombre del archivo con su extensión.
    - title: título del histograma.
    - xlabel: etiqueta para el eje X.
    - ylabel: etiqueta para el eje Y.

    Salida:
    - No devuelve argumentos.
    - Imagen del histograma y su ruta.
    '''
    # Crear la carpeta si no existe
    os.makedirs(output_path, exist_ok = True)
    
    # Generar el gráfico
    plt.figure(figsize = (10, 6))
    plt.bar(data[x_column], data[y_column], width = 0.5, align = 'center')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xticks(rotation = 45)
    plt.tight_layout()
    
    # Guardar el histograma
    full_path = os.path.join(output_path, name)
    plt.savefig(full_path)
    plt.close()
    
    print(f"\nHistograma guardado en: {full_path}.\n")


def ex3(data: pd.DataFrame):
    '''
    Resolución del ejercicio 3.3, en el que se pide:
    - Agrupación de tiempos en franjas de 20 minutos.
    - Generación de un histograma.

    Entrada:
    - DataFrame anonimizado.

    Salida:
    - data: DataFrame actualizado.
    - data_grouped: DataFrame con una columna nueva que agrupa por franja de tiempo.
    - Histograma almacenado en una imagen.
    '''
    # Nombre del ejercicio:
    print("\n--- Ejercicio 3: Agrupamiento de tiempos y generación del histograma ---")

    # Filtrado de datos válidos, aplicando el agrupamiento:
    data['time_grouped'] = data['time'].apply(minutes_002040)

    # Eliminar valores nulos:
    data = data.dropna(subset = ['time_grouped'])

    print(data)

    # Agrupamiento por franjas temporales:
    data_grouped = data.groupby('time_grouped').size().reset_index(name = 'count')
        # data.groupby('time_grouped'):
            # Agrupa los datos en función de los valores únicos de la columna 'time_grouped'.
            # Cada grupo contiene todas las filas que tienen el mismo valor en 'time_grouped'.
        # .size():
            # Cuenta el número de filas en cada grupo.
            # Devuelve una serie con los índices como los valores de 'time_grouped', 
            # y los valores como el número de ocurrencias (frecuencias) de cada grupo.
        # .reset_index(name='count'):
            # Convierte la Serie resultante en un DataFrame.
            # El índice (valores únicos de 'time_grouped') se convierte en una columna normal.
            # La columna resultante del conteo se nombra 'count'.
    
    print("\n* Datos agrupados: \n", data_grouped)

    # Rutas relativas:
    img_path = './img/'
    name = 'histograma.png'
    
    # Generar histograma en la carpeta de imágenes:
    hist = img_hist(data = data_grouped, 
                    x_column = 'time_grouped',
                    y_column = 'count',
                    output_path = img_path,
                    name = name,
                    title = "Distribución de ciclistas en franjas de 20 minutos",
                    xlabel = "Tiempos agrupados (hh:mm)",
                    ylabel = "Número de ciclistas"
                    )
    
    # Devolver el DataFrame actualizado y el generado:
    return data, data_grouped
