"""
Formatação básica de strings
s - string
d - string
f - float
<número de dígitos>f
x OU X - Hexadecimal
(caractere)(><^)(quantidade)
 = - Força o número a aparecer antes dos zeros
> - Esquerda
< - Direita
^ - Centro
Sinal - + ou -
Ex: 0 > -100,.1f
conversion flags - !r(_repr_) !s(_str) !a(_)

"""
#pad - lurgura fixa na vairalvel, quando ela não atinge seu limete de caractere
# pode fazer o preenchimento.
variavel = "ABC"
print(f"{variavel}")
print(10 * "---")

#função pad
print(f"{variavel:@>10}") # nesse exemplo será colocado 10 espaços do lado esquerdo do resultado da saida

print(10*"---")
print(f"{variavel:a<10}.") # nesse exemplo será colocado 10 espaçamento de prencgimento do lado Direita do resultado da saida

print(10 * "-")
print(f"{variavel:$^10}.") # nesse exemplo será colocado 10 espaçamento de prencgimento do lado Direita e da esquerda  do resultado da saida
# com o uso do sifram os espaços iram ser prenechido pelo sifram ou qualquer outro caractere que for escolhido.print(f"{variavel:$^10}.")
print(f"{variavel:0^10}.")
print(10*"-")


print(f"{-100.455864646846848:+,.1f}")

print("O hexadecimal de 1500 é{1500:08x}")#uso do exadecimal