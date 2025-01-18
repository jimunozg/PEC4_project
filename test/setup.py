from setuptools import setup, find_packages

setup(
    name="PEC4_Tests",
    version="1.0.0",
    author="Ignacio Muñoz Gracia",
    author_email="imunoz5@uoc.edu",
    description="Pruebas unitarias para el proyecto PEC4",
    packages=find_packages(include=['PEC4', 'PEC4.*']),
    install_requires=[
        "pandas",
        "numpy",
        "matplotlib",
        "Pillow",
        "coverage"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
    entry_points={
        'console_scripts': [
            'run-tests=unittest:main',
        ],
    },
    include_package_data=True,
)

# Nota adicional para README:
# Este archivo se puede utilizar para instalar todas las dependencias necesarias para ejecutar las pruebas unitarias. Ejecuta:
# pip install .
# Esto instalará automáticamente todas las librerías especificadas en `install_requires`. Una vez instaladas, puedes ejecutar las pruebas con:
# python -m unittest discover