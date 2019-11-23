import os
apellido = os.sys.argv[1]
nro_letras = 0
for letra in apellido:
    print(letra)
    nro_letras +=1
    if nro_letras == 11:
        print("bien")
#fin_for
print("el nombre tiene:",nro_letras)
