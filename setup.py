from setuptools import setup

setup(
    name = "src",
    version = "0.1",
    descripction = "carpeta src con las distintas clases y paquetes del programa ademas de la base de datos",
    author = "Sergio David Paz Suarez",
    author_email = "sdpaezs@correo.duistrital.edu.co",
    packages=['src','src.Mundo','src.Persistence']
)