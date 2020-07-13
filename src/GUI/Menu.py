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

        #Instancia inicial del menu que va a aparecer cada vez que quiera editar
        self.editPanel = None

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

        #Creacion de espacio de notificacion cuando se haya agregado un producto
        self.mesagge = Label(text = '', fg= 'red')
        self.mesagge.grid(row = 3, column = 0,columnspan = 2, sticky = W + E)

        #Crear una tabla
        self.panel = ttk.Treeview(height = 10,column = 2)
        self.panel.grid(row = 4, column = 0,columnspan = 2)
        self.panel.heading('#0',text = 'Nombre', anchor = CENTER)
        self.panel.heading('#1',text = 'Precio',anchor = CENTER)

        #Creacion de los botones de la parte inferior
        self.btnEliminar = ttk.Button(self.window,text = 'Eliminar',command = self.deleteProduct)
        self.btnEliminar.grid(row = 7, column = 0, sticky = W + E)

        self.btnEditar = ttk.Button(self.window, text = 'Editar',command = self.editProduct)
        self.btnEditar.grid(row = 7, column = 1, sticky = W + E)
        

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
            self._db.insertQuery(self._db.getInsertQuery(),params)
            self.renderData()
            self.mesagge['text'] = '{} ha sido agregado de forma exitosa'.format(self.name.get())
            self.name.delete(0,END)
            self.price.delete(0,END)
        else:
            self.mesagge['text'] = 'Nombre y precio son requeridos'

    def deleteProduct(self):
        self.mesagge['text'] = ''
        try:
            name = self.panel.item(self.panel.selection())['text']
            self._db.insertQuery(self._db.getDeleteQuery(),(name,))
            self.mesagge['text'] = '{} ha sido eliminado exitosamente'.format(name)
            self.renderData()
        except IndexError as e:
            self.mesagge['text'] = 'Selecciona un elemento'
            return

    def editProduct(self):
        self.mesagge['text'] = ''
        name = ''
        try:
            name = self.panel.item(self.panel.selection())['text']
            #self._db.insertQuery(self._dbUpdateQuery(),(name,))
            #self.mesagge['text'] = '{} ha sido eliminado exitosamente'.format(name)
            self.renderData()
        except IndexError as e:
            self.mesagge['text'] = 'Selecciona un elemento'
            return

        self.editPanel = Toplevel()
        self.editPanel.title('Editar informacion')
        Label(self.editPanel, text = 'Nombre:').grid(row = 0,column = 1)
        Entry(self.editPanel, textvariable = StringVar(self.editPanel, value = name),state = 'readonly').grid(row = 0, column = 2)
    
        Label(self.editPanel,text = 'Precio:').grid(row = 1, column = 1)
        precioNuevo = Entry(self.editPanel).grid(row = 1,column = 2)
        
        
        