"""Leer el nombre de 10 frutas {nombre, color, precio} para preparar un
salpicón; el programa debe permitir mostrar las 10 frutas ingresadas al 
mismo tiempo en sentido inverso al ingresado"""

print(" PROGRAMA PARA HREGISTRAR 10 FRUTAS DE SALPICON ")
fruta={}
frutas=[]
for i in range(10):
    fruta={}
    fruta['nombre']=input('Digite el nombre de la fruta: ')
    fruta['color']=input('Digite el color de la fruta: ')
    fruta['precio']=input('Digite el precio de la fruta: ')
    frutas.append(fruta)
    
for i in range(10):
    print(frutas[9-i])