"""3.Construir un programa para ir de compras en un supermercado 
que permita la construcción del siguiente MENU:
1. Digitar 1 para recibir {código, nombre, precio} de un producto 
2. Digitar 2 para mostrar todos los productos registrados 
3. Digitar 3 para permitir buscar por código un producto y editar el precio
de este 
4. Digitar 4 para permitir buscar por código un producto y eliminar el
producto 
5. Digitar 0 para SALIR"""
print("     BIENVENIDO A LA TIENDA   ")
op=1
productos=[]
while op!=0 :
    op=int(input('''elija una opcion: 
        
    1. Digitar 1 para recibir {código, nombre, precio} de un producto 
    2. Digitar 2 para mostrar todos los productos registrados 
    3. Digitar 3 para permitir buscar por código un producto y editar el precio
    de este 
    4. Digitar 4 para permitir buscar por código un producto y eliminar el
    producto 
    5. Digitar 0 para SALIR 
    : '''))
    if op ==1:
        producto={}
        producto['codigo']=input('Digite el codigo del producto: ')
        producto['nombre']=input('Digite el nombre del producto: ')
        producto['precio']=input('Digite el precio del producto: ')
        productos.append(producto)
    
    elif op ==2:
        if len(productos)>0:
                    for producto in productos:
                        print(f"El producto: {producto['nombre']} de código: {producto['codigo']} Cuesta: {producto['precio']}")
        else:
            print("el supermercado está vacio")
    elif op == 3:
        if len(productos)>0:
            c=input("Digite el codigo del producto a cambiar el precio: ")
            nv=input("Digite el nuevo valor del producto")
            for v in productos:
                if v['codigo']==c:
                    v['precio']=nv
                    print(f"el producto {v['nombre']} ahora cuesta : {nv}")
        else:
            print("el supermercado está vacio")
    elif op == 4:    
        if len(productos)>0:
            c=input("Digite el codigo del producto a ELIMINAR: ")
            i=0
            for v in productos:  
                if v['codigo']==c:
                    d=int(input(f"Desea eliminar el producto {v['nombre']} si=1 o no=0"))
                    if d==1:
                        productos.pop(i)
                        print("Producto eliminado")
                    else:
                        print("no se ha eliminado el producto")
                i+=1
        else:
            print("el supermercado está vacio")
    elif op == 5: 
        print("CERRANDO PROGRAMA..")
        op=0
    else:
        print("Digito invalido")
