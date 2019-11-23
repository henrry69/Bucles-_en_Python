import os
#llamar a 993457801
telefono=993457801
telefono_ingresado=int(os.sys.argv[1])
#telefono incorrecto cuando el telefono sea diferente de telefono ingresado
telefono_incorrecto=(telefono!= telefono_ingresado)
while telefono_incorrecto:
    print("Telefono incorrecto")
    break
#fin_while
if telefono_incorrecto==False:
     print("Esta llamando...")
#fin_if

