import os
#pedir la edad de una persona y determinar si es mayor de edad
edad=int(os.sys.argv[1])
edad_valida=(edad>0 and edad<=110)
while edad_valida:
    a=(edad>=18)
    print("es mayor de edad")
    break
#fin_while
