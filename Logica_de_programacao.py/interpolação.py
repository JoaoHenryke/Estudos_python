"""
Interpolação básica de strings semelhanate ao métado f-string(de estilização da função print)
s - string 
d e i (d double e i(inteiro)) - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)
"""
nome = 'Luiz'
preco = 1000.95897643
#exemplo de interpolação na váriavel print
variavel = '%s, o preço é R$%.2f' % (nome, preco) #%s(está tendo relação com o string presente na variavél "nome", com isso essa instancia ira chamar o contéudo da váriavel para o métado print)
#uso da porcentagem e para chamar os valores depois de terfeita a correlação dos simbolos com o que será impresso e depois da untlima % antes de chamar o nomes da variasvis, soemnte coloca entre parentese se caso for mais de uma vaáriavel internpolada.
# a vairiável chamada "variavel" pode-se fazer toda a stilização da saida em uma varialvel e deposi só chamar a variavel para saida na função print
print(variavel)
print('O hexadecimal de %d é %08X' % (1500, 1500)) # uso do hexadecimal.


#Métodos de saida na função print
#f-String (o métado que eu uso)
#format
#interpolação