import os
#mostrar cuantas tildes hay en una frase
frase=os.sys.argv[1]
contador=0
for x in frase:
    if x=="á" or x=="é" or x=="í" or x=="ó" or x=="ú":
        contador+=1
    #fin_if
print("Hay",contador,"tildes")
#fin_iterar
