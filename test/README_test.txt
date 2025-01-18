# README - Ejecución de Pruebas

## Descripción
Este proyecto incluye pruebas unitarias diseñadas para validar la funcionalidad de cada uno de los ejercicios presentes en el proyecto PEC4. Las pruebas verifican la importación, limpieza, agrupamiento y análisis de datos, además de garantizar que no se produzcan errores durante su ejecución.

## Requisitos Previos
- Python 3.8 o superior.
- Librerías requeridas:
  - pandas
  - unittest
  - numpy
  - matplotlib
  - Pillow
- La estructura del proyecto debe estar correctamente configurada, con todos los módulos accesibles.

## Instalación de Dependencias
Asegúrate de instalar todas las dependencias necesarias. Esto se puede hacer ejecutando:

```bash
pip install -r test/test_requirements.txt
```

## Resultados del test

```bash
(pec4) python -m unittest discover

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
    dorsal           biker           club      time
0    4515       Sarah Liu  Independiente  00:00:00
1    2017   Valerie Moore  Independiente  00:00:00
2     116    James Taylor  Independiente  00:00:00
3    1469  Yolanda Graves  Independiente  00:00:00
4    4536      John Perez  Independiente  00:00:00

* Total de ciclistas que realmente participaron: 3887

* Datos de los 5 primeros ciclistas que participaron realmente: 
     dorsal         biker               club      time
83    1484    John Lynch      C.c. Alfinden  03:01:18
84    1916   Joshua Hale      GEIC Carcalin  03:05:19
85    1424    Lisa Lewis      Independiente  03:09:03
86     160   Lisa Savage      Independiente  03:20:07
87       2  John Garrett  Orbea Sport CLUB   03:20:08

* Los datos asociados al ciclista con el dorsal 1000 son: 
      dorsal            biker           club      time
174    1000  Danielle Thomas  C.D.El cubio   03:56:33
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
Ran 7 tests in 1.222s

OK
(pec4)
```
