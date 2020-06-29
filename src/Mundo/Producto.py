from tkinter import ttk #libreria que me ermite hacer la interfaz
from tkinter import * #Segundo import para traer elements graficos como botones
import sqlite3 #Modulo de python para conexion con la base de datos de sqlite

class Producto:

    #Metodo constructor
    def __init__(self,window):
        self.window = window
        self.window.title('Product Aplication')
        #Creacion de un contenedor
        frame = LabelFrame(self.window, text = 'Registrar un nuevo producto')
        frame.grid(row = 0, column = 0, columnspan = 3, pady = 20)
        #nameINput 
        Label(text='Name: ').grid(row = 1, column = 0)
        self.name = Entry(frame).grid(row = 1,column = 1)

        Label(text='Precio: ').grid(row = 2, column = 0)
        self.price = LabelFrame(frame, text = 'Ingrese el precio:')
        self.price.grid(row = 2,column = 1)
        
    
    
        