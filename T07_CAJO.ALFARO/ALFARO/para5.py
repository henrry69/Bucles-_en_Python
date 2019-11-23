import os
#mostar los numeros pares desde n hasta m siendo n menor que m
n=int(os.sys.argv[1])
m=int(os.sys.argv[2])
i=0
while n<m :
    if i<=m and i>=n:
        if i%2==0:
            print(i)
    i+=1
    #fin_if
#Fin_for
print("fin")
