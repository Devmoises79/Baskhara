# Se o delta for maior que 0 (x > 0): haverão duas raízes
# Se o delta for igual a 0 (x == 0): haverá uma única raiz
# Se o delta for menor que 0 (x < 0): não haverá raiz real

a = float(input("Digite o coeficiente a: ")) 
b = float(input("Digite o coeficiente b: "))
c = float(input("Digite o coeficiente c:"))



delta = (b ** 2) - 4*a*c

if delta < 0:
    print("Não há raízes reais.")
elif delta == 0:
    x1 = (-b + delta ** 0.5) / (2*a)
    print("Há uma raíz única: ",x1)
else : 
    x1 = (-b + delta ** 0.5) / (2*a)
    x2 = (-b - delta ** 0.5) / (2*a)
    print("Primeira raiz : ",x1)
    print("Segunda raiz : ",x2)

    