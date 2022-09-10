n=int(input("Digite cuantos numeros desea registrar: "))
m2=0
m3=0
for i in range(n):
    v=int(input('Digite un numero a almacenar'))
    if v%2==0:
       m2+=1
    elif v%3==0:
        m3+=1;
print(f"La cantidad de multiplos de 2 es: {m2} y de 3 es: {m3}")