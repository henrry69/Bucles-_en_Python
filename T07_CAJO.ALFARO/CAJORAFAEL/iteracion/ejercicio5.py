import os
cadena = os.sys.argv[1]
cadena2 = os.sys.argv[2]
cadena3 = os.sys.argv[3]
nro_letras = 0
for letra in cadena:
    print(letra)
    nro_letras +=1
    if nro_letras == 22:
        print("y ya es muy tarde")
#fin_for
print("la cadena tiene:",nro_letras)
