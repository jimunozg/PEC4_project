# README - PEC4

## Descripción del Proyecto
El proyecto de la PEC4 implementa un conjunto de ejercicios relacionados con el análisis y transformación de datos, así como con la generación de visualizaciones. Este código está diseñado para ser ejecutado de manera interactiva, permitiendo al usuario seleccionar qué parte del proyecto desea resolver o ejecutar todas las etapas de forma secuencial.

## Estructura del Proyecto

### Directorios Principales:
- **/PEC4**: Contiene el archivo main.py, que implementa la función e interfaz principal del programa.
- **/PEC4/Ex1**: Contiene la implementación del ejercicio 1 (importación y análisis inicial).
- **/PEC4/Ex2**: Implementación del ejercicio 2 (limpieza y anonimización de datos).
- **/PEC4/Ex3**: Implementación del ejercicio 3 (agrupamiento y generación de un histograma).
- **/PEC4/Ex4**: Implementación del ejercicio 4 (agrupamiento por clubes).
- **/PEC4/Ex5**: Implementación del ejercicio 5 (análisis final y resultados).
- **/img**: Directorio que contiene las visualizaciones generadas, como el histograma.
- **/test**: Directorio que contiene todo lo referente a los tests del programa.
- **/data**: Directorio que contiene los archivos de datos usados en el proyecto.

### Archivos Principales:
- **main.py**: Archivo principal que orquesta la ejecución de los ejercicios y permite la interacción con el usuario.
- **requirements.txt**: Lista de dependencias necesarias para ejecutar el código.
- **LICENSE.txt**: licencia correspondiente al proyecto.
- **README_PEC4.txt**: README referente al proyecto en su conjunto, donde se explica como preparar el entorno y ejecutarlo.


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
Ejecuta el archivo `main.py` desde el dirctorio raíz para comenzar la interacción:
```bash
python PEC4/main.py
```

### Opciones del Menú:
1. Ejercicio 1: Importación y análisis inicial del dataset.
2. Ejercicio 2: Limpieza y anonimización del dataset.
3. Ejercicio 3: Agrupamiento de tiempos y generación del histograma.
4. Ejercicio 4: Agrupamiento por clubes.
5. Ejercicio 5: Análisis final.
6. Todos los ejercicios: Ejecuta todos los ejercicios en orden.
0. Salir: Termina el programa.

## Ejecución de Pruebas

### Instalación de Dependencias para Pruebas
Asegúrate de que las dependencias estén instaladas. Esto se puede hacer utilizando el archivo `setup_test.py` con el siguiente comando:
```bash
pip install test/
```
Esto instalará automáticamente las librerías requeridas para las pruebas.

### Ejecutar Pruebas Unitarias
Para ejecutar todas las pruebas unitarias, usa el siguiente comando:
```bash
python -m unittest discover
```

### Medir Cobertura de Código
Para verificar el porcentaje de cobertura del código durante las pruebas, utiliza la herramienta `coverage`:
1. Instala `coverage` si no lo tienes:
   ```bash
   pip install coverage
   ```
2. Ejecuta las pruebas con cobertura:
   ```bash
   coverage run --source=PEC4 -m unittest discover
   ```
3. Genera un reporte en la consola:
   ```bash
   coverage report
   ```
4. Genera un reporte HTML detallado:
   ```bash
   coverage html
   ```
   Abre el archivo `htmlcov/index.html` en tu navegador para ver un informe visual de la cobertura.

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

## Ejemplo de cobertura del código en los tests

