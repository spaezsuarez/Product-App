from setuptools import setup

setup(
    name = "src",
    version = "0.1",
    description = "Pequeña aplicacion para aprender a usar orientacion de objetos en python y una conexion a una base de datos relacional en sqlite",
    author = "Sergio David Paz Suarez",
    author_email = "sdpaezs@correo.duistrital.edu.co",
    packages=['src','src.GUI','src.Persistence']
)