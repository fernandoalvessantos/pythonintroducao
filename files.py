arquivo = open("arquivo.txt")
print(arquivo)
textocompleto = arquivo.read()
print(textocompleto)
linhas = arquivo.readlines()
print(linhas)

w = open("arquivo2.txt", "w")
w.write("meu segundo arquivo")
w.close()

w = open("arquivo.txt", "a")
w.write("nova linha no arquivo\n")
w.close()

lista = [1,2,3,4]
del lista[2:]
print(lista)
