'''
epetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim

'''

'''
#exemplo 1:

contador = 0

while contador < 10:

    contador = contador + 1
    print('Contador')

print('Acabou')

#nesse exemplo não aparece os numeros somente o conteudo do função print enquanto a função while for true e por conta da lógica usada.


contador = 0 

while contador <= 10:
    print(contador)
    contador = contador + 1

print("Acabou!")
# nesse exemplo aparece a seguencia de números que são impressos e passam pelo while, sendo que será impresso somente de 0 a 9 caso não tenho o operador lógico "<=".
'''

i = 10

while True:
    
    if i % 2 == 0:
        break
        print(i)
       