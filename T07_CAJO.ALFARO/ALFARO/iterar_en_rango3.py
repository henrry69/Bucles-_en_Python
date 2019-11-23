import os
#mostar cuantos numeros pares hay entre dos numeros
I=0
a=int(os.sys.argv[1])
b=int(os.sys.argv[2])
for x in range(a,b+1):
    if(x%2!=0):
        I+=1
    #Fin_if
#Fin_iterar_en _rango
print("Son",I,"numeros impares")
