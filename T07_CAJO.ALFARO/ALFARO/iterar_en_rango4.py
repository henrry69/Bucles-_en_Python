import os
#Mostar cuantos numeros multiplos de 7 hay entre dos numeros
I=0
a=int(os.sys.argv[1])
b=int(os.sys.argv[2])
for x in range(a,b+1):
    if(x%7==0):
        I+=1
    #Fin_if
#Fin_iterar_en _rango
print("Son",I,"multiplos de 7")
