#Funciones del Gestor de tablas de termodinámica v0.1

#Autor: G. Villanueva 
#Github: Tabvov


#Funcion cerrar programa
def CerrarPrograma(valor):
    valor.destroy()


#Numero Proximo siguiente
def NumeroProximo(valor,ListaNum):
    def el_menor(ListaNum1):
        menor = ListaNum1[0]
        retorno = 0
        for x in range(len(ListaNum)):
            if ListaNum1[x]<menor:
                menor = ListaNum1[x]
                retorno = x

        return retorno

    diferencia = []
    for x in range(len(ListaNum)):
        diferencia.append(abs(valor - ListaNum[x]))
    if ListaNum[el_menor(diferencia)] <valor:
        return ListaNum[el_menor(diferencia)+1]
    else: 
        return ListaNum[el_menor(diferencia)]

#INTERPOLACIÓN 
def InterpolacionList(x, x0, x1,var0, var1):
    x=x
    y=[]
    x0=x0
    x1=x1
    var0=var0
    var1=var1

    for i in range(1,len(var0)):
        if var0.index(x0) == i: 
            y.append(x)
        else: 
            interpolacion = (var0[i] + ((var1[i] - var0[i])*(x-x0))/(x1-x0))
            y.append(interpolacion)
    return y

def Interpolacion(x, x0, x1, y0, y1):
    y = (y0 + ((y1 - y0)*(x-x0))/(x1-x0))
    return y

def calculador_mezclas(yf,yg,x):
    y=yf+x*(yg-yf)
    return y
    
def calculador_entalpia(hf_t,vf_t,P,Psat_t):
    #A presiones y temperaturas entre bajas y moderadas es posible reducir el error utilizando
    h=hf_t + vf_t*(P-Psat_t)
    return h



