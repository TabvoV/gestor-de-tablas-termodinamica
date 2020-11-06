#Seccion Herramientas del Gestor de tablas termodinámica

#Autor: G. Villanueva 
#Github: Tabvov
from tkinter import *
from Funciones import*



variablesHerraminetasInicialeEntalpia=[0,0,0,0]
varlocalHerramientasEntalpia =[0,0,0,0] #X,x1,x0,y0,y1
resultado_entalpia=0.0

def main_calculadora_entalpia():
    global variablesHerraminetasInicialeEntalpia
    global varlocalHerramientasEntalpia
    global resultado_entalpia

    rootEntalpia=Tk()
    rootEntalpia.title("Calculadora de entalpia")
    rootEntalpia.resizable(False,False)
    rootEntalpia.config(bg="#404353")
    #rootEntalpia.iconbitmap("icono.ico")

    varlocalHerramientasEntalpia=[StringVar(),StringVar(),StringVar(),StringVar(),StringVar()]

    

    mainFrame=Frame(rootEntalpia, bg="#404353",width="500", height ="250")
    mainFrame.pack(padx=10)
    tituloLabel=Label(mainFrame,bg="#404355", text="Calculadora de entalpia", font=("consolas",15), fg="white")
    tituloLabel.grid(row=1, column=1,padx=20, pady=20, columnspan=9)


    def funcionBotonEntalpia():
        global resultado_entalpia
        resultado_entalpia=calculador_entalpia(float(varlocalHerramientasEntalpia[0].get()), float(varlocalHerramientasEntalpia[1].get()), float(varlocalHerramientasEntalpia[2].get()),float(varlocalHerramientasEntalpia[3].get()))
        herramienta_entalpia(variablesHerraminetasInicialeEntalpia)
        
        

    class BotonesEntalpia():
        def __init__(self, row, column, titulo):
            self.__width=8
            self.row=row
            self.column=column
            self.titulo=titulo
            

        def BotonCalcularEntalpia(self):
            botonGeneral2 =Button(mainFrame, text=self.titulo, width=self.__width, font = "consolas",command=lambda:funcionBotonEntalpia())
            botonGeneral2.grid(row=self.row, column=self.column,pady=10)#, columnspan=3)

    class CuadroDeIngresoEntalpia():
        def __init__(self, row, column,sentencia,i):
            self.__width="13"
            self.row=row
            self.column=column
            self.sentencia=StringVar(value=sentencia)
            self.index=i

        def recuperar(self):
            #global varlocalHerramientasEntalpia
            self.varvar=self.sentencia
            
            cuadroDeIngreso=Entry(mainFrame, width=self.__width, textvariable= self.varvar)#varlocal)
            cuadroDeIngreso.config(background="#404352", font = ("consolas", 10) ,fg="white", justify="left")
            cuadroDeIngreso.grid(row=self.row, column=self.column, padx=5, pady=5)
            varlocalHerramientasEntalpia[self.index]=self.varvar
            print(self.varvar.get())
        
        def Resultado(self):
            #global varlocalHerramientasEntalpia
        
            self.varvar=self.sentencia
            
            cuadroDeIngreso=Entry(mainFrame, width=self.__width, textvariable= self.varvar, background="#404352",state="readonly")
            cuadroDeIngreso.config(background="#404352", font = ("consolas", 10) ,fg="black", justify="left")
            cuadroDeIngreso.grid(row=self.row, column=self.column, padx=10, pady=10)

    class titulos_entalpia():
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

    def herramienta_entalpia(variables):
        Listalocal=variables

        Tituloh_f=titulos_entalpia(2,1,"h_f@T")
        Tituloh_f.mostrar()
        Cuadroh_f=CuadroDeIngresoEntalpia(3,1,Listalocal[0],0)
        Cuadroh_f.recuperar()
        

        suma1=titulos_entalpia(3,2," + ")
        suma1.mostrar()

        Titulov=titulos_entalpia(2,3,"V_f@T")
        Titulov.mostrar()
        Cuadrov=CuadroDeIngresoEntalpia(3,3,Listalocal[1],1)
        Cuadrov.recuperar()
        resta1=titulos_entalpia(3,4," (")
        resta1.mostrar()

        Tituloy_p=titulos_entalpia(2,5,"P")
        Tituloy_p.mostrar()
        Cuadroy_p=CuadroDeIngresoEntalpia(3,5,Listalocal[2],2)
        Cuadroy_p.recuperar()


        parentesis1=titulos_entalpia(3,6," - ")
        parentesis1.mostrar()


        Titulo_psat=titulos_entalpia(2,7,"P_sat@T")
        Titulo_psat.mostrar()
        Cuadro_psat=CuadroDeIngresoEntalpia(3,7,Listalocal[3],3)
        Cuadro_psat.recuperar()
        
        
        parentesis1=titulos_entalpia(3,8," )")
        parentesis1.mostrar()

        TituloResultado=titulos_entalpia(4,3, "Resultado ≅")
        TituloResultado.mostrar()
        CuadroResultado=CuadroDeIngresoEntalpia(5,3,resultado_entalpia,0)
        CuadroResultado.Resultado()


    boton_calcular_entalpia=BotonesEntalpia(5,5,'Calcular')
    boton_calcular_entalpia.BotonCalcularEntalpia()
    herramienta_entalpia(variablesHerraminetasInicialeEntalpia)
    rootEntalpia.mainloop()
    

main_calculadora_entalpia()



