#Seccion Herramientas del Gestor de tablas termodinámica

#Autor: G. Villanueva 
#Github: Tabvov

from tkinter import *
from Funciones import*




    
variablesHerraminetasIniciales=[0,0,0,0,0]
varlocalHerramientas =[0,0,0,0,0] #X,x1,x0,y0,y1
resultado_interpolacion=0.0

def main_interpolador():
    global variablesHerraminetasIniciales
    global varlocalHerramientas
    global resultado_interpolacion

    rootHerramientas=Tk()
    rootHerramientas.title("Interpolador lineal")
    rootHerramientas.resizable(False,False)
    rootHerramientas.config(bg="#404353")
    rootHerramientas.iconbitmap("Images/marcelo.ico")

    varlocalHerramientas=[StringVar(),StringVar(),StringVar(),StringVar(),StringVar()]

    

    mainFrame=Frame(rootHerramientas, bg="#404353",width="500", height ="250")
    mainFrame.pack(padx=10)
    tituloLabel=Label(mainFrame,bg="#404355", text="Interpolador lineal", font=("consolas",15), fg="white")
    tituloLabel.grid(row=1, column=1,padx=20, pady=20, columnspan=10)


    def funcionBoton():
        global resultado_interpolacion

        #print(float(varlocalHerramientas[0].get()))
        #print(varlocalHerramientas[1].get())
        #print(varlocalHerramientas[2].get())
        #print(varlocalHerramientas[3].get())
        #print(varlocalHerramientas[4].get())
        #inter = Interpolacion(1.3,1,3,3,5)
        resultado_interpolacion=Interpolacion(float(varlocalHerramientas[0].get()), float(varlocalHerramientas[2].get()), float(varlocalHerramientas[1].get()), float(varlocalHerramientas[3].get()), float(varlocalHerramientas[4].get()))
        herramienta_interpolar(variablesHerraminetasIniciales)
        
        

    class Botones():
        def __init__(self, row, column, titulo):
            self.__width=10
            self.row=row
            self.column=column
            self.titulo=titulo
            

        def BotonInterpolar(self):
            botonGeneral2 =Button(mainFrame, text=self.titulo, width=self.__width, padx=10,  pady=10, font = "consolas",command=lambda:funcionBoton())
            botonGeneral2.grid(row=self.row, column=self.column, pady=17)

    class CuadroDeIngreso():
        def __init__(self, row, column,sentencia,i):
            self.__width="13"
            self.row=row
            self.column=column
            self.sentencia=StringVar(value=sentencia)
            self.index=i

        def recuperar(self):
            #global varlocalHerramientas
            self.varvar=self.sentencia
            
            cuadroDeIngreso=Entry(mainFrame, width=self.__width, textvariable= self.varvar)#varlocal)
            cuadroDeIngreso.config(background="#404352", font = ("consolas", 10) ,fg="white", justify="left")
            cuadroDeIngreso.grid(row=self.row, column=self.column, padx=5, pady=5)
            varlocalHerramientas[self.index]=self.varvar
            #print(self.varvar.get())
        
        def Resultado(self):
            #global varlocalHerramientas
        
            self.varvar=self.sentencia
            
            cuadroDeIngreso=Entry(mainFrame, width=self.__width, textvariable= self.varvar, background="#404352",state="readonly")
            cuadroDeIngreso.config(background="#404352", font = ("consolas", 10) ,fg="black", justify="left")
            cuadroDeIngreso.grid(row=self.row, column=self.column, padx=10, pady=10)

    class titulos():
        def __init__(self,row,column, titulo):
            self.row=row 
            self.column=column 
            self.titulo=StringVar(value=titulo)

        def mostrar(self):
            tituloLabel=Label(mainFrame, textvariable= self.titulo)
            tituloLabel.config( font=("calibri",10), background="#404352", fg="white")
            tituloLabel.grid(row=self.row, column=self.column)
        def linea(self):
            tituloLabel=Label(mainFrame, textvariable= self.titulo)
            tituloLabel.config( font=("calibri",10), background="#404352", fg="white")
            tituloLabel.grid(row=self.row, column=self.column, columnspan=3)

    def herramienta_interpolar(variables):
        Listalocal=variables

        Tituloy0=titulos(2,1,"y0")
        Tituloy0.mostrar()
        Cuadroy0=CuadroDeIngreso(3,1,Listalocal[3],3)
        
        suma1=titulos(3,2," + (")
        suma1.mostrar()

        Tituloy1=titulos(2,3,"y1")
        Tituloy1.mostrar()
        Cuadroy1=CuadroDeIngreso(3,3,Listalocal[4],4)
        Cuadroy1.recuperar()
        resta1=titulos(3,4," - ")
        resta1.mostrar()

        Titulo_y0=titulos(2,5,"y0")
        Titulo_y0.mostrar()
        Cuadro_y0=CuadroDeIngreso(3,5,Listalocal[3],3)
        Cuadro_y0.recuperar()

        Cuadroy0.recuperar() #<--se usa para no haber doble

        parentesis1=titulos(3,6,") (")
        parentesis1.mostrar()

        linea_division=titulos(5,3,"______________________________________      ")
        linea_division.linea()
        
        
        Titulo_x1=titulos(6,3," x_1")
        Titulo_x1.mostrar()

        Cuadro_x1=CuadroDeIngreso(7,3,Listalocal[1],1)
        Cuadro_x1.recuperar()

        resta2=titulos(7,4," - ")
        resta2.mostrar()
        
        Titulo_x0=titulos(6,5,"x0")
        Titulo_x0.mostrar()
        Cuadro_x0=CuadroDeIngreso(7,5,Listalocal[2],2)
        

        Tituloxx=titulos(2,7,"X")
        Tituloxx.mostrar()
        Cuadroxx=CuadroDeIngreso(3,7,Listalocal[0],0)
        Cuadroxx.recuperar()

        resta3=titulos(3,8,"  - ")
        resta3.mostrar()

        Titulox2=titulos(2,9,"x0")
        Titulox2.mostrar()
        Cuadrox0=CuadroDeIngreso(3,9,Listalocal[2],2)
        Cuadrox0.recuperar()

        Cuadro_x0.recuperar() #<--se usa para no haber doble

        parentesis1=titulos(3,10," )")
        parentesis1.mostrar()

        TituloResultado=titulos(8,5, "Resultado")
        TituloResultado.mostrar()
        CuadroResultado=CuadroDeIngreso(9,5,resultado_interpolacion,0)
        CuadroResultado.Resultado()


    Boton_interpolar=Botones(10,5,'Interpolar')
    Boton_interpolar.BotonInterpolar()
    herramienta_interpolar(variablesHerraminetasIniciales)
    rootHerramientas.mainloop()
    

#main_interpolador()



