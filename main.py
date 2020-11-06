#GUI para Gestor de tablas de termodinámica v0.1

#Autor: G. Villanueva 
#Github: Tabvov


#Para agregar tabla seguir los siguietes pasos:
#agregarla a la base de datos
#Ingresar las variables de los titulos para las pantallas
#Ingresar las opciones para el menú
#en la funcion seleccionMenuTabla generar un elif para hacer seleccion_tabla="CODIGO DE TABLA"


from tkinter import *
from tkinter import  ttk
from tkinter import messagebox
from Kernel import *
from Funciones import *
from Tooltips import *


#########################################################################################################################################
#GUI ROOT 
#########################################################################################################################################

root=Tk()
root.title("Gestor de tablas de Termodinámica v0.1")
root.resizable(False,False)
root.iconbitmap(resolver_ruta("./Images/icono.ico"))
root.config(width="1000", height ="450", bg="#404352")


#########################################################################################################################################
#VARIABLES PUBLICAS
#########################################################################################################################################

numeroPantallaInicial=["0","0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0","0"]
#numeroPantalla=[133, 296.044, 0.001073, 0.616, 558.886, 1983.74, 2542.62, 559.202, 2164.94, 2724.18, 1.66616, 5.33082, 6.99698] 
variables_titulos=[
                ('T','Psat','Vf','Vg','Uf','Ufg','Ug','hf','hfg','hg','Sf','Sfg', 'Sg'),
                ('P','Tsat','Vf','Vg','Uf','Ufg','Ug','hf','hfg','hg','Sf','Sfg', 'Sg'),
                ('P','T','V','U','H','S','VAR','VAR','VAR','VAR','VAR','VAR','VAR'),
                ('P','T','V','U','H','S','VAR','VAR','VAR','VAR','VAR','VAR','VAR'),
                ('T','Psat','Vf','Vg','Uf','Ufg','Ug','hf','hfg','hg','Sf','Sfg', 'Sg'),
                ('P','Tsat','Vf','Vg','Uf','Ufg','Ug','hf','hfg','hg','Sf','Sfg', 'Sg'),
                ('P','T','V','U','H','S','VAR','VAR','VAR','VAR','VAR','VAR','VAR'),
                ('VAR','VAR','VAR','VAR','VAR','VAR','VAR','VAR','VAR','VAR','VAR','VAR','VAR')
                ]

titulos_pantalla=list(variables_titulos[0])
variables_unidades=[
    ('°C','kPa','m^3/kg','m^3/kg','kJ/kg','kJ/kg','kJ/kg','kJ/kg','kJ/kg','kJ/kg','kJ/kgK','kJ/kgK','kJ/kgK',),
    ('kPa','°C','m^3/kg','m^3/kg','kJ/kg','kJ/kg','kJ/kg','kJ/kg','kJ/kg','kJ/kg','kJ/kgK','kJ/kgK','kJ/kgK',),
    ('MPa','°C','m^3/kg','kJ/kg','kJ/kg','kJ/kgK','VAR','VAR','VAR','VAR','VAR','VAR','VAR'),
    ('MPa','°C','m^3/kg','kJ/kg','kJ/kg','kJ/kgK','VAR','VAR','VAR','VAR','VAR','VAR','VAR'),
    ('°C','kPa','m^3/kg','m^3/kg','kJ/kg','kJ/kg','kJ/kg','kJ/kg','kJ/kg','kJ/kg','kJ/kgK','kJ/kgK','kJ/kgK',),
    ('kPa','°C','m^3/kg','m^3/kg','kJ/kg','kJ/kg','kJ/kg','kJ/kg','kJ/kg','kJ/kg','kJ/kgK','kJ/kgK','kJ/kgK',),
    ('MPa','°C','m^3/kg','kJ/kg','kJ/kg','kJ/kgK','VAR','VAR','VAR','VAR','VAR','VAR','VAR')
    ]
opciones=[
        'TA-4 Agua saturada. Tabla de temperaturas', 
        'TA-5 Agua saturada. Tabla de presiones',
        'TA-6 Vapor de agua sobrecalentado',
        'TA-7 Agua líquida comprimida',
        'TA-11 Refrigerante 134a saturado. Tabla de temperatura',
        'TA-12 Refrigerante 134a saturado. Tabla de presión',
        'TA-13 Refrigerante 134a sobrecalentado'
        ]
