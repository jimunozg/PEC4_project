# LIBRERÍAS
import pandas as pd


# FUNCIONES
def ex5(data: pd.DataFrame):
    '''
    Resolución del ejercicio 3.5, en el que se pide:
    - Ciclistas pertenecientes a la UCSC.
    - Ciclista de la UCSC que ha hecho el mejor tiempo.
    - Posición sobre el total en que ha quedado ese ciclista.
    - Porcentaje sobre el total que representa ese ciclista.

    Entrada:
    - data: DataFrame actualizado en los ejercicios anteriores.

    Salida:
    - Imprime los resultados de las cueestiones pedidas.
    - No devuelve ningún argumento.
    '''
    # Nombre del ejercicio:
    print("\n--- Ejercicio 5: Análisis del club UCSC ---")

    # Filtramos los ciclistas del club UCSC:
    ucsc_data = data[data['club_clean'] == 'UCSC']
    
    if ucsc_data.empty:
        print("No se encontraron ciclistas del club UCSC.\n")
        return None
    
    # Buscamos al ciclista con el mejor tiempo:
    ucsc_data = ucsc_data.copy()
    ucsc_data['time_seconds'] = ucsc_data['time'].apply( lambda x: sum( int(t) * 60 ** i for i, t in enumerate( reversed( x.split(":") ) ) ) )
    best_cyclist = ucsc_data.loc[ucsc_data['time_seconds'].idxmin()]

    # Calculamos la posición y el porcentaje sobre el total:
    data['time_seconds'] = data['time'].apply(lambda x: sum(int(t) * 60 ** i for i, t in enumerate(reversed(x.split(":")))))
    sorted_data = data.sort_values(by='time_seconds').reset_index(drop=True)
    best_position = sorted_data.index[sorted_data['time_seconds'] == best_cyclist['time_seconds']][0] + 1
    total_cyclists = len(data)
    percentage = (best_position / total_cyclists) * 100


    # Imprimimos los resultados:
    print(f"Ciclistas del club UCSC: \n{ucsc_data[['time', 'club_clean']]}\n")
    print(f"Mejor ciclista del club UCSC: \n{best_cyclist}\n")
    print(f"Posición del mejor ciclista: {best_position}\n")
    print(f"Porcentaje sobre el total: {percentage:.2f}%\n")



    

