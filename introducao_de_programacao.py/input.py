# comanda input usado para coletar dados de usuários.

"""
no input qunado é solicitado dados ao usuário nessa função o resultados recebido que fica gravado na variavel é sempre um string, para recerber outro valaores os dados 
precisam ser tratado antes de serem gravados.

um exemplo da alteração do string recebida do usuário atráves do imput abaixo

num_1 = int(input("Digite um numero? "))
num_2 = int(input("Digite mais um numero?"))

soma = (num_1 + num_2)

print(f'O resultado da soma é igual á: {soma}')

# nesse caso foi relaixado o typecast(mudaça no tipo de dado de str/int), esse metado de converção nessa caso não é o mais indicado, pois existe umas peculiaridades,
pois e interessante o programador saber qual o tipo de dado que foki inserido antes de realizar o typecasting, pois se o usuário adcionar umb strg quando a linha de 
código já esta configurada para realizar o typecasting, sendo que str não pode ser convertida para inteiro, vai quebra o codigo essa procedimento. 



nome = input("Qual e o seu nome? ")

print(f"O seu nome é {nome}")



num_1 = int(input("Digite um numero? "))
num_2 = int(input("Digite mais um numero?"))

soma = (num_1 + num_2)

print(f'O resultado da soma é igual á: {soma}')

"""

num_1 = input("Digite um numero: ")

num_2 = input("Digite um numero: ")

int_num_1 = int(num_1)
int_num_2 = int(num_2)

print(f'O resultado é igual á: {int_num_1 + int_num_2}')
