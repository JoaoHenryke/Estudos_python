""" 
Calculadora em while 

2 variaveis com o mesmo nome

exemplo:
 while True:
    sair = input('quer sair? [s]sim')
    sair = 'henrique'
    print(sair)

    isso sigifica que quando for da a sair o que vai aparecer será o contéudo
    do ultima variavél, pois ela será reatribuida o valor que sera a str='henrique'

    função - lower() = no caso abaixo o função irá converte a palavras digitadas e maiuculas,
    retornando para lowercase(menusculas). obs: retorna outra string.

    função - que indentifican  a letra inicial e final para formula uma regra em python.

    startswith() - inicia com.
    endswith() - termica com.

# metodo lower() - letras minusculas.
while True:
retorna um str   sair = input('quer sair? [s]sim: ')
retorna um str  sair = sair.lower() # transforma as palavras maiusculas coletadas pelo input em minusculas. 
retornar um bool   sair = sair.startswith('s') # verifica se a primeira letra é um 's'e retorna um valor bool (treu or false)
gual a bool print(sair)

nesse caso como a utlima variavel ira substituir a variavel antecesorá, com o fançao startschit irá retorna 
um bool, terá conflito de tipagem, pois começa em str e termina em bool.

solução: determinar as funções em somente uma linha para retorna tudo em bool.
    or

    while True:
    input('Digite sair? [s]sim: ').lower().startswith('s')
    print(sair)

"""
while True:
    sair = input('digite sair? [s]sim: ').lower().startswith('s')
    print(sair)