import os

promedio=float(os.sys.argv[1])
print(promedio)

promedio_invalido=(promedio <0  or promedio > 20)
# Validar si el promedio del alumno es correcto
while (promedio_invalido== True):
    promedio=float(os.sys.argv[1])
    promedio_invalido = (promedio < 0 or promedio > 10)
#fin_while

print("Fin del bucle")
