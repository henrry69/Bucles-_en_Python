import os
#mostrar "es par" cuando sea multiplo de dos y "es impar" cuando no
numero1=int(os.sys.argv[1])
modulo=numero1%2
multiplo=(modulo==0)
while multiplo:
    print("es par")
    break
#fin_while
if multiplo==False:
    print("es impar")
#fin_if
