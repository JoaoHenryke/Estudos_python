"""
converção de dados mais também conhecido como: coerção, type convertion, typecasting e coersion

- consiste no ato de mudar o tipo da dado para outro tipo
-Tipos imutaveis e primitivos: str, int, float e bool

(obs: concatenar segnifica "juntar")
"""
print("2", type("2")) #mostra a string e a class equivalente.

print(int("2"), type(int("2"))) # nesse modelo e realizado o aconverção da string "2" para o tipo inteiro, e mostrando a class do dado equivalente.

print(int("4")+ 2) # nesse exemplo a string 4 que está ebtre parentece e convertida para o type int.

print(float("1.50") + 1.49) #Neste exemplo temos o primeiro dados "1.50" que é uma string, fazendo a converção para float e somando com outro valor float.

print(bool(" ")) # uma sting com um valor até um espaço e true(verdadeira)

print(bool()) # uma sting vazia é considerada true(verdadeira)


print(type(int("5") + 7)) # realizando a converção da string "5" realizando a soma dando o resultado e a class type indentificadon o type de dado.