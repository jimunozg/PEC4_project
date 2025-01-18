# LIBRERÍAS

    # EXTERNAS
from PIL import Image

    # MÓDULOS
from PEC4.Ex1.Ex1 import ex1
from PEC4.Ex2.Ex2 import ex2
from PEC4.Ex3.Ex3 import ex3
from PEC4.Ex4.Ex4 import ex4
from PEC4.Ex5.Ex5 import ex5


# FUNCIONESS
def main_all():
    """
    Función que ejecuta todos los ejercicios en orden:
    - No recibe nada ni devuelve nada.
    """

    # Ejercicio 1:
    data = ex1()
    if data is None:
        print("Error: No se pudo importar el dataset. Revisa la ruta.")
        return
    
    # Ejercicio 2:
    data = ex2(data)
    data_cleaned = True

    # Ejercicio 3:
    data, data_group = ex3(data)

    try:
        hist = Image.open(img_path)         # abrir histograma
        hist.show()                         # mostrar el histograma
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo de imagen en la ruta {img_path}.")
    except Exception as e:
        print(f"Ocurrió un error al abrir la imagen: {e}")
    
    # Ejercicio 4:
    data, clubs_grouped = ex4(data)
    
    # Ejercicio 5:
    ex5(data)


def main():
    '''
    Función principal del programa. 
    Responde a las cuestiones planteadas en la PEC 4 s.
    Permite al usuario elegir qué ejercicio quiere ver resuelto,
    siempre y cuando este no pida el ejercicio "x" sin haber realizado "x-1",
    salvo en casos especiales, como:
    - Está el ejercicio 2 hecho, pero no el 3. Esto no influye en la realización del ejercicio 4.
    
    Opciones disponibles:
    - Ex1.
    - Ex2.
    - Ex3.
    - Ex4.
    - Ex5.
    - Todos los ejercicios.
    - Ningún ejercicio (fin del programa).
    '''
    # Variables a utilizar:
    global data, data_cleaned, data_group, clubs_grouped, img_path
    
    # Inicialización de variables:
    data_cleaned = False                                # Estado de anonimización
    data, data_group, clubs_grouped = None, None, None  # DataFrames
    img_path = './img/histograma.png'                   # ruta al archivo


    # Bucle del programa:
    while True:
        try:
            opcion = int(input("\nIntroduce el número de tu elección: "))
        except ValueError:
            print("Por favor, introduce un número válido.")
            continue

        # Ejercicio 1:
        if opcion == 1:
            print("\n--- Ejercicio 1: Importación y análisis inicial del dataset ---")
            data = ex1()
            if data is not None:
                print("Ejercicio 1 completado correctamente.")
            else:
                print("Error: No se pudo importar el dataset. Revisa la ruta.")
        
        # Ejercicio 2:
        elif opcion == 2:
            if data is None:
                print("Por favor, ejecuta primero el ejercicio 1.")
            else:
                print("\n--- Ejercicio 2: Anonimización y limpieza del dataset ---")
                data = ex2(data)
                data_cleaned = True
                print("Ejercicio 2 completado correctamente.")

        # Ejercicio 3:
        elif opcion == 3:
            if data_cleaned == False:
                print("Por favor, ejecuta primero el ejercicio 2.")
            else:
                print("\n--- Ejercicio 3: Agrupamiento de tiempos y generación del histograma ---")
                data, data_group = ex3(data)

                try:
                    hist = Image.open(img_path)         # abrir histograma
                    hist.show()                         # mostrar el histograma
                    print("Ejercicio 3 completado correctamente.")

                except FileNotFoundError:
                    print(f"Error: No se encontró el archivo de imagen en la ruta {img_path}.")
                except Exception as e:
                    print(f"Ocurrió un error al abrir la imagen: {e}")

        # Ejercicio 4:
        elif opcion == 4:
            if not data_cleaned:
                print("Por favor, ejecuta primero el ejercicio 2.")
            else:
                data, clubs_grouped = ex4(data)
                print("Ejercicio 4 completado correctamente.")

        # Ejercicio 5:
        elif opcion == 5:
            if not data_cleaned :
                print("Por favor, ejecuta primero el ejercicio 2.")
            elif data_group is None:
                print("Por favor, ejecuta primero el ejercicio 4.")
            else:
                ex5(data)
                print("Ejercicio 5 completado correctamente.")

        # Todos los ejercicios:
        elif opcion == 6:
            print("\n--- Ejecutando todos los ejercicios en orden ---")
            main_all()
            print("\n--- Todos los ejercicios completados ---")

        # Salir del programa:
        elif opcion == 0:
            print("Saliendo del programa.")
            break

        # Opción no válida:
        else:
            print("Opción no válida. Por favor, selecciona una opción del 0 al 6.")


# EJECUCIÓN DEL PROGRAMA
if __name__ == "__main__":
    main()
    