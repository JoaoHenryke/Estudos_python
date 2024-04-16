""""
 ->CONSTANTE = "Variáveis" que não vão mudar.
-> Muitas condições ao mesmo tempo if (ruim).
-> Contagem de complexidade (ruim).

"""
# As duas variaveis estão com letras menusculas pois o valor das mesmas podem ser alteradas
velocidade = 60 # velocidade atual do carro
local_carro = 100 # posição do carro na estrada


# As três variaveis abaixo com as letras maiusculas, pois os valores armazenados não seram alterados ao decorrer do código seram fixas.
RADAR_1 = 60 #  velocidade máexima do radar 1
LOCAL_1 = 101 # local onde o radar 1 está
RADAR_RANGER = 1 # A distância onde a radar pega


#exemplo de um código usando as variaveis acima ecom vairos erros de boas práticas:
""""
if velocidade > RADAR_1:
    print("Velocidade carro passou do radar")

if local_carro >= (LOCAL_1 + RADAR_RANGER) and \
local_carro <= (LOCAL_1 - RADAR_RANGER) and \
velocidade > RADAR_1:
    print("Carro multado em radar")

"""

# Exemplo usando boas práticas
# a barra envertida significa que o código vai ser continuado ná próxima linha 

vel_carro_pass_radar_1 = velocidade > RADAR_1 # a varialvel quando for chamada já será realizada o condinções que foram 
#atribuidas, e do jeito que está engolihndo palavras não está legal, o certo é ser bem explicado o nome da variavél.
carro_pasosou_radar_1 = local_carro >= (local_carro + RADAR_RANGER) and local_carro <=(local_carro - RADAR_RANGER) 
carro_multado_radar_1 = carro_pasosou_radar_1 and vel_carro_pass_radar_1
# rembrando que essas variaveis criadas e sendo atribuidos condições serão para deixar, mais limpo e de fácil enterpretação do código.


if  vel_carro_pass_radar_1:
    print("velocidade do carro passou non radar")

if carro_pasosou_radar_1:
    print("Carro passou radar 1")


if carro_multado_radar_1:
    print("Carro multado em radar 1")