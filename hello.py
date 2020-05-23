print("Hello World")
var1 = 1
var2 = 2.2  # float
var3 = "String"
var4 = True
print(var1)
print(var2)
print(var3)
print(var4)

if var2 == var1:
    print("var 2 igual var 1")
elif var1 < var2:
    print("var 1 menor que var2")
elif var2 > var2:
    print("var 2 maior que var 1")
else:
    print("numero diferente")

lista = [1, 2, 3, 4, 5]
lista = [0, "txt", 0.2, True]

for i in range(10):
    print(i)
for i in range(10, 20):
    print(i)
for i in range(20, 30, 2):
    print(i)
