import os
#Contar cuantas letras "j" o "J" hay en cualquier palabra
palabra=os.sys.argv[1]
contador=0
for x in palabra:
   if x=="j" or x=="J":
       contador+=1
       print("Son",contador,"letras")
   #Fin_if
#Fin_iterar

