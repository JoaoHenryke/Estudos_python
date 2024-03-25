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
#quando far selecionar com intervalo seleionar a  mais para pegar todos os caracteres solicitados,
#.. tipo um intevalo de m / o selecina o indece 4 ferente ao m e 8 ele não pega toda a parte de mundo somente 'mund'
#.... no caso tem que colocar o numero passando nesse exemplo o 9 par apegar toda a palavras 'mundo'.

# para pegar tudo usa-se os dois pontos(:), do indeci 4 para frente.

print(variavel[4:])
print(variavel[3]) # selecionado o espaço
print(10*"-")
print(len(variavel))

print(10*"-")
print(variavel[0:9:3]) # [0(indice inicial):9[ultimo indice]:2[pular duas em duas palavras]]

#o passo pode ser tanto negativo quandto positivos, n´négativo ele vai busca os indices de trás para frente 

print(variavel[-1:-10:-1]) # nesse exemplo ele ira inverte a varialvél e fazer a busca do indece pulando um caractere