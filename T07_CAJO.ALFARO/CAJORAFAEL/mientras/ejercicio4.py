import os
area_de_la_base= int(os.sys.argv[1])
altura=  int(os.sys.argv[2])
volumen= area_de_la_base*altura
while volumen==45:
    print("el volumen es mayor")
    area_de_la_base=  int(os.sys.argv[3])
    altura= int(os.sys.argv[4])
    volumen= area_de_la_base*altura
if volumen<22:
    print("el volumen es menor")
#fin_mientras
