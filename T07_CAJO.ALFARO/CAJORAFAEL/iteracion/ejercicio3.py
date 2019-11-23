import os
tipos_de_aros = os.sys.argv[1]
nro_aro = 0
for aro in tipos_de_aros:
    print(aro)
    nro_aro +=1
    if nro_aro <3.5:
        print("aro incorrecto")
#fin_for
print("los tipos son:",nro_aro)
