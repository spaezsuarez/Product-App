from tkinter import ttk #libreria que me ermite hacer la interfaz
from tkinter import * #Segundo import para traer elements graficos como botones
from Persistence.ConexionBD import ConexionBD

class Producto:

    #Metodo constructor
    def __init__(self,window):
        #Instancia de un objeto para conectarse a la base de datos 
        self._db = ConexionBD()
        #-------------------------------------------------------------------------------------------
        self.window = window
        self.window.title('Product Aplication')

        #Creacion de un contenedor y agregar a la ventana que recibe como parametro
        self.frame = LabelFrame(self.window, text = 'Registrar un nuevo producto')
        self.frame.grid(row = 0, column = 0, columnspan = 3, pady = 20)

        #nameInput agregado al contenedor
        Label(frame,text='Name: ').grid(row = 1, column = 0)
        self.name = Entry(frame)
        self.name.focus()
        self.name.grid(row = 1,column = 1)

        #PriceInput agregado al contenedor
        Label(frame,text='Precio: ').grid(row = 2, column = 0)
        self.price = Entry(frame)
        self.price.grid(row = 2,column = 1)

        #Creacion de un boton
        self.btn = ttk.Button(frame,text='Guardar')
        self.btn.grid(row = 3, columnspan = 2,sticky = W + E)

        #Crear una tabla
        self.panel = ttk.Treeview(height = 10,column = 2)
        self.panel.grid(row = 4, column = 0,columnspan = 2)
        self.panel.heading('#0',text = 'Nombre', anchor = CENTER)
        self.panel.heading('#1',text = 'Precio',anchor = CENTER)
        #-----------------------------------------------------------------------------------------------
        self.renderData()
        
    def renderData(self):
        array = self._db.getProducts()
        ActualRecords = self.panel.get_children()
        #Primer ciclo para limpiar la infiormacion existente en la interfaz
        for element in ActualRecords:
            self.panel.delete(element)
        #Segundo ciclo para actualizar la informacion de la interfaz con el objeto de la conslta
        for newElement in array:
            self.panel.insert('',0,text = newElement[1], values = newElement[2])


        
    
        