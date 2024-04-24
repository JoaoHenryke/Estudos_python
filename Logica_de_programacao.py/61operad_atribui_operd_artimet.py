""""
Operadores de atribuição
= , +=, -=, *=, /=, //=, **=, %=
"""
"""
contador = 0 

while contador < 10:
    contador = contador + 1
    print(contador)
"""   



# usa a mesma lógica do exemplo acima, mais com poucas comandos.
contador = 0

contador += 10
print(contador)

# funcionna com string também mais no caso abaixc não soma e sim concatena.
contador = "1"


contador += "2"
print(contador)

# no exemplo abaixo segue o padrão de strg multiplicando comm int, a str vai repetir a quantidade 
#.... de que o int é.
contador = "@"

contador *= 10
print(contador)

#
contador = 2

contador -= 1
print(contador)


#
contador = 4
 
 # resultado de um divição normal e sempre um float.
contador /= 2
print(contador)


#
contador = 1

contador **= 2
print(contador)