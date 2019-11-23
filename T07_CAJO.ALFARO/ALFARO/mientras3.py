import os
#Mostrar si se puede comprar un objeto ingresando el dinero con el que cuenta y el precio del producto
dinero=float(os.sys.argv[1])
precio=float(os.sys.argv[2])
#validar el dinero y el precio existan
validar_dinero=(dinero>=0)
validar_precio=(precio>=0)
se_puede_comprar=(dinero>=precio)
vuelto=dinero-precio
faltaria=precio-dinero
while (validar_dinero and validar_precio):
    se_puede_comprar==True
    print("Su compra ha sido realizada con exito")
    print("Tu vuelto es",vuelto)
    break
#fin_while
if se_puede_comprar==False:
    print("no puede realizar su compra, le falta",faltaria)
#fin_if
