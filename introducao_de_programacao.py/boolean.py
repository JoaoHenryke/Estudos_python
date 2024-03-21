"""
tipo de dado "boolean"

só existe duas respotas lógicas que o computador irá aceitar:
o "sim" ou o "não" no caso o sim(true) e não(false):
podemos usar para questionar algo em um programa
existe varios operadores lógicos para questionar:

== que indicar igualdade na programação.
> maior que
< menor que
>= maior ou igual 
<= menor ou igual
entre outros operadores lógicos que será visto mais na frente do curso.

"""

# seguir abaixo alguns exemplos:

print(10 == 10) # na saida do intrepretador ele indicará um valor true(verdadeiro).

print(10 == 6) # na saida do intrepretador ele indicará um valor false(falso).

print(10 > 7) # na saida do intrepretadir ele indicará uma valor true(verdadeiro).

print( 10 < 7) # na saida do intrepretadir ele indicará uma valor false(falsoe).

print(10 >= 5)# na saida do intrepretadir ele indicará uma valor true(verdadeiro)

print(10 <= 5)# na saida do intrepretadir ele indicará uma valor false(falso)


# podemos usar a função "type()", para indentifacar o tipo de  dado inserido:

# na saida o intrepretador indentificará as senteças abaixo como "bool"
print(10 == 10) #sentença 1º
print(type (10 == 8)) # sentença 2º

# na saida o intrepretador indentificará as senteças abaixo como "bool"
print(type(True)) #sentença 1º
print(type(False)) #sentença 2º