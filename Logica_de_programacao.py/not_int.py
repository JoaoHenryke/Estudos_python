"""
operador in(entre) e not int(não entre)
string são Iterávio (pode navegar por todos os itens)

Exemplo:

[0]  [1]  [2]  [3]  [4]  [5]  [6]  [7]  - indece positivos que a contagem começa do zero.
H     E    N    R    I    Q    U    E
[-8] [-7] [-6] [-5] [-4] [-3] [-2] [-1] - indeci negitivos não começa do zero e sim so -1.




nome = "henrique"
#print([4],[-4]) a função print não consegui imprimir com essa sintaxe dois endices simutanios, para imprimir dois indeces , precisa ser em duas funções destintas do print.
print(nome[-3])
print(nome[-2])
print("henr" in nome)
print(10*"--")
print("rique" not in nome)
print("zero" not in nome)

"""

nome = input("Digite seu nome: ")
encontra = input("Digite o que você quer encontrar: ")

if encontra in nome:
    print(f"{encontra}encontrado")
else:
    print("Não encontrado")
