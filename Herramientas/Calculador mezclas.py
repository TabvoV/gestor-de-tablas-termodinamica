#Seccion Herramientas del Gestor de tablas termodinámica

#Autor: G. Villanueva 
#Github: Tabvov

from tkinter import *
from Funciones import*




variablesHerraminetasInicialesMezcla=[0,0,0]
varlocalHerramientasMezclas =[0,0,0] #X,x1,x0,y0,y1
resultado_Mezclas=0.0

def main_calculadora_mezcla():
    global variablesHerraminetasInicialesMezcla
    global varlocalHerramientasMezclas
    global resultado_Mezclas

    rootMezlcas=Tk()
    rootMezlcas.title("Interpolador lineal")
    rootMezlcas.resizable(False,False)
    rootMezlcas.config(bg="#404353")
    rootMezlcas.iconbitmap("Images/marcelo.ico")

    varlocalHerramientasMezclas=[StringVar(),StringVar(),StringVar(),StringVar(),StringVar()]

    

    mainFrame=Frame(rootMezlcas, bg="#404353",width="500", height ="250")
    mainFrame.pack(padx=10)
    tituloLabel=Label(mainFrame,bg="#404355", text="Calculador de propiedades de  \n Vapores-humedos", font=("consolas",15), fg="white")
    tituloLabel.grid(row=1, column=1,padx=20, pady=20, columnspan=9)


    def funcionBotonMezcla():
        global resultado_Mezclas
        resultado_Mezclas=calculador_mezclas(float(varlocalHerramientasMezclas[0].get()), float(varlocalHerramientasMezclas[1].get()), float(varlocalHerramientasMezclas[2].get()))
        herramienta_mezcla(variablesHerraminetasInicialesMezcla)
        
        

    class BotonesMezcla():
        def __init__(self, row, column, titulo):
            self.__width=8
            self.row=row
            self.column=column
            self.titulo=titulo
            

        def BotonCalcularMezcla(self):
            botonGeneral2 =Button(mainFrame, text=self.titulo, width=self.__width, font = "consolas",command=lambda:funcionBotonMezcla())
            botonGeneral2.grid(row=self.row, column=self.column,pady=10)#, columnspan=3)

    class CuadroDeIngresoMezcla():
        def __init__(self, row, column,sentencia,i):
            self.__width="13"
            self.row=row
            self.column=column
            self.sentencia=StringVar(value=sentencia)
            self.index=i

        def recuperar(self):
            #global varlocalHerramientasMezclas
            self.varvar=self.sentencia
            
            cuadroDeIngreso=Entry(mainFrame, width=self.__width, textvariable= self.varvar)#varlocal)
            cuadroDeIngreso.config(background="#404352", font = ("consolas", 10) ,fg="white", justify="left")
            cuadroDeIngreso.grid(row=self.row, column=self.column, padx=5, pady=5)
            varlocalHerramientasMezclas[self.index]=self.varvar
            print(self.varvar.get())
        
        def Resultado(self):
            #global varlocalHerramientasMezclas
        
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

    def herramienta_mezcla(variables):
        Listalocal=variables

        Tituloy_f=titulos(2,1,"Y_f")
        Tituloy_f.mostrar()
        Cuadroy_f=CuadroDeIngresoMezcla(3,1,Listalocal[0],0)
        

        suma1=titulos(3,2," + ")
        suma1.mostrar()

        Titulox=titulos(2,3,"X")
        Titulox.mostrar()
        Cuadrox=CuadroDeIngresoMezcla(3,3,Listalocal[2],2)
        Cuadrox.recuperar()
        resta1=titulos(3,4," (")
        resta1.mostrar()

        Tituloy_g=titulos(2,5,"Y_g")
        Tituloy_g.mostrar()
        Cuadroy_g=CuadroDeIngresoMezcla(3,5,Listalocal[1],1)
        Cuadroy_g.recuperar()


        parentesis1=titulos(3,6," - ")
        parentesis1.mostrar()


        Titulo_y_f=titulos(2,7,"Y_f")
        Titulo_y_f.mostrar()
        Cuadro_y_f=CuadroDeIngresoMezcla(3,7,Listalocal[0],0)
        Cuadro_y_f.recuperar()
        Cuadroy_f.recuperar()
        
        parentesis1=titulos(3,8," )")
        parentesis1.mostrar()

        TituloResultado=titulos(4,3, "Resultado")
        TituloResultado.mostrar()
        CuadroResultado=CuadroDeIngresoMezcla(5,3,resultado_Mezclas,0)
        CuadroResultado.Resultado()


    Boton_calcular_mezcla=BotonesMezcla(5,5,'Calcular')
    Boton_calcular_mezcla.BotonCalcularMezcla()
    herramienta_mezcla(variablesHerraminetasInicialesMezcla)
    rootMezlcas.mainloop()
    

main_calculadora_mezcla()



