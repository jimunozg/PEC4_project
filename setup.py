
from setuptools import setup, find_packages

setup(
    name="PEC4_Project",
    version="1.0.0",
    author="Ignacio Muñoz Gracia",
    author_email="imunoz5@uoc.edu",
    description="Proyecto PEC4: Análisis y transformación de datos con visualizaciones",
    long_description=open("README_PEC4.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/jimunozg/PEC4_Project",
    packages=find_packages(include=['PEC4', 'PEC4.*']),
    install_requires=[
        "pandas",
        "numpy",
        "matplotlib",
        "Pillow"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
    entry_points={
        'console_scripts': [
            'pec4=PEC4.main:main',
        ],
    },
    include_package_data=True,
)
