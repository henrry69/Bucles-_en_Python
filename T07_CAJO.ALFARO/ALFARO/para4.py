import os
#mostar el numero de numeros pares desde 0 hasta n
n=0
i=0
a=int(os.sys.argv[1])
while i<=a:
  if i%2==0:
    n+=1
  i+=1
#Fin_for
print("Son",n,"numeros pares")
