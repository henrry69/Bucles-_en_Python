import os
#Cuando se ingrese 12#%& sea contraseña correcta
contraseña=os.sys.argv[1]
contraseña_incorrecta=(contraseña!="12#%&")
while contraseña_incorrecta:
    print("Contraseña incorrecta")
    break
#Fin_while
if contraseña_incorrecta==False:
    print("contraseña correcta")
    print("iniciando sesion..")
#fin_if

