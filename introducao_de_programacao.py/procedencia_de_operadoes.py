"""
precedencia de operadorres aritimeticos

1º (n + n) {parentese}
2º ** {eponenciação}
3º *, /, // e % {multiplicação, divição normal, divisão com inteira e resto de divisão}
4º +, - {Soma e subtração}




obs: nos casos onde hpa varios parenteses o precedencia e do parentese mais interno para os mias externos.
"""

#Atividade ....

Aluno = "joão henrique"
peso = 97.7 
altura = 1.89
imc = peso // altura ** 2

print("O seu IMC é igaual á = ", imc)