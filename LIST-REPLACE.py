
import random
S= 35
T= 50
L= 15

lista = [random.randint(S, T) for iter in range(L)]
lista.sort();
print("Elements of A: ", lista)

x = int(input("Input X : "))
for i in range (len(lista)):
    if lista[i]< x:
        lista[i]=x

print(lista)