```bash
(pec4) coverage run --source=PEC4 -m unittest discover

--- Ejercicio 1: Importación y análisis inicial del dataset ---

* Primeras 5 filas del dataset: 
    dorsal              biker           club      time
0    4515  Christopher Bauer  Independiente  00:00:00
1    2017         Mary White  Independiente  00:00:00
2     116      Melissa Olson  Independiente  00:00:00
3    1469       Joshua Klein  Independiente  00:00:00
4    4536     Maurice Castro  Independiente  00:00:00

* Columnas:      ['dorsal', 'biker', 'club', 'time']

* Número de ciclistas que participaron en la prueba:     3975

* Tamaño total del dataset:      15900
.
--- Ejercicio 1: Importación y análisis inicial del dataset ---

* Primeras 5 filas del dataset: 
    dorsal              biker           club      time
0    4515  Christopher Bauer  Independiente  00:00:00
1    2017         Mary White  Independiente  00:00:00
2     116      Melissa Olson  Independiente  00:00:00
3    1469       Joshua Klein  Independiente  00:00:00
4    4536     Maurice Castro  Independiente  00:00:00

* Columnas:      ['dorsal', 'biker', 'club', 'time']

* Número de ciclistas que participaron en la prueba:     3975

* Tamaño total del dataset:      15900

--- Ejercicio 2: Anonimización y limpieza del dataset ---

Datos anonimizados (primeros 5 registros): 
    dorsal             biker           club      time
0    4515      Kyle Flowers  Independiente  00:00:00
1    2017   Elizabeth Perry  Independiente  00:00:00
2     116     Lisa Robinson  Independiente  00:00:00
3    1469      Anna Jackson  Independiente  00:00:00
4    4536  Kimberly Kaufman  Independiente  00:00:00

* Total de ciclistas que realmente participaron: 3887

* Datos de los 5 primeros ciclistas que participaron realmente: 
     dorsal            biker               club      time
83    1484  Brenda Reynolds      C.c. Alfinden  03:01:18
84    1916     Jerry Abbott      GEIC Carcalin  03:05:19
85    1424   Rebekah Taylor      Independiente  03:09:03
86     160   Brandon Newton      Independiente  03:20:07
87       2   Ross Armstrong  Orbea Sport CLUB   03:20:08

* Los datos asociados al ciclista con el dorsal 1000 son: 
      dorsal        biker           club      time
174    1000  Kim Woodard  C.D.El cubio   03:56:33
.
--- Ejercicio 1: Importación y análisis inicial del dataset ---

* Primeras 5 filas del dataset: 
    dorsal              biker           club      time
0    4515  Christopher Bauer  Independiente  00:00:00
1    2017         Mary White  Independiente  00:00:00
2     116      Melissa Olson  Independiente  00:00:00
3    1469       Joshua Klein  Independiente  00:00:00
4    4536     Maurice Castro  Independiente  00:00:00

* Columnas:      ['dorsal', 'biker', 'club', 'time']

* Número de ciclistas que participaron en la prueba:     3975

* Tamaño total del dataset:      15900

--- Ejercicio 3: Agrupamiento de tiempos y generación del histograma ---
      dorsal              biker                 club      time time_grouped
0       4515  Christopher Bauer        Independiente  00:00:00        00:00
1       2017         Mary White        Independiente  00:00:00        00:00
2        116      Melissa Olson        Independiente  00:00:00        00:00
3       1469       Joshua Klein        Independiente  00:00:00        00:00
4       4536     Maurice Castro        Independiente  00:00:00        00:00
...      ...                ...                  ...       ...          ...
3970    2877        Glenda Ball        Arroyobikers   05:36:55        05:20
3971     136     Amber Franklin          CD El Cubio  03:52:54        03:40
3972    4390        Denise Peck  En Bici Por Madrid   07:13:22        07:00
3973     597  Matthew Frederick            RR Bikers  05:58:58        05:40
3974     108       Zachary Knox      Pista Barcelona  04:01:24        04:00

[3975 rows x 5 columns]

* Datos agrupados: 
    time_grouped  count
0         00:00     88
1         03:00      3
2         03:20     46
3         03:40    101
4         04:00    253
5         04:20    309
6         04:40    431
7         05:00    493
8         05:20    510
9         05:40    455
10        06:00    360
11        06:20    267
12        06:40    243
13        07:00    148
14        07:20    130
15        07:40     73
16        08:00     32
17        08:20     27
18        08:40      6

Histograma guardado en: ./img/histograma.png.

.
--- Ejercicio 1: Importación y análisis inicial del dataset ---

* Primeras 5 filas del dataset: 
    dorsal              biker           club      time
0    4515  Christopher Bauer  Independiente  00:00:00
1    2017         Mary White  Independiente  00:00:00
2     116      Melissa Olson  Independiente  00:00:00
3    1469       Joshua Klein  Independiente  00:00:00
4    4536     Maurice Castro  Independiente  00:00:00

* Columnas:      ['dorsal', 'biker', 'club', 'time']

* Número de ciclistas que participaron en la prueba:     3975

* Tamaño total del dataset:      15900

--- Ejercicio 4: Limpieza de nombres de clubes ciclistas ---
    dorsal              biker                   club      time   club_clean
0     4515  Christopher Bauer          Independiente  00:00:00  INDEPENDIEN
1     2017         Mary White          Independiente  00:00:00  INDEPENDIEN
2      116      Melissa Olson          Independiente  00:00:00  INDEPENDIEN
3     1469       Joshua Klein          Independiente  00:00:00  INDEPENDIEN
4     4536     Maurice Castro          Independiente  00:00:00  INDEPENDIEN
5     1810      Michael Baker              EL BICHO   00:00:00     EL BICHO
6     1247         Chad Chase          Independiente  00:00:00  INDEPENDIEN
7     4625  Jonathan Caldwell          Independiente  00:00:00  INDEPENDIEN
8       91     Roberto Powell          Independiente  00:00:00  INDEPENDIEN
9     5320       Sarah Hansen          Independiente  00:00:00  INDEPENDIEN
10     440       Chase Porter  Club ciclista Alcañiz  00:00:00      ALCAÑIZ
11    2207     Victoria Perez          Independiente  00:00:00  INDEPENDIEN
12    3058   Michael Marshall          Independiente  00:00:00  INDEPENDIEN
13    2287        Debbie Hess          Independiente  00:00:00  INDEPENDIEN
14     253        Luke Arnold    Club Ciclista Frafa  00:00:00        FRAFA
      club_clean  count
460  INDEPENDIEN   2544
732     SARIÑENA     21
844         UCSC     19
634      OSCENSE     16
92     BARBASTRO     11
.
--- Ejercicio 1: Importación y análisis inicial del dataset ---

* Primeras 5 filas del dataset: 
    dorsal              biker           club      time
0    4515  Christopher Bauer  Independiente  00:00:00
1    2017         Mary White  Independiente  00:00:00
2     116      Melissa Olson  Independiente  00:00:00
3    1469       Joshua Klein  Independiente  00:00:00
4    4536     Maurice Castro  Independiente  00:00:00

* Columnas:      ['dorsal', 'biker', 'club', 'time']

* Número de ciclistas que participaron en la prueba:     3975

* Tamaño total del dataset:      15900

--- Ejercicio 4: Limpieza de nombres de clubes ciclistas ---
    dorsal              biker                   club      time   club_clean
0     4515  Christopher Bauer          Independiente  00:00:00  INDEPENDIEN
1     2017         Mary White          Independiente  00:00:00  INDEPENDIEN
2      116      Melissa Olson          Independiente  00:00:00  INDEPENDIEN
3     1469       Joshua Klein          Independiente  00:00:00  INDEPENDIEN
4     4536     Maurice Castro          Independiente  00:00:00  INDEPENDIEN
5     1810      Michael Baker              EL BICHO   00:00:00     EL BICHO
6     1247         Chad Chase          Independiente  00:00:00  INDEPENDIEN
7     4625  Jonathan Caldwell          Independiente  00:00:00  INDEPENDIEN
8       91     Roberto Powell          Independiente  00:00:00  INDEPENDIEN
9     5320       Sarah Hansen          Independiente  00:00:00  INDEPENDIEN
10     440       Chase Porter  Club ciclista Alcañiz  00:00:00      ALCAÑIZ
11    2207     Victoria Perez          Independiente  00:00:00  INDEPENDIEN
12    3058   Michael Marshall          Independiente  00:00:00  INDEPENDIEN
13    2287        Debbie Hess          Independiente  00:00:00  INDEPENDIEN
14     253        Luke Arnold    Club Ciclista Frafa  00:00:00        FRAFA
      club_clean  count
460  INDEPENDIEN   2544
732     SARIÑENA     21
844         UCSC     19
634      OSCENSE     16
92     BARBASTRO     11

--- Ejercicio 5: Análisis del club UCSC ---
Ciclistas del club UCSC: 
          time club_clean
791   04:48:42       UCSC
872   04:52:38       UCSC
928   04:55:56       UCSC
1626  05:28:52       UCSC
1883  05:40:38       UCSC
1885  05:40:41       UCSC
1888  05:40:42       UCSC
1999  05:46:06       UCSC
2115  05:51:54       UCSC
2471  06:12:06       UCSC
2801  06:36:58       UCSC
2832  06:39:47       UCSC
3026  06:54:27       UCSC
3027  06:54:27       UCSC
3045  06:57:26       UCSC
3115  07:08:55       UCSC
3204  07:21:23       UCSC
3247  07:29:53       UCSC
3321  07:41:05       UCSC

Mejor ciclista del club UCSC: 
dorsal                     415
biker           Benjamin Mason
club                     UCSC 
time                  04:48:42
club_clean                UCSC
time_seconds             17322
Name: 791, dtype: object

Posición del mejor ciclista: 986

Porcentaje sobre el total: 24.81%

.
--- Ejercicio 1: Importación y análisis inicial del dataset ---

* Primeras 5 filas del dataset: 
    dorsal              biker           club      time
0    4515  Christopher Bauer  Independiente  00:00:00
1    2017         Mary White  Independiente  00:00:00
2     116      Melissa Olson  Independiente  00:00:00
3    1469       Joshua Klein  Independiente  00:00:00
4    4536     Maurice Castro  Independiente  00:00:00

* Columnas:      ['dorsal', 'biker', 'club', 'time']

* Número de ciclistas que participaron en la prueba:     3975

* Tamaño total del dataset:      15900
.
--- Ejercicio 1: Importación y análisis inicial del dataset ---

* Primeras 5 filas del dataset: 
    dorsal              biker           club      time
0    4515  Christopher Bauer  Independiente  00:00:00
1    2017         Mary White  Independiente  00:00:00
2     116      Melissa Olson  Independiente  00:00:00
3    1469       Joshua Klein  Independiente  00:00:00
4    4536     Maurice Castro  Independiente  00:00:00

* Columnas:      ['dorsal', 'biker', 'club', 'time']

* Número de ciclistas que participaron en la prueba:     3975

* Tamaño total del dataset:      15900
.
----------------------------------------------------------------------
Ran 7 tests in 1.468s

OK
(pec4) coverage report
Name                   Stmts   Miss  Cover
------------------------------------------
PEC4/Ex1/Ex1.py           15      3    80%
PEC4/Ex1/__init__.py       0      0   100%
PEC4/Ex2/Ex2.py           28      3    89%
PEC4/Ex2/__init__.py       0      0   100%
PEC4/Ex3/Ex3.py           38      2    95%
PEC4/Ex3/__init__.py       0      0   100%
PEC4/Ex4/Ex4.py           23      2    91%
PEC4/Ex4/__init__.py       0      0   100%
PEC4/Ex5/Ex5.py           19      2    89%
PEC4/Ex5/__init__.py       0      0   100%
PEC4/__init__.py           0      0   100%
PEC4/main.py              81     54    33%
------------------------------------------
TOTAL                    204     66    68%
(pec4)
```
