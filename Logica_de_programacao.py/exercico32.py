"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

numero_inteiro = input("Digite um número inteiro: ") # solicitando os dados do usuário


if numero_inteiro.isdigit(): # verificação dos dados solicitados, no caso se são strings para validar e dar continuidade no código
  
        if numero_inteiro % 2 == 0: # realizando a divição com resto.
             
             print(f"O número {numero_inteiro} é par")
        else:
             print(f"O número {numero_inteiro} é impar")

else:
    print("Erro, o que foi digitado não equivale a números inteiro.")







"""
num = input("Digite um número: ")

num_int = int(num)

if num_int % 2 == 0:
    print("O número é par")
else:
    print("O número é impar")

 outra forma de fazer:


try:

numero_inteiro1 = int(input("Digite aqui um número inteiro"))

if numero_inteiro1 % 2 ==o:
    print("O número digitador é par")
else:
    print("O número digitado é ímpar")

except ValueError:
print("Erro: valores digitados não especificados a um número inteiro")
     
"""


"""
Faça um programa que exige a hora ao usuário e, baseando-se no horário
descrito, exiba a saudação correspondente. Ex.
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
"""  
hora = int(input("Digite a hora atual: "))

if 0 <= hora <=12:
    print(f"Bom dia!, são extamente {hora} hora")
elif 13 <= hora <= 17:
  print(f"Boa tarde!, são extamente {hora} hora")

elif 18 <= hora <= 24:
   print(f"Boa noiete!, são exatamente {hora}") 

else:
   print("Erro!")
"""
   
"""
Faça um programa que parte do primeiro nome do usuário. Se o nome tiver 4 letras ou
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva
“Seu nome é normal”; maior que 6 escreva "Seu nome é muito grande".

#Se o nome tiver 4 letras ou menos escreva " Seu nome é curto ";

#Se tiver entre 5 e 6 letras, escreva "_Seu nome é norma_l";

#Maior que 6 escreva " Seu nome é muito grande ".

nome = input("Digite seu primeiro nome: ")

if nome.isalpha():
    try:
        if len(nome) <= 4:
            print("seu nome é muito piqueno")
        elif len(nome) <=6:
            print("Seu nome é normal")
        else:
            print("Seu nome é grande")
    except:
        print("Erro, você não digitou uma palavra")
else:
    print("Você digitou um nome inválido.")

"""