import os
#sumar todos los numeros pares que hay entre a y b sabiendo que a>b
a=int(os.sys.argv[1])
b=int(os.sys.argv[2])
c=0
for i in range(a,b+1):
    if(i%2==0):
        c+=i
        print(c)
    #Fin_if
#Fin_iterar_en _rango
print("fin")
