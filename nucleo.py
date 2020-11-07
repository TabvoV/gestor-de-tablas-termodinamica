#Gestor de tablas de termodinámica v0.1

#Autor: G. Villanueva 
#Github: Tabvov

import sqlite3
from Funciones import *
import os, sys

def resolver_ruta(ruta_relativa):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, ruta_relativa)
    return os.path.join(os.path.abspath('.'), ruta_relativa)


nuevaConección=sqlite3.connect(resolver_ruta("./Termodinámica_7a.db"))
nuevoCursor=nuevaConección.cursor()


class ConsultaTabla():
    def __init__(self,valor,Tablaselec, propiedad,valorSecundario):
        self.tablaTermo=Tablaselec
        self.propiedad=propiedad
        self.propiedadSecundaria="P"
        self.valor=valor
        self.valorSecundario=valorSecundario
        self.consultaSQL=""
        self.fila=()
    #    self.i=True


    
    def solicitud(self):
        #Esta funcion unicamente se usa para la funcion de probar
        print("selecciona la tabla que quieres consultar")
        print("ejemplo: TA-4")
        self.tablaTermo=input("ingresa: ").upper()

        if self.tablaTermo == "TA-6" or self.tablaTermo == "TA-7" or self.tablaTermo == "TA-13" :
            print("Ingresa el valor de ", self.propiedadSecundaria, ": ")
            self.valorSecundario=float(input("valor:"))


        print("Selecciona la propiedad:")
        print("T - Psat - vf - vg - uf - ufg - ug - hf - hfg - hg - sf - sfg - sg")
        self.propiedad=input("Seleccionar: ").upper()
        print("Ingresa el valor de la propiedad")
        self.valor=float(input("valor: "))

        print("----------------------------------------------------------------------------\n\n")

    def extremos(self):
        if  self.tablaTermo == "TA-4" or self.tablaTermo == "TA-5" or self.tablaTermo == "TA-11" or self.tablaTermo == "TA-12":
            self.consultaSQL=self.consultaSQL= " SELECT "+ self.propiedad  + " FROM `" + self.tablaTermo + "`"
            nuevoCursor.execute(self.consultaSQL)
            self.fila=nuevoCursor.fetchall()
            self.listadeFila=[i[0] for i in self.fila]
            a=[]
            a.append(min(self.listadeFila))
            a.append(max(self.listadeFila))
            print(a)
            return a
            del self.consultaSQL
            del self.fila
            del self.listadeFila
        else:
            self.consultaSQL=self.consultaSQL= " SELECT "+ self.propiedad  + " FROM `" + self.tablaTermo + "`"
            nuevoCursor.execute(self.consultaSQL)
            self.fila=nuevoCursor.fetchall()
            self.listadeFila=[i[0] for i in self.fila]
            self.listadeFila=sorted(list(set(self.listadeFila)))
            a=[]
            a.append(min(self.listadeFila))
            a.append(max(self.listadeFila))
            #print(self.propiedad)
            #print(a)
            del self.consultaSQL
            del self.fila
            del self.listadeFila

            self.consultaSQL= " SELECT "+ self.propiedadSecundaria +  " FROM `" + self.tablaTermo + "` " 
            nuevoCursor.execute(self.consultaSQL)
            self.fila=nuevoCursor.fetchall()
            self.fila=[i[0] for i in self.fila]
            a.append(min(self.fila))
            a.append(max(self.fila))
            #print(self.propiedadSecundaria)
            print(a)
            del self.consultaSQL
            del self.fila
            return a
            



            

    def comprobacion(self):
        if self.tablaTermo == "TA-4" or self.tablaTermo == "TA-5" or self.tablaTermo == "TA-11" or self.tablaTermo == "TA-12":

            #PARA TABLAS TIPO TA-4 Y TA-5

            self.consultaSQL= " SELECT "+ self.propiedad  + " FROM `" + self.tablaTermo + "`" 
            nuevoCursor.execute(self.consultaSQL)
            self.fila=nuevoCursor.fetchall()
            self.listadeFila=[i[0] for i in self.fila]

            if self.valor in self.listadeFila:
                
                #consulta sqlite
                self.consultaSQL= " SELECT *  FROM `" + self.tablaTermo + "` WHERE " + self.propiedad   +"= " + str(self.valor)
                nuevoCursor.execute(self.consultaSQL)
                self.fila=nuevoCursor.fetchall()
                self.fila=list(self.fila[0])
                self.fila=self.fila[1:]
                
                return self.fila

            else:

                self.numProx = (NumeroProximo(self.valor, self.listadeFila))
                self.indexProx =  self.listadeFila.index(NumeroProximo(self.valor, self.listadeFila))

                self.consultaSQL= " SELECT "+ self.propiedad +" FROM `" + self.tablaTermo + "` WHERE  ID=" + str(self.indexProx -1) + " OR ID= "+ str(self.indexProx)
                nuevoCursor.execute(self.consultaSQL)
                variablesxinter=nuevoCursor.fetchall()
                x0,x1 = [i[0] for i in variablesxinter]

                self.consultaSQL= " SELECT * FROM `" + self.tablaTermo + "` WHERE  ID=" + str(self.indexProx -1) + " OR ID= "+ str(self.indexProx)
                nuevoCursor.execute(self.consultaSQL)
                self.filasInterpolacion=nuevoCursor.fetchall()
                
                var0, var1 = self.filasInterpolacion
                """var0 = list(var0)
                var1 = list(var1)"""
                self.fila = InterpolacionList(self.valor, x0, x1, var0, var1)
            
                return self.fila

                
        else: 
            #PARA TABLAS DEL TIPO TA-6 TA-7 O TA-13

            self.consultaSQL= " SELECT "+ self.propiedadSecundaria  + " FROM `" + self.tablaTermo + "`" 
            nuevoCursor.execute(self.consultaSQL)
            self.fila=nuevoCursor.fetchall()
            self.listadeFila=[i[0] for i in self.fila]
            self.listadeFila=sorted(list(set(self.listadeFila)))

            if self.valorSecundario in self.listadeFila:

                #SI EL VALOR DE P ESTÁ EN LAS TABLAS
                
                self.consultaSQL= " SELECT "+ self.propiedad+  " FROM `" + self.tablaTermo + "` WHERE " + self.propiedadSecundaria   +"= " + str(self.valorSecundario)
                nuevoCursor.execute(self.consultaSQL)
                self.fila=nuevoCursor.fetchall()
                self.fila=[i[0] for i in self.fila]

                if self.valor in self.fila:

                    #SI EL DE P Y EL VALOR DE LA SEGUNDA PROPIEDAD ESTÁN EN LAS TABLAS

                    self.consultaSQL=" SELECT * FROM `" + self.tablaTermo + "` WHERE " + self.propiedadSecundaria   +"= " + str(self.valorSecundario) +" AND "+  self.propiedad +"= "+ str(self.valor)
                    nuevoCursor.execute(self.consultaSQL)
                    self.fila=nuevoCursor.fetchall()
                    self.fila=list(self.fila[0])
                    self.fila=self.fila[1:]
                    return self.fila

                else:
                    #SI EL DE P ESTÁ EN LA TABLAS Y EL VALOR DE LA SEGUNDA PROPIEDAD NO ESTÁ EN LAS TABLAS

                    self.numProx = (NumeroProximo(self.valor, self.fila))
                    self.indexProx =  self.fila.index(NumeroProximo(self.valor, self.fila))

                    self.consultaSQL = "SELECT "+self.propiedad+" FROM(select *, ROW_NUMBER() OVER(ORDER BY id) as row from `"+ self.tablaTermo+"` where "+self.propiedadSecundaria+"="+str(self.valorSecundario)+") WHERE row="+str(self.indexProx)+ " or row="+str(self.indexProx +1)
                    nuevoCursor.execute(self.consultaSQL)
                    variablesxinter=nuevoCursor.fetchall()
                    x0,x1 = [i[0] for i in variablesxinter]
                    

                    self.consultaSQL = "SELECT * FROM(select *, ROW_NUMBER() OVER(ORDER BY id) as row from `"+ self.tablaTermo+"` where "+self.propiedadSecundaria+"="+str(self.valorSecundario)+") WHERE row="+str(self.indexProx)+ " or row="+str(self.indexProx +1)
                    nuevoCursor.execute(self.consultaSQL)
                    variablesxinter=nuevoCursor.fetchall()
                    var0,var1 = variablesxinter
                    var0 = list(var0[:-1])
                    var1 = list(var1[:-1])
                    self.fila = InterpolacionList(self.valor, x0, x1, var0, var1)
                    
                    return self.fila
            
            else:
                #SI EL VALOR DE P NO ESTÁ EN LAS TABLAS
                self.numProx = (NumeroProximo(self.valorSecundario, self.listadeFila))
                self.indexProx =  self.listadeFila.index(NumeroProximo(self.valorSecundario, self.listadeFila))
                
                self.consultaSQL= " SELECT "+ self.propiedad+  " FROM `" + self.tablaTermo + "` WHERE " + self.propiedadSecundaria  +"= " + str(self.numProx)
                nuevoCursor.execute(self.consultaSQL)
                self.fila=nuevoCursor.fetchall()
                self.fila=[i[0] for i in self.fila]


                if self.valor in self.fila:

                    #SI EL VALOR DE P NO ESTÁ EN LAS TABLAS Y EL VALOR DE LA PROPIEDAD SECUNDARIA SI
                    self.consultaSQL= "SELECT * FROM `"+self.tablaTermo+"` WHERE "+self.propiedadSecundaria+"= "+str(self.listadeFila[self.indexProx -1])+" AND "+self.propiedad+"= "+str(self.valor)+" or "+self.propiedadSecundaria+"= "+str(self.listadeFila[self.indexProx])+" AND "+self.propiedad+"= "+str(self.valor)
                    nuevoCursor.execute(self.consultaSQL)
                    variablesxinter=nuevoCursor.fetchall()
                    var0,var1 = variablesxinter
                    var0 = list(var0)
                    var1 = list(var1)

                    self.fila = InterpolacionList(self.valorSecundario, self.listadeFila[self.indexProx -1], self.numProx, var0, var1)
                    return self.fila

                else:
                    #SI EL VALOR DE P NO ESTÁ EN LAS TABLAS Y EL VALOR DE LA PROPIEDAD SECUNDARIA TAMPOCO

                    #primero se encuentra el valor de las P y sus tablas aleddañas
                    self.numProx = (NumeroProximo(self.valorSecundario, self.listadeFila))
                    self.indexProx =  self.listadeFila.index(NumeroProximo(self.valorSecundario, self.listadeFila))
                    
                    Tabla_x0=self.listadeFila[self.indexProx-1]
                    Tabla_x1=self.numProx
                    
                    #luego hay que encontrar el var en cada una de las tablas
                    self.numProx = (NumeroProximo(self.valor, self.fila))
                    self.indexProx =  self.fila.index(NumeroProximo(self.valor, self.fila))
                    
                    self.consultaSQL = "SELECT "+self.propiedad+" FROM(select *, ROW_NUMBER() OVER(ORDER BY id) as row from `"+ self.tablaTermo+"` where "+self.propiedadSecundaria+"="+str(Tabla_x0)+") WHERE row="+str(self.indexProx)+ " or row="+str(self.indexProx +1)
                    nuevoCursor.execute(self.consultaSQL)
                    variablesxinter=nuevoCursor.fetchall()
                    x0,x1 = [i[0] for i in variablesxinter]

                    self.consultaSQL = "SELECT * FROM(select *, ROW_NUMBER() OVER(ORDER BY id) as row from `"+ self.tablaTermo+"` where "+self.propiedadSecundaria+"="+str(Tabla_x0)+") WHERE row="+str(self.indexProx)+ " or row="+str(self.indexProx +1)
                    nuevoCursor.execute(self.consultaSQL)
                    variablesxinter=nuevoCursor.fetchall()
                    var0,var1 = variablesxinter
                    var0 = list(var0[:-1])
                    var1 = list(var1[:-1])
                    self.fila = InterpolacionList(self.valor, x0, x1, var0, var1)
                    Fila_tabla0=self.fila

                    self.consultaSQL = "SELECT "+self.propiedad+" FROM(select *, ROW_NUMBER() OVER(ORDER BY id) as row from `"+ self.tablaTermo+"` where "+self.propiedadSecundaria+"="+str(Tabla_x1)+") WHERE row="+str(self.indexProx)+ " or row="+str(self.indexProx +1)
                    nuevoCursor.execute(self.consultaSQL)
                    variablesxinter=nuevoCursor.fetchall()
                    x0,x1 = [i[0] for i in variablesxinter]

                    self.consultaSQL = "SELECT * FROM(select *, ROW_NUMBER() OVER(ORDER BY id) as row from `"+ self.tablaTermo+"` where "+self.propiedadSecundaria+"="+str(Tabla_x1)+") WHERE row="+str(self.indexProx)+ " or row="+str(self.indexProx +1)
                    nuevoCursor.execute(self.consultaSQL)
                    variablesxinter=nuevoCursor.fetchall()
                    var0,var1 = variablesxinter
                    var0 = list(var0[:-1])
                    var1 = list(var1[:-1])
                    self.fila = InterpolacionList(self.valor, x0, x1, var0, var1)
                    Fila_tabla1=self.fila
                    
                    self.fila=[self.valorSecundario]+InterpolacionList(self.valorSecundario, Fila_tabla0[0], Fila_tabla0[1], Fila_tabla0, Fila_tabla1)
                    
                    return self.fila



def cerrarBase():
        nuevaConección.commit()
        nuevaConección.close()

#Funcion de pruebas. Esta funcion sirve para probar el programa el núcleo del programa sin GUI
def FuncionDePrueba():
    i=1
    o = True
    while o == True: 

        consulta1=ConsultaTabla(0,"","",0)
        consulta1.solicitud()
        print(consulta1.comprobacion())
        print("\n repetir consulta? 0/1")
        i=int(input())

        if i == 0:
            print("adios")
            o = False

#FuncionDePrueba()

