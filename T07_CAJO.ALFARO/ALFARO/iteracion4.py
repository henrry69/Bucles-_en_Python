import os
#determinar cuantos signos de puntuacion hay en un texto
frase=os.sys.argv[1]
contador=0
for x in frase:
    if x=="." or x=="," or x==";":
        contador+=1
    #fin_if
print("hay",contador,"signos de puntuacion")
#fin_iterar