valoresExtremos=[
        'Mínimo: 0.01°C\nMáximo: 373.95°C',
        'Mínimo: 1.0kPa\nMáximo: 22064.0kPa',
         'Mínimo: 45.81°C\nMáximo: 1300.0°C',
        'Mínimo: 0°C\nMáximo: 380.0°C',
        'Mínimo: -40.0°C\nMáximo: 100.0°C',
        'Mínimo: 60.0kPa\nMáximo: 3000.0kPa',
         'Mínimo: -36.95°C\nMáximo: 180.0°C'
        ]
valoresExtremosSecundarios=[
        'Mínimo: 0.01MPa\nMáximo: 60.0MPa',
        'Mínimo: 5.0MPa\nMáximo: 50.0MPa', 
        'Mínimo: 0.06MPa\nMáximo: 1.6MPa',
        ]
valorExtremo=valoresExtremos[0]
valorExtremosecundario=valoresExtremosSecundarios[0]
unidades=variables_unidades[0]
#variable_entrada=0.0
variable_propiedad=titulos_pantalla[0]
tabla_seleccionada=StringVar()
valoresTotales=StringVar()
#varlocal=StringVar(value="150")
varlocal=StringVar(value=0.0)   #[StringVar(),StringVar(),StringVar(),StringVar(),StringVar()]
listaLocal=["0","0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0","0"]
varlocalSecundaria=StringVar(value=0.0)#0.0
seleccion_tabla="TA-4"  #TA-4 por defecto
indice_publico=0



#########################################################################################################################################
#FRAME PRINCIPAL
#########################################################################################################################################
mainFrame=Frame(root)
mainFrame.config(bg="#323542")
mainFrame.pack()



#########################################################################################################################################
#MENÚ
#########################################################################################################################################


aviso="\n\n\n------IMPORTANTE-----\n\nEste software se encuentra en periodo de pruebas,\nen caso de encontrar algun fallo, problema o error, \nfavor de informarlo a: gustavoivanvillanueva@gmail.com"
barraMenu = Menu(root)
root.config(menu=barraMenu)
archivoMenu=Menu(barraMenu, tearoff=0)
archivoMenu.add_separator()
archivoMenu.add_command(label="Salir", command=lambda:CerrarPrograma(root))

#archivoEdicion=Menu(barraMenu, tearoff=0)
archivoHerramientas=Menu(barraMenu, tearoff=0)
#archivoHerramientas.add_command(label="Interpolador", command=lambda:aviso_Error("ERROR","Herramienta no encontrada\nFuncion por asignar\n\n"+aviso))
archivoHerramientas.add_command(label="Interpolador", command=lambda:main_interpolador())
archivoHerramientas.add_command(label="Calculadora de propiedades de mezcla", command=lambda:main_calculadora_mezcla())
archivoHerramientas.add_command(label="Calculadora de entalpía", command=lambda:main_calculadora_entalpia())

archivoAyuda=Menu(barraMenu, tearoff=0)
archivoAyuda.add_command(label="Uso del gestor", command=lambda:acercaDe("Uso del sistema","Uso del  gestor de tablas\n\n1.Elije la tabla que necesite.\n2.Ingresa el valor en el recuadro sombreado.\n3.Pulsa el boton calcular.\nNota: si no genera respuesta, quiere decir que el valor \nestá fuera del rango \n\nPara más información consulte el manual de usuario."))
archivoAyuda.add_command(label="info de tablas", command=lambda:acercaDe("Informacion","Tablas de propiedades extraidas de: \n •Çengel, Boles: Termodinámica, Octava edición, Ed Mc Graw Hill, 2014."))
archivoAyuda.add_command(label="Acerca de", command=lambda:acercaDe("Acerca de", "GESTOR DE TABLAS DE TERMODINÁMICA v0.1\n-GUI v1.0\n-Kernel v1.0\nAutor: G. Villanueva \nGithub: TabvoV/gestor-de-tablas-termodinamica\nLicencia GPL" ))


barraMenu.add_cascade(label="Archivo", menu=archivoMenu)
barraMenu.add_cascade(label="Herramientas", menu=archivoHerramientas)
barraMenu.add_cascade(label="Ayuda", menu=archivoAyuda,)



#########################################################################################################################################
#SECCIÓN DE FUNCIONES
#########################################################################################################################################


def acercaDe(titulo, texto):
    messagebox.showinfo(titulo,texto + aviso )

def aviso_Error(titulo,texto):
    messagebox.showerror(titulo, texto)


    
