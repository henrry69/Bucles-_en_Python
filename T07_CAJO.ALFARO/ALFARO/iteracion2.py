import os
#mostrar las letras de una palabra tomando de dos en dos
palabra=os.sys.argv[1]
contador=0
a=""
for x in palabra:
    a+=x
    contador+=1
    if contador==2:
        print(a)
        contador=0
        a=""
    #fin_if
#fin_iterar
