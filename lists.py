x = [1,2,3,4,5]
y = [i**2 for i in x]
print(x)
print(y)
z = [i for i in x if i%2==1]
print(z)

lista = ["abacate", "bola", "cachorro", "dinheiro", "elefante"]
for i, nome in enumerate(lista):
    print(i,nome)

def dobro(x):
    return x*2

valor = 2
print(dobro(valor))

valordobrado =map(dobro, x)
valordobrado = list(valordobrado)
print(valordobrado)

from functools import reduce
def soma(x,y):
    return x+y
vs = reduce(soma, x)
print(vs)

for numero, nome in zip(x, lista):
    print(numero, nome)