def seleccionMenuTabla(event):
    global seleccion_tabla
    global titulos_pantalla
    global valorExtremo
    global valorExtremosecundario
    global unidades
        
    if opciones.index(tabla_seleccionada.get()) == 1:
        #TA-5
        titulos_pantalla=list(variables_titulos[1])
        seleccion_tabla ="TA-5"
        unidades=variables_unidades[1]
        valorExtremo=valoresExtremos[1]
        
        refrescar(numeroPantallaInicial,True)

    elif opciones.index(tabla_seleccionada.get()) == 2:
        #TA-6
        titulos_pantalla=list(variables_titulos[2])
        seleccion_tabla ="TA-6"
        unidades=variables_unidades[2]
        valorExtremo=valoresExtremos[2]
        valorExtremosecundario=valoresExtremosSecundarios[0]
        refrescar(numeroPantallaInicial,False)
    
    elif opciones.index(tabla_seleccionada.get()) == 3:
        #TA-7
        titulos_pantalla=list(variables_titulos[3])
        seleccion_tabla ="TA-7"
        unidades=variables_unidades[3]
        valorExtremo=valoresExtremos[3]
        valorExtremosecundario=valoresExtremosSecundarios[1]
        refrescar(numeroPantallaInicial,False)
    
    elif opciones.index(tabla_seleccionada.get()) == 4:
        #TA-11
        titulos_pantalla=list(variables_titulos[4])
        seleccion_tabla ="TA-11"
        unidades=variables_unidades[4]
        valorExtremo=valoresExtremos[4]
        refrescar(numeroPantallaInicial,True)
    
    elif opciones.index(tabla_seleccionada.get()) == 5:
        #TA-11
        titulos_pantalla=list(variables_titulos[5])
        seleccion_tabla ="TA-12"
        unidades=variables_unidades[5]
        valorExtremo=valoresExtremos[5]
        refrescar(numeroPantallaInicial,True)

    elif opciones.index(tabla_seleccionada.get()) == 6:
        #TA-11
        titulos_pantalla=list(variables_titulos[6])
        seleccion_tabla ="TA-13"
        unidades=variables_unidades[6]
        valorExtremo=valoresExtremos[6]
        valorExtremosecundario=valoresExtremosSecundarios[2]
        refrescar(numeroPantallaInicial, False)

    else:
        #TA-4
        titulos_pantalla=list(variables_titulos[0])
        seleccion_tabla="TA-4"
        unidades=variables_unidades[0]
        valorExtremo=valoresExtremos[0]
        refrescar(numeroPantallaInicial,True)
    
    
        

def consultarMaximos():
    global valoresExtremos
    variable_propiedad=titulos_pantalla[indice_publico]
    nuevaConsulta=ConsultaTabla(0.0, seleccion_tabla, variable_propiedad, 0.0)
    valoresExtremos= nuevaConsulta.extremos()

def realizarBusqueda():
    #asignacion de variables
    variable_propiedad=titulos_pantalla[indice_publico]
    variable_entrada=float(varlocal.get())
    variable_secundaria_entrada=float(varlocalSecundaria.get())
    
    #consulta DB
    nuevaConsulta=ConsultaTabla(variable_entrada, seleccion_tabla, variable_propiedad, variable_secundaria_entrada)

    seleccion_refresco(nuevaConsulta.comprobacion())
    #print(seleccion_tabla)

def seleccion_refresco(valoresGen):
    if seleccion_tabla == "TA-6" or seleccion_tabla == "TA-7" or seleccion_tabla == "TA-13":
        refrescar(valoresGen,False)
    else: 
        refrescar(valoresGen,True)

