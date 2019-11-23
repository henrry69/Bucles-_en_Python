import os

sobre_peso=int(os.sys.argv[1])
print(sobre_peso)

peso_invalido=(sobre_peso < 120 or sobre_peso > 300)

# Validar si una persona tiene sobre peso
while (peso_invalido== True):
    sobre_peso=int(os.sys.argv[1])
    peso_invalido = (sobre_peso < 100 or sobre_peso >300)
#fin_while

print("persona con sobre peso")
