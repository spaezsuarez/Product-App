from tkinter import ttk #libreria que me ermite hacer la interfaz
from tkinter import * #Segundo import para traer elements graficos como botones
from Mundo.Producto import Producto

def main():
    window = Tk()
    app = Producto(window)
    window.mainloop() #Se ejecuta la ventana 

main()