"""
Fatiamento de strings
0123456
olá mundo
-987654321
Fatiamento [i:f:p] [::] p- passos ou pulas
obs: a função ""len"" retorna a quantidade de caracteres da string
o espaço conta como caractere normal ele conta Bytes

"""

variavel = 'óla mundo'

print(variavel[4:9])
#quando for selecionar com intervalo selecionar a  mais para pegar todos os caracteres solicitados,
#.. tipo um intevalo de 4 / o selecina o indece 4 referente ao 4 a 8 ele não pega toda a parte de mundo somente 'mund'
#.... no caso tem que colocar o numero passando nesse exemplo o 9 par apegar toda a palavras 'mundo'.

# para pegar tudo usa-se os dois pontos(:), do indeci 4 para frente.

print(variavel[4:])
print(variavel[3]) # selecionado o espaço
print(10*"-")
print(len(variavel))

print(10*"-")
print(variavel[0:9:3]) # [0(indice inicial):9[ultimo indice]:3[pular três em três palavras]]

#o passo pode ser tanto negativo quandto positivos, n´négativo ele vai busca os indices de trás para frente 

print(variavel[-1:-10:-1]) # nesse exemplo ele ira inverte a varialvél e fazer a busca do indece pulando um caractere

print(len(variavel))