"""

# Variáveis são usadas para salvar algo na memória do computador.
# pep8: incie variáveis com letras, minúsculas, pode usar
# números e underline _.
#O sinal de  "=" é o operador de atribuções. Ele é usado para
#atribuir um valor a um nome(vairével).
# Uso: nome_variavel  = expressão


"""

nome_completo = "joão henrique de sousa gomes" 
soma_dois_mais_dois = 2 + 2

print(nome_completo, "é igual á: ", soma_dois_mais_dois)

int_um = int("1") 
"""Variável chamada: "int_num" ( onde esse nome irá representar algum valor),  ""="" (sinal de atribuição), int("1") isso e 
 dado a ser gravado na vairiável int_num os seja toda que for chamado o nome dessa variável ela ira representar o dados armazenado."""

int_dois = type(int("2")) # nessa variável usa-se o mesmo ráciocinio acima.

print(int("2"), type(int("2"))) #expressão 1º

print(int_um, int_dois) #expressão 2º  
# usar a expressão 2 se tona mais banefico no código pois os se for usar muitas vezes os mesma variável bata mudar o valor da variável que onde 
#..... foi chamada a mesma mudará automatico.


nome = "joao"
idade = 25
maior_de_idade = idade >= 18

print("o senhor:", nome, "de idade =", maior_de_idade, "já consedrado adulto.")