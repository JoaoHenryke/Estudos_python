
""""
"Exercício"
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome} /ok
        Seu nome invertido é {nome invertido} /ok
        Seu nome contém (ou não) espaços /ok
        Seu nome tem {n} letras /ok
        A primeira letra do seu nome é {letra} /ok
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."
"""

nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")


if nome:
    print(f"Seu nome é: {nome}")
    print(f"Seu nome invertido é: {nome[::-1]}")
    if ' ' in nome:
        print("Seu nome contém espaços")
    else:
        print("Seu nome não contém espaços")
    
    print(f"Seu nome contem {len(nome)} lertras")
    print("n" in nome)
    print(f"A primeira letra do  nome é: {nome[0]}")
    print(f"A ultima letra do seu nome é {nome[-1]}") #vai conta de trás para frente procurando o primeiro indice da direita para esquerda

else:
    print("Desculpe, você deixou campos vazios ")














"""
print(f"Seu nome é {nome}")
print(nome[::-1]) # para enverte o some de traz para frente.
print(" " not in nome)
print("n" in nome)
print(nome [0])
print(nome[3])
"""