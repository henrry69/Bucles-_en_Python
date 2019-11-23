import os
num_informe = os.sys.argv[1]
nro_errores = 0
for error in num_informe:
    print(error)
    nro_errores +=1
    if nro_errores == 19:
        print("en el informe 2 tiene errores")
#fin_for
print("en numero de errores es:",nro_errores, "errores")
