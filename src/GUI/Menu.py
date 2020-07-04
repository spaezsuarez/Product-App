from tkinter import ttk #libreria que me ermite hacer la interfaz
from tkinter import * #Segundo import para traer elements graficos como botones
from Persistence.ConexionBD import ConexionBD

class Menu:

    def __init__(self):
        #Instancia de un objeto para conectarse a la base de datos 
        self._db = ConexionBD()
        #-------------------------------------------------------------------------------------------
        self.window = Tk()
        self.window.title('Product Aplication')

        #Creacion de un contenedor y agregar a la ventana que recibe como parametro
        self.frame = LabelFrame(self.window, text = 'Registrar un nuevo producto')
        self.frame.grid(row = 0, column = 0, columnspan = 3, pady = 20)

        #nameInput agregado al contenedor
        Label(self.frame,text='Name: ').grid(row = 1, column = 0)
        self.name = Entry(self.frame)
        self.name.focus()
        self.name.grid(row = 1,column = 1)

        #PriceInput agregado al contenedor
        Label(self.frame,text='Precio: ').grid(row = 2, column = 0)
        self.price = Entry(self.frame)
        self.price.grid(row = 2,column = 1)

        #Creacion de un boton
        self.btn = ttk.Button(self.frame,text='Guardar',command = self.addProduct)
        self.btn.grid(row = 3, columnspan = 2,sticky = W + E)

        #Crear una tabla
        self.panel = ttk.Treeview(height = 10,column = 2)
        self.panel.grid(row = 4, column = 0,columnspan = 2)
        self.panel.heading('#0',text = 'Nombre', anchor = CENTER)
        self.panel.heading('#1',text = 'Precio',anchor = CENTER)
        #-----------------------------------------------------------------------------------------------
        self.renderData()
        self.window.mainloop()
        
    def renderData(self):
        array = self._db.getProducts()
        ActualRecords = self.panel.get_children()
        #Primer ciclo para limpiar la infiormacion existente en la interfaz
        for element in ActualRecords:
            self.panel.delete(element)
        #Segundo ciclo para actualizar la informacion de la interfaz con el objeto de la conslta
        for newElement in array:
            self.panel.insert('',0,text = newElement[1], values = newElement[2])

    def validateEntryData(self):
        if len(self.name.get()) != 0 and len(self.price.get()) != 0:
            return True
        else:
            return False 

    def addProduct(self):
        if self.validateEntryData():
            params = (self.name.get(),self.price.get())
            self._db.insertData(self._db.getInsertQuery(),params)
            self.renderData()
        else:
            print("Los campos estan vacios")
