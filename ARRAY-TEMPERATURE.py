
import random

data = (int(input("Please input data size (Max size 50): ")))
if (data > 50):
    print("Invalid size!")
    exit();
else:
    pass

n=data

start=1
stop=100
limit=n

lista = [random.randrange(start, stop) for iter in range(limit)]
lista.sort();
print("\n",lista)

hot=[h for h in lista if h>84]
print("\nNumber of hot days: ",len(hot))
pleasant=[p for p in lista if p>60 and p<84]
print("\nNumber of pleasant days: ",len(pleasant))
cold=[c for c in lista if c<60]
print("\nNumber of cold days: \n",len(cold))
