
# README - PEC4

## Descripción del Proyecto
El proyecto de la PEC4 implementa un conjunto de ejercicios relacionados con el análisis y transformación de datos, así como con la generación de visualizaciones. Este código está diseñado para ser ejecutado de manera interactiva, permitiendo al usuario seleccionar qué parte del proyecto desea resolver o ejecutar todas las etapas de forma secuencial.

## Estructura del Proyecto

### Directorios Principales:
- **/PEC4/Ex1**: Contiene la implementación del ejercicio 1 (importación y análisis inicial).
- **/PEC4/Ex2**: Implementación del ejercicio 2 (limpieza y anonimización de datos).
- **/PEC4/Ex3**: Implementación del ejercicio 3 (agrupamiento y generación de un histograma).
- **/PEC4/Ex4**: Implementación del ejercicio 4 (agrupamiento por clubes).
- **/PEC4/Ex5**: Implementación del ejercicio 5 (análisis final y resultados).
- **/PEC4/img**: Directorio que contiene las visualizaciones generadas, como el histograma.

### Archivos Principales:
- **main.py**: Archivo principal que orquesta la ejecución de los ejercicios y permite la interacción con el usuario.
- **requirements.txt**: Lista de dependencias necesarias para ejecutar el código.

## Requisitos del Sistema
- Python 3.8 o superior.
- Librerías requeridas (pueden instalarse con `pip install -r requirements.txt`):
  - pandas
  - numpy
  - matplotlib
  - Pillow

## Ejecución del Proyecto

### Paso 1: Clonar el Repositorio
Clona el repositorio o descarga los archivos directamente.

### Paso 2: Instalar Dependencias
Ejecuta el siguiente comando en el terminal desde el directorio raíz del proyecto:
```bash
pip install -r requirements.txt
```

### Paso 3: Ejecutar el Archivo Principal
Ejecuta el archivo `main.py` para comenzar la interacción:
```bash
python main.py
```

### Opciones del Menú:
1. Ejercicio 1: Importación y análisis inicial del dataset.
2. Ejercicio 2: Limpieza y anonimización del dataset.
3. Ejercicio 3: Agrupamiento de tiempos y generación del histograma.
4. Ejercicio 4: Agrupamiento por clubes.
5. Ejercicio 5: Análisis final.
6. Todos los ejercicios: Ejecuta todos los ejercicios en orden.
0. Salir: Termina el programa.

## Estructura del Código
El archivo principal `main.py` contiene dos funciones principales:
1. **`main_all()`**: Ejecuta todos los ejercicios en secuencia automáticamente.
2. **`main()`**: Permite al usuario elegir manualmente qué ejercicio ejecutar.

## Notas Importantes
1. Asegúrate de que las rutas de los datasets y archivos de imagen sean correctas.
2. Si encuentras la advertencia `SettingWithCopyWarning`, revisa que los DataFrames sean copias explícitas cuando sea necesario.
3. La generación del histograma en el ejercicio 3 requiere que la librería Pillow esté instalada correctamente.

## Solución de Problemas
- **Error: No se pudo importar el dataset.**
  - Verifica que el archivo del dataset esté en la ruta especificada.

- **Error: Imagen no encontrada.**
  - Asegúrate de que la ruta `./img/histograma.png` sea correcta y que el archivo exista.

## Referencias
- Documentación oficial de Pandas: [https://pandas.pydata.org/](https://pandas.pydata.org/)
- Documentación oficial de Matplotlib: [https://matplotlib.org/](https://matplotlib.org/)
- Documentación oficial de Pillow: [https://python-pillow.org/](https://python-pillow.org/)