def refrescar(Lista,Bool):
    global listaLocal
    
    if Bool: 
        #Muestra los 13 contadores
        numeroPantalla = Lista
        Cuadro1x1 =CuadroDeIngreso(2,1,titulos_pantalla[0],numeroPantalla[0],0)
        #Cuadro1x1.mostrar()
        Cuadro1x1.recuperar()
        #Cuadro1x1.selector()

        Cuadro1x2 = CuadroDeIngreso(2,2,titulos_pantalla[1],numeroPantalla[1],1)
        Cuadro1x2.mostrar()
        #Cuadro1x2.recuperar()
        #Cuadro1x2.selector()

        Cuadro1x3 = CuadroDeIngreso(2,3,titulos_pantalla[2],numeroPantalla[2],2)
        Cuadro1x3.mostrar()
        #Cuadro1x3.recuperar()
        #Cuadro1x3.selector()
        Cuadro1x4 = CuadroDeIngreso(2,4,titulos_pantalla[3],numeroPantalla[3],3)
        Cuadro1x4.mostrar()
        #Cuadro1x4.recuperar()
        #Cuadro1x4.selector()
        #Cuadro1x4.recuperar()

        Cuadro1x5 = CuadroDeIngreso(2,5,titulos_pantalla[4],numeroPantalla[4],4)
        Cuadro1x5.mostrar()

        Cuadro2x1 = CuadroDeIngreso(3,1,titulos_pantalla[5],numeroPantalla[5],5)
        Cuadro2x1.mostrar()
        Cuadro2x2 = CuadroDeIngreso(3,2,titulos_pantalla[6],numeroPantalla[6],6)
        Cuadro2x2.mostrar()
        Cuadro2x3 = CuadroDeIngreso(3,3,titulos_pantalla[7],numeroPantalla[7],7)
        Cuadro2x3.mostrar()
        Cuadro2x4 = CuadroDeIngreso(3,4,titulos_pantalla[8],numeroPantalla[8],8)
        Cuadro2x4.mostrar()
        Cuadro2x5 = CuadroDeIngreso(3,5,titulos_pantalla[9],numeroPantalla[9],9)
        Cuadro2x5.mostrar()

        Cuadro3x1 = CuadroDeIngreso(4,1,titulos_pantalla[10],numeroPantalla[10],10)
        Cuadro3x1.mostrar()
        Cuadro3x2 = CuadroDeIngreso(4,2,titulos_pantalla[11],numeroPantalla[11],11)
        Cuadro3x2.mostrar()
        Cuadro3x3 = CuadroDeIngreso(4,3,titulos_pantalla[12],numeroPantalla[12],12)
        Cuadro3x3.mostrar()
    
        listaLocal=numeroPantalla

    else:
        #muestra 6 contadores
        numeroPantalla = Lista
        Cuadro1x1 =CuadroDeIngresoVariableSecundaria(2,1,titulos_pantalla[0],numeroPantalla[0],0)
        Cuadro1x1.mostrar()
        Cuadro1x2 = CuadroDeIngreso(2,2,titulos_pantalla[1],numeroPantalla[1],1)
        #Cuadro1x2.mostrar()
        Cuadro1x2.recuperar()
        #Cuadro1x2.selector()
        Cuadro1x3 = CuadroDeIngreso(2,3,titulos_pantalla[2],numeroPantalla[2],2)
        Cuadro1x3.mostrar()
        Cuadro1x4 = CuadroDeIngreso(2,4,titulos_pantalla[3],numeroPantalla[3],3)
        Cuadro1x4.mostrar()
        #Cuadro1x4.recuperar()

        Cuadro1x5 = CuadroDeIngreso(2,5,titulos_pantalla[4],numeroPantalla[4],4)
        Cuadro1x5.mostrar()

        Cuadro2x1 = CuadroDeIngreso(3,1,titulos_pantalla[5],numeroPantalla[5],5)
        Cuadro2x1.mostrar()

        #Los siguiente no se ven
        Cuadro2x2 = CuadroDeIngreso(3,2,0,0,6)
        Cuadro2x2.noMostrar()
        Cuadro2x3 = CuadroDeIngreso(3,3,0,0,7)
        Cuadro2x3.noMostrar()
        Cuadro2x4 = CuadroDeIngreso(3,4,0,0,8)
        Cuadro2x4.noMostrar()
        Cuadro2x5 = CuadroDeIngreso(3,5,0,0,9)
        Cuadro2x5.noMostrar()

        Cuadro3x1 = CuadroDeIngreso(4,1,0,0,10)
        Cuadro3x1.noMostrar()
        Cuadro3x2 = CuadroDeIngreso(4,2,0,0,11)
        Cuadro3x2.noMostrar()
        Cuadro3x3 = CuadroDeIngreso(4,3,0,0,12)
        Cuadro3x3.noMostrar()
    
        listaLocal=numeroPantalla
 
#########################################################################################################################################
#SECCION DE OBJETOS
#########################################################################################################################################


class Botones():
    def __init__(self, row, column, titulo):
        self.__width=10
        self.row=row
        self.column=column
        self.titulo=titulo
        

    def Mostrar(self):
        botonGeneral =Button(mainFrame, text=self.titulo, width=self.__width, padx=10,  pady=10, font = ("consolas"),command=lambda:seleccion_refresco(numeroPantallaInicial))
        botonGeneral.grid(row=self.row, column=self.column, pady=20)
   
    def BotonBusqueda(self):
        botonGeneral2 =Button(mainFrame, text=self.titulo, width=self.__width, padx=10,  pady=10, font = "consolas",command=lambda:realizarBusqueda())
        botonGeneral2.grid(row=self.row, column=self.column, pady=20)


