# LIBRERÍAS
import pandas as pd
import re


# FUNCIONES
def clean_club(club_name: str):
    '''
    Función que impia los nombres de los clubes según las reglas especificadas en el enunciado.
    Si después de limpiarlos el nombre del club está vacío devuelve "INDEPENDIENTE".
    
    Entrada:
    - club_name: nombre original del club (cadena de texto).
    
    Salida:
    - club_name: nombre limpio del club.
    '''
    if not isinstance(club_name, str):
        # isinstance(club_name, str):
            # Comprueba si el valor de club_name es una instancia del tipo str,
            # es decir, si es una cadena de texto.
        
        # not isinstance(...):
            # Evalúa si el valor no es del tipo str.
        return "INDEPENDIENTE"
            # Si el valor de club_name no es una cadena, se considera inválido o faltante,
            # por lo que la función asigna el valor "INDEPENDIENTE" como predeterminado.
            # Útil para manejar valores como None, números, o cualquier tipo no esperado.

    # Convertir a mayúsculas:
    club_name = club_name.upper()

     # Reemplazar términos comunes por nada (cuando están en el inicio):
    club_name = re.sub(r"(PEÑA CICLISTA|PENYA CICLISTA|AGRUPACIÓN CICLISTA|AGRUPACION CICLISTA|AGRUPACIÓ CICLISTA|AGRUPACIO CICLISTA|CLUB CICLISTA|CLUB)",
                        "", club_name)
                # Se usa or (|) para que si se encuentra uno de ellos lo elimine,
                # en vez de usar funciones independientes.

    # Eliminar prefijos comunes con expresión regular (al principio):
    club_name = re.sub(r"^(C\.C\.|C\.C|CC|C\.D\.|C\.D|CD|A\.C\.|A\.C|AC|A\.D\.|A\.D|AD|A\.E\.|A\.E|AE|E\.C\.|E\.C|EC|S\.C\.|S\.C|SC|S\.D\.|S\.D|SD)\s*",
                        "", club_name)
                # Análogo al anterior, pero con 2 diferencias:
                # El uso del carácter ^ asegura que solo se eliminen estos términos sólo si están al comienzo.
                # En la expresión regular, C\.C\. se escribe así porque el punto (.) es un carácter especial en las expresiones regulares. 
                # Por defecto, el punto significa "cualquier carácter". 
                # Para buscar específicamente un punto literal, debes escaparlo con una barra invertida (\).

    # Eliminar sufijos comunes (al final):
    club_name = re.sub(r"(T\.T\.|T\.T|TT|T\.E\.|T\.E|TE|C\.C\.|C\.C|CC|C\.D\.|C\.D|CD|A\.D\.|A\.D|AD|A\.C\.|A\.C|AC)$",
                        "", club_name)
                # El uso del carácter $ asegura que solo se eliminen estos términos si están al final.

    # Eliminar espacios en blanco extra:
    club_name = club_name.strip()
                # .strip():
                # Elimina cualquier espacio en blanco al inicio o al final del nombre del club.
    
    # Devolvemos el nombre del club limpio:
    if club_name:
        return club_name
    else:
        return "INDEPENDIENTE"
                # Si el nombre está vacío, retorna "INDEPENDIENTE".


def ex4(data: pd.DataFrame):
    '''
    Resolución del ejercicio 3.4, en el que se pide:
    - Limpiar los nombres de los clubes ciclistas.
    - Añadir una nueva columna club_clean con los nombres limpios.
    - Calcular el número de ciclistas por club.
    - Devolver un DataFrame con los ordenado de mayor a menor número de ciclistas en cada club.
    
    Entrada:
    - data: DataFrame con la columna 'club' que contiene los nombres originales de los clubes.
    
    Salida:
    - data: DataFrame actualizado.
    - clubs_grouped: DataFrame agrupado y ordenado con la cantidad de ciclistas por club limpio.
    '''
    # Nombre del ejercicio:
    print("\n--- Ejercicio 4: Limpieza de nombres de clubes ciclistas ---")

    # Si el DataFrame no contiene la columna 'club':
    if "club" not in data.columns:
        raise KeyError("\nEl DataFrame no contiene la columna 'club'.\n")

    # Creamos una nueva columna con los nombres limpios:
    data['club_clean'] = data['club'].apply(clean_club)
                # Uso análogo al utilizado en otros ejercicios.

    # Mostramos los 15 primeros valores:
    print(data.head(15))

    # Agrupar por los clubes limpios y contar los ciclistas en cada club:
    clubs_grouped = data.groupby('club_clean').size().reset_index(name = 'count')
                # Uso análogo al utilizado en otros ejercicios.

    # Ordenar por la cantidad de ciclistas (descendente):
    clubs_grouped = clubs_grouped.sort_values(by = 'count', ascending = False)

    print(clubs_grouped.head())

    # Devolvemos el DataFrame actualizado y el creado:
    return data, clubs_grouped

