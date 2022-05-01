#nome = input('Qual é o seu nome?')
#print('Prazer em te conhecer {:=^20}!'.format(nome))

n1 = int(input('Valor 1:'))
n2 = int(input('Valor2:'))
s = n1+n2
sub = n1-n2
m = n1*n2
d = n1/n2
di = n1//n2
e = n1**n2

print('A soma é {}, a subtração é {} e a multiplicação é {}'.format(s, sub, m),end=' ')
print('A divisão é {:.2f}, a divisão inteira é {} e a potência é {}.'.format(d, di, e))
#O comando {:.2f} deixa a divisão com apenas 2 casa após o ponto.
#O comando end='' faz o programa não quebrar a linha, coloca o conteúdo na mesma linha
#\n quebra a linha  e começa o programa na próxima linha.



