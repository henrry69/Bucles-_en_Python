import os

temperatura=float(os.sys.argv[1])
print(temperatura)

temperatura_invalido=(temperatura < 38.0 or temperatura > 40.0)

# Validar si una persona tiene fiebre
while (temperatura_invalido== True):
    temperatura=float(os.sys.argv[1])
    temperatura_invalido = (temperatura < 38.0 or temperatura > 40.0)
#fin_while

print("Fin del bucle")
