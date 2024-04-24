"""
Repatições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
Break -> que é a parada forçado do código em execução
Continue -> ele interrompe a execução do codifo e volta para o começao sem salva o dados, ou seja pulando

obs: ter cuidado quando for usar um printe dentro do bloco do while depois ou antes da função break, pois depois o ultimo elemento do rapetição não efetuada e o elemnto não 
é mostrado na saída do código.

exemplo:
------------------------------------------------------------------------
i = 10

while True:
    
    if i % 2 == 0:
        break
        print(i)
    
Saida: não mostrada no terminal, pois o comando break mata o código e não mostra á saida.
----------------------------------------------------------------------------


obs:  o uso do while com o as funções break e continue será válidas para o while mais próximo.

#exemplo do uso da função continue....

contador = 0 

while contador < 100:
    contador += 1        # parte do código responsável por controlar o while.  

    if contador >=10 and contador <=30:
    #if contador == 6:
        print("Não irei mostra o ", contador) 
        continue

    print(contador)


print("-" * 20)
# uso do comando break.....
contador = 0

while contador < 100:
    contador += 1

    if contador == 50:
        break
    print(contador)

# exemplo de loop infinito...
condicao = False

while condicao:
    print("1")
    print("2")
    print("3")
    print("4")
    print("5")

exemplo 2
condicao = True

while condicao:
    nome = input('Digite seu nome: ')
    print(f'Seu nome é {nome}')

    if nome == "sair" or nome == "Sair":
        break

    print('Acabou')

"""
contador = 0

while contador <= 100:
    contador += 1
# esse if tem que vir antes do print, pois precisa valida a informação antes de salva é exibir no terminal 
    if contador == 6:
        print("pulou o numero 5",contador)
        continue

    if contador >= 20 and contador <= 35:
        print("pulou o numero ",contador)
        continue

    print(contador)


    if contador == 40:
        break

print("Acabou!")