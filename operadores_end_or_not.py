"""
Operadores lógicos
end(e) / or(ou) / not(não)

and: 
 -Todas as condições precisam ser verdadeiras.
 -Se qualquer valor for considerado falso, a expresão inteira será
 avaliada naquele valor
 -São considerados falsy(que vc já viu)
 - 0 / 0.0 / ""(string vazia) False, o interpretador para em um desses valores considerado falsy e além de para a interpretação, o python retorna o valor que foi dado com falsy
 na saida do interpretador.
  - Também exite o tipo None que é usado para representar um não valor.


entrada = input("Digite [E] entrar ou [S] sair: ")
senha_login = input('Digite sua senha de acesso: ')


senha_bd = "1234" #senha gravda no banco de dados.

if entrada == "E" and senha_login == senha_bd:
    print('Login efetivado')
else:
    print('Sair')

"""

#Avaliação de curto circuito
print(True and True and True)
print(False and False and False)
print(True and 0 and True)
print(True and 0.0 and True)
print(True and "" and True) #string 
print(True and " " and True)#string com argumento espaço


#----------------------------------------------------------------------------------------------------------
"""
 Operadores lógicos
# and (e) or (ou) not (não)
# or - Qualquer condição verdadeira avalia
# toda a expressão como verdadeira.
# Se qualquer valor for considerado verdadeiro,
# a expressão inteira será avaliada naquele valor.
# São considerados falsy (que vc já viu)
# 0 0.0 '' False
# Também existe o tipo None que é
# usado para representar um não valor

# entrada = input('[E]ntrar [S]air: ')
# senha_digitada = input('Senha: ')

# senha_permitida = '123456'

# if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
#     print('Entrar')
# else:
#     print('Sair')

# Avaliação de curto circuito
senha = input('Senha: ') or 'Sem senha'
print(senha)

"""


entrada = input("digite: [E] ou [e] para entrar [S] ou [s] para sair: s")
senha = input("digite sua senha: ")

senha_bd = "1234"
#observação, pode usar dois operadores lógicos na mesma linha de código, oberserva se ele não bagunda o metodologia usada no sistema.

# podendo usar os parenteses para poder da preferencia na leitura do código

if (entrada == "S" or entrada == "s") and senha == "1234":
    print("Entrar")
else:
    print("Sair, senha ou metado de entrar incorreto")

    