class MenuDesplegable():
    def __init__(self, row, column, opciones):
        self.row=row
        self.column=column
        self.opciones=opciones

    def mostrar(self):
        menudesplegable= ttk.Combobox(mainFrame, font = ("consolas",8), values = self.opciones,width = 60, state="readonly", textvariable = tabla_seleccionada)
        menudesplegable.grid(row=self.row, column= self.column, padx=10, pady=10, columnspan=5)
        menudesplegable.config(background="#404352", font = "consolas", justify="left")
        menudesplegable.current(0)
        menudesplegable.bind("<<ComboboxSelected>>",seleccionMenuTabla)
        
    
class CuadroDeIngreso():
    
    def __init__(self, row, column, titulo,sentencia,i):
        self.__width="20"
        self.row=row
        self.column=column
        self.titulo=titulo
        self.sentencia=StringVar(value=sentencia)
        self.index=i
        
    def mostrar(self):
        #global variable_entrada
        #global varlocal
        #varlocal=self.sentencia


        labelDeCuadro=Label(mainFrame)
        labelDeCuadro.config( background="#323542")
        labelDeCuadro.grid(row=self.row, column=self.column)

        labelTitulo =Label(labelDeCuadro, text=self.titulo+" ("+unidades[self.index]+")", font= ("consolas",12), justify ="left", bg="#323542", fg="white")
        labelTitulo.grid(row= 1, column = 1)

        cuadroDeIngreso=Entry(labelDeCuadro, width=self.__width, textvariable=self.sentencia)
        cuadroDeIngreso.config(background="#404352", font = ("consolas", 10) ,fg="white", justify="left")
        cuadroDeIngreso.grid(row=2, column=1, padx=10, pady=10)
    
    def noMostrar(self):
        labelDeCuadro=Label(mainFrame)
        labelDeCuadro.config( background="#323542", width=self.__width, height=4)
        labelDeCuadro.grid(row=self.row, column=self.column)



    def recuperar(self):
        global varlocal
        global listaLocal
        global indice_publico
        indice_publico = self.index
        self.varvar=self.sentencia
        #self.tooltipinfo= "Mínimo: "+ str(valoresExtremos[0])+ "\nMáximo: "+ str(valoresExtremos[1])
        #varlocal=self.sentencia
        

        labelDeCuadro=Label(mainFrame)
        labelDeCuadro.config( background="#5B5F74" )
        labelDeCuadro.grid(row=self.row, column=self.column)

        labelTitulo =Label(labelDeCuadro, text=self.titulo+" ("+unidades[self.index]+")", font= ("consolas",12), justify ="left", bg="#5B5F74", fg="white")
        labelTitulo.grid(row= 1, column = 1)

        

        cuadroDeIngreso=Entry(labelDeCuadro, width=self.__width, textvariable= self.varvar)#varlocal)
        cuadroDeIngreso.config(background="#404352", font = ("consolas", 10) ,fg="white", justify="left")
        cuadroDeIngreso.grid(row=2, column=1, padx=10, pady=10)
        toolinfo=CreateToolTip(cuadroDeIngreso,valorExtremo)
        #print(self.index)
        varlocal=self.varvar #varlocal[self.index]=self.varvar
        
    def selector(self):
        if float(self.varvar.get()) != float(listaLocal[self.index]):
            global indice_publico
            indice_publico=self.index
            print("anterior",listaLocal[self.index]) 
            print("actual",self.varvar.get())     
            print(titulos_pantalla[self.index], "escribe y pasa valores")
            print(indice_publico)
            
        else: 
            #varlocal = StringVar(value=listaLocal[self.index])
            print("anterior",listaLocal[self.index]) 
            print("actual",self.varvar.get())   
            print(titulos_pantalla[self.index], "NO escribe y NO pasa valores")
           

