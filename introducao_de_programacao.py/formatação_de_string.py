
"""
f-string

"""

nome = "joao"
altura = 1.89
peso = 96.7
imc = peso /altura ** 2

#ex: 1º
linha_0 = 'nome tem altura de altura'
'''nesse exeplo a variável está com uma string normmal, perçeba que tem os
mesmo no das variável acima mais não pode ser relacionar pois na linha
está caracterizado com string, para chamar as varias e obter o valor a elas 
relacionadas, usa-se o f-string traduzindo para o portugues formatação de 
string que é idicada com o uso da leta "F" e coloca as varias que deseja 
chamar entre chaves { }. como será mostrado no exemplo abaixo.'''

#ex: 2º

linha_1 = f'{nome} tem {altura:.2f} de altura'

"""
nesse exemplo a formatçao da string já está  em uso, assim por fora das aspas
temos  a letra f indicando formatação das string que é toda a frase, entre 
chaves temos as varias que foram atribuidado algum tipo de dado, na {altura:.2f}
esse expressão que indica que o termo está atribuido, no caso é uma valor de ponto
flutuante ou float, que  pode apresentar na saida suas casas decimais, somente duas, mas també esse valor pode 
ser maior de casas decimais.
"""

print(linha_1)
print('peso', peso,'quilos e seu imc é', )
print(imc)