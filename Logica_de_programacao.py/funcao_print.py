#função sep(separdor), tem a finalidade adcionar tipor de separadores de argumentps diferentes
#Podemos usar também somente o \n que indicará quebra de linha no sistema windows
#CRLF -> \r\n
#LF -> \n usado no sistemas operacionais windows e linux,mec.....

#ex:

print(12, 34, sep=".", end='##\r\n') # fez a junção dos 2 prints pelo comando end.
"""nesse print acima, temos comando end, que siginifica o final do print logo em sequida temos duas cerquilhas e o caracteres referente a quebra de
linha usado no sistema windows que o \r\n, nesse exemplo as cerquilhas iram aparecer no final e terá uma quebra de linha, onde os prints não ira se
juntar."""
print(12, 34,sep='-',end='\n@\n')