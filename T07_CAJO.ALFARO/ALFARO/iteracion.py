import os
#Contar cuantas letras hay en cualquier palabra
palabra=os.sys.argv[1]
contador=0
for x in palabra:
    contador+=1
#Fin_iterar
print("Son",contador,"letras")
