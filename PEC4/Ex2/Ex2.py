# LIBRERÍAS
import pandas as pd
from faker import Faker


# FUNCIONES
def name_surname(data: pd.DataFrame):
    '''
    Función que anonimiza los nombres de los ciclistas. 
    Para ello busca en la columna 'biker' utilizando Faker.
    
    Entrada:
    - DataFrame con una columna llamada 'biker'.
    
    Salida:
    - DataFrame con la columna 'biker' actualizada con nombres anonimizados.
    '''
    # Crear una instancia de Faker:
    fake = Faker()
    
    # Modificar la columna 'biker' con nombres anonimizados:
    data['biker'] = [ f"{fake.first_name()} {fake.last_name()}" for i in range( len(data) ) ]
        # len(data) obtiene el número total de filas en el DataFrame.
        # Para cada fila en el DataFrame, se generan nombres y apellidos, usando fake.
        # El resultado de la lista generada se asigna a la columna 'biker' del DataFrame. 
        # Si la columna 'biker' ya existe, sobrescribe los valores anteriores con los nuevos nombres aleatorios. 
    
    # Devolvemos el DataFrame modificado
    return data


def NAN_delete(data: pd.DataFrame):
    '''
    Función que elimina a los ciclistas que no participaron en la prueba.
    Para ello busca a los que no tienen un tiempo de 00:00:00 en la prueba, 
    hace una lista y sobreescribe el DataFrame sin los que no participaron.

    Entrada: 
    - DataFrame anonimizado.

    Salida: 
    - DataFrame anonimizado con los participantes reales.
    '''
    # Eliminar los ciclistas que no han participado:
    data = data[data['time'] != '00:00:00']
        # data['time'] != '00:00:00' crea una máscara booleana.
        # Sólo las filas donde la condición es TRUE se conserva, es decir, se eliminan las que sean iguales a la condición.
    
    # Devolvemos el DataFrame resultante:
    return data


def number_data(data: pd.DataFrame, dorsal: int):
    '''
    Función que devuelve los datos correspondientes a un dorsal concreto.
    Si no existe el dorsal o hay problemas con el DataFrame devuelve un error.

    Entradas:
    - data: DataFrame con los datos de la prueba.
    - dorsal: entero que identifica el dorsal del que queremos obtener los datos.

    Salida:
    - data_number: datos correspondientes al dorsal especificado.
    '''
    try:
        # Filtrar el DataFrame para obtener el ciclista con el dorsal dado:
        data_number = data[data['dorsal'] == dorsal]
        
        # Devolvemos el DataFrame resultante o un error:
        if not data_number.empty: 
            return data_number
        else:
            raise ValueError(f"\n\tNo se encontró un ciclista con el dorsal {dorsal}.")
    
    # Errores en el DataFrame:
    except Exception as e:
        return f"Error: {e}"


def ex2(data: pd.DataFrame):
    '''
    Resolución del ejercicio 3.2, en el que se pide:
    - Anonimización de los datos.
    - Eliminación de datos.
    - Consulta de datos.

    Entrada:
    - Recibe un dataset con el que trabajar.

    Salida: 
    - Datos anonimizados.
    - Eliminar a los ciclistas que no participaron.
    - Número de ciclistas en el dataframe.
    - Recuperar los datos del ciclista con dorsal 1000.
    '''
    # Nombre del ejercicio:
    print("\n--- Ejercicio 2: Anonimización y limpieza del dataset ---")

    # Anonimización de datos:
    data = name_surname(data)
    
    print("\nDatos anonimizados (primeros 5 registros): \n", data.head())

    # Eliminación de los ciclistas que no han participado:
    data = NAN_delete(data)

    print(f"\n* Total de ciclistas que realmente participaron: {len(data)}")
    print("\n* Datos de los 5 primeros ciclistas que participaron realmente: \n", data.head())

    # Datos del ciclista con dorsal 1000:
    dorsal = 1000
    data_dorsal = number_data(data, dorsal)

    print(f"\n* Los datos asociados al ciclista con el dorsal {dorsal} son: \n", data_dorsal)

    # Devolvemos el DataFrame actualizado:
    return data
