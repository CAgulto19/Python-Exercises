
x=int(input("X is: \n"))

ALPHA=[x]*50
tf=ALPHA[:25]
ff=ALPHA[25:]

tf = [a * x for a in tf]
ff = [b * 3 for b in ff]
com= tf+ff

print(com[:10])
print(com[10:20])
print(com[20:30])
print(com[30:40])
print(com[40:50])