class CuadroDeIngresoVariableSecundaria():
    def __init__(self, row, column, titulo,sentencia,i):
        self.__width="20"
        self.row=row
        self.column=column
        self.titulo=titulo
        self.sentencia=StringVar(value=sentencia)
        self.index=i


    def mostrar(self):
        global varlocalSecundaria
        global indice_publico
        indice_publico = self.index
        self.varvar=self.sentencia
        #self.tooltipinfo= "Mínimo: "+ str(valoresExtremos[2])+ "\nMáximo: "+ str(valoresExtremos[3])

        #varlocal=self.sentencia
        labelDeCuadro=Label(mainFrame)
        labelDeCuadro.config( background="#5B5F74" )
        labelDeCuadro.grid(row=self.row, column=self.column)

        labelTitulo =Label(labelDeCuadro, text=self.titulo+"* ("+unidades[self.index]+")", font= ("consolas",12), justify ="left", bg="#5B5F74", fg="white")
        labelTitulo.grid(row= 1, column = 1)

        cuadroDeIngreso=Entry(labelDeCuadro, width=self.__width, textvariable= self.varvar)
        cuadroDeIngreso.config(background="#404352", font = ("consolas", 10) ,fg="white", justify="left")
        cuadroDeIngreso.grid(row=2, column=1, padx=10, pady=10)
        toolinfo=CreateToolTip(cuadroDeIngreso,valorExtremosecundario )
        varlocalSecundaria=self.varvar


#########################################################################################################################################
#GENERACIÓN DE PANTALLA ROOT
#########################################################################################################################################

menu_Tablas=MenuDesplegable(1,1,opciones)
menu_Tablas.mostrar()

BotonDeRefresco=Botones(5,2, "Refrescar")
BotonDeRefresco.Mostrar()

BotonDeBusqueda=Botones(5,4, "Búsqueda")
BotonDeBusqueda.BotonBusqueda()

refrescar(numeroPantallaInicial,True)



        
#######################################################################################################################
#SECCION DE HERRAMIENTAS
#######################################################################################################################



#FUNCION INTERPOLACION

variablesHerraminetasIniciales=[0,0,0,0,0]
varlocalHerramientas =[0,0,0,0,0] #X,x1,x0,y0,y1
resultado_interpolacion=0.0

def main_interpolador():
    global variablesHerraminetasIniciales
    global varlocalHerramientas
    global resultado_interpolacion

    rootHerramientas=Toplevel(root)
    rootHerramientas.title("Interpolador lineal")
    rootHerramientas.resizable(False,False)
    rootHerramientas.config(bg="#404353")
    rootHerramientas.iconbitmap(resolver_ruta("./Images/icono.ico"))

    varlocalHerramientas=[StringVar(),StringVar(),StringVar(),StringVar(),StringVar()]

    

    mainFrame=Frame(rootHerramientas, bg="#404353",width="500", height ="250")
    mainFrame.pack(padx=10)
    tituloLabel=Label(mainFrame,bg="#404355", text="Interpolador lineal", font=("consolas",15), fg="white")
    tituloLabel.grid(row=1, column=1,padx=20, pady=20, columnspan=10)


    def funcionBoton():
        global resultado_interpolacion

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


#FUNCION CALCULADORA DE PROPIEDADES DE VAPOR-HUMEDO (MEZCLA)


    
variablesHerraminetasInicialesMezcla=[0,0,0]
varlocalHerramientasMezclas =[0,0,0] #X,x1,x0,y0,y1
resultado_Mezclas=0.0

def main_calculadora_mezcla():
    global variablesHerraminetasInicialesMezcla
    global varlocalHerramientasMezclas
    global resultado_Mezclas

    rootMezlcas=Toplevel(root)
    rootMezlcas.title("Calculadora de propiedades de mezclas")
    rootMezlcas.resizable(False,False)
    rootMezlcas.config(bg="#404353")
    rootMezlcas.iconbitmap(resolver_ruta("./Images/icono.ico"))

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
    


#calculadora de entalpia


variablesHerraminetasInicialeEntalpia=[0,0,0,0]
varlocalHerramientasEntalpia =[0,0,0,0] #X,x1,x0,y0,y1
resultado_entalpia=0.0

def main_calculadora_entalpia():
    global variablesHerraminetasInicialeEntalpia
    global varlocalHerramientasEntalpia
    global resultado_entalpia

    rootEntalpia=Toplevel(root)
    rootEntalpia.title("Calculadora de entalpia")
    rootEntalpia.resizable(False,False)
    rootEntalpia.config(bg="#404353")
    rootEntalpia.iconbitmap(resolver_ruta("./Images/icono.ico"))

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
           # print(self.varvar.get())
        
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
    






################################################################################################
#FIN DE SECCIÓN DE HERRAMIENTAS
###############################################################################################




root.mainloop()
cerrarBase()