import os
#sumar los numeros pares desde 0 hasta n
n=int(os.sys.argv[1])
i=0
suma=0
while i<=n:
    if i%2==0:
        suma+=i
    i+=1
#fin_for
print("la suma es:",suma)
