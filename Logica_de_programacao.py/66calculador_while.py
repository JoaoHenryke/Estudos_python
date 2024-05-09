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

    if sair is true:
        break
        
---------------------------------------------------------------------------------

forma de verificação de numero - pode usar a função isdigit() ou usar o try  / except 
para realizar essa verificação dos dados solicitados ao usuário.

[obs:  o uso do try / except é uma má pratica de programação em python.]

continui - usado para que o código não quebre, e sim da quele ponto volta para o começo do código novamnete
para começo do laço e começar a execução novamnete.
"""
while True:
    numero_1 =  input('Digite um número: ')
    numero_2 =  input('Digite outro número: ')
    operador = input('Digite o operador (+, -, /, *): ')

    numeros_validos = None
    num_1_float = 0
    num_2_float = 0

    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numeros_validos = True

    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Um ou ambos os números digitados são inválidos.')
        continue


    operador_permitidos = "+-/*"

    if operador not in operador_permitidos:
        print('operador inválido')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador.')


    print('Realizando sua conta, confira o resultado abaixo')

    if operador == "+":
        print(f"{num_1_float } + {num_2_float} =", num_1_float + num_2_float)
    elif operador == "-":
        print(f"{num_1_float } - {num_2_float} =", num_1_float - num_2_float)
    elif operador == "*":
        print(f"{num_1_float } * {num_2_float} =", num_1_float * num_2_float)
    elif operador == "/":
        print(f"{num_1_float } / {num_2_float} =", num_1_float / num_2_float)
    else:
        print("Nunca devria chegar até aqui.")
    


    sair = input('digite sair? [s]sim: ').lower().startswith('s')
    

    if sair is True:
        break