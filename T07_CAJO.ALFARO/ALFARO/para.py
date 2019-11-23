import os
#mostrar los numeros multiplos de 5 desde 1 hasta n
i=1
n=int(os.sys.argv[1])
while i<=n:
    if i%5==0:
        print(i)
    i=i+1
#Fin_for
print("fin")
