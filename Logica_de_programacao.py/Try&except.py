"""
Intradução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar

numero_str = input("Digite um número: ")

if numero_str.isdigit():
    numero_str = float(numero_str)
    print(f"O dobro do número{numero_str} é {numero_str * 2:.2f}")

else:
    print("O número digitado não é inteiro.")


num1 = input("Digite um númer: ")

print(num1.isdigit())

num_converte = float(num1)

print(f"O numero digitado foi {num_converte * 2}")

"""

numero_str = input("Digite um nuúemro para dobra seu valor: ")

try:
    numero_float = float(numero_str)
    print("float:", numero_float)
    print(f"O dobro do número {numero_str}é {numero_float * 2:.1f}")
except:
    print("Isso não é um número")