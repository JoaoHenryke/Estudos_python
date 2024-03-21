"""Formatção de estring, metado formate

a = 'A'
b = 'B'
c = 1.1

string = 'a={2} b={1} c={2:.2f}'
formato = string.format(a, b, c) # / formato_1 = 'a={} b={} c{}'.format(a, b, c)

print(formato)


nessa formatação e bem simple, consiste em criar uma variavel e nela por padrão obedece uma regra que consiste em ter uma função chamada
 de  .format(as atribuição),podendo usar as atribuições do exemplos acima, lembrando que em qeustçao de casas decimais obedece a mesma regra 
 da formatação do modelo f-string. para trabalhar com as casas decimais precisa apenas seguir o exemplo a seguir; c={:.2f}.


erro comundo quando está trabalhando com esse tipo de formatação: que quando e solicitado mais um atributo, no caso adcionando mais umas chave, o 
interpretador apresentará um erro
ex: 

a = 'A'
b = 'B'
c = 1.1

string = 'a={} b={} c={:.2f} {}' foi solicitado mais uma valor sem ter ter mais vavriais disponiveis 
formato = string.format(a, b, c) # / formato_1 = 'a={} b={} c{}'.format(a, b, c)

print(formato)

na saida do interpretador indicara o seguindo erro: Replacement index 3 'out of range' for positional args tuple

out of ranger significará que o interpretador está buscando uma coisa que não existe.

indicis:sempre começa a contagem pelo o zero:

levando em concideração o questão do indice  no exemplo acima fica da seguinte forma:  'a={0} b={1} c={2:.2f} {}'

Á variável a e determinado por conta que na contagem do indice começa pelo zero.

com isso eu tenho a possibilidade de fazer a realocação dos dodas das variáveis apenas mudando o numeração dos indices.

podendo também repetir a vairável  varias vezes, no exemplo abaixo com repetir o argumento "a" mais de uma vez.

paramentro nomeado: que podemos atribuir nomes as argumentos. dentro de alguma função nesse caso da funcção "format". 

ex: 
 a={} a={} a={} b={} c={:.2f}
"""

a = 444
b = 822 
c = 1.2

string = 'a ={nome0} b={nome1} b={nome1} c{nome1:.5f}'

formato = string.format(nome0=a,nome1=b,nome2=c)
print(formato)