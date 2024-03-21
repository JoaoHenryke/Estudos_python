'''
#LINK DO SITE DE QUESTÕES: https://www.pythonprogressivo.net/2018/02/Exercicios-Python-IF-ELIF-ELSE.html

#1º.FAÇA UM PROGRMA QUE VERIFIQUE SE UMA LETRA DIGITADO E VOGAL OI CONSOANTE.

letra = input('Digite uma letra do alfabeto: ')


if letra == 'a' or letra == 'A':
   print('vogal')

elif letra == 'e' or letra == 'E':
   print('vogal')

elif letra == 'i' or letra =='I':
   print('vogal')
  

elif letra == 'o' or letra == 'O':
   print('vogal')
   

elif letra == 'u' or letra == 'U':
   print('vogal')
  

else:
    print('consoante')


 2ª 2. Faça um programa que pede duas notas de um aluno. Em seguida ele deve calcular a média do aluno e dar o seguinte resultado:

    A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
    A mensagem "Reprovado", se a média for menor do que sete;
    A mensagem "Aprovado com Distinção", se a média for igual a dez.


nota_um = input("Digite sua primeira nota: ")

nota_dois = input("Digite sua segunda nota: ")


media = float(nota_um * nota_dois)

if media >= 7:
   print("Você está aprovado nessa diciplina")

elif media == 0:
   print("Você está aprovado com destinçã")
   
   

else:
   print("Você está reprovado nessa diciplina")
   

'''

