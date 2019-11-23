import os
#mostrar cuantos multiplos de 3 son desde 1 hasta n
i=1
b=0
n=int(os.sys.argv[1])
while i<=n:
    if i%3==0:
        b=b+1
    i=i+1
#Fin_for
print("Son",b,"multiplos de 3")
print("fin del bucle")
