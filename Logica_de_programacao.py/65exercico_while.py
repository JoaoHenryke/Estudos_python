"""
Iterando strings com while

"""
#.......01234567
#nome = "Henrique" #iteraveis
#.......76543210
#tamanho_nome = len(nome)
#print(nome)
#print([tamanho_nome])
#print(nome[3])

nome = "Henrique"

indice = 0
novo_nome = ''

while indice < len(nome):
    letra = nome[indice]
    novo_nome += f'*{letra}'
    indice += 1

print(novo_nome)