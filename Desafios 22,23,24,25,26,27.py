#EXERCICIO 22
nome = input('Digite seu nome inteiro:')
nome = nome.upper()
print(nome)
nome = nome.lower()
print(nome)
print(len(nome.split(' ')[0]))
nome = ''.join(nome.split())
print(len(nome))

#EXERCICIO 23
num = input('Digite um numero de 0 a 9999:')
print('Milhar:{}' .format(num[0:1]))
print('Centena:{}' .format(num[1:2]))
print('Dezena:{}' .format(num[2:3]))
print('Unidade:{}' .format(num[3:4]))

num = input('Digite um numero de 0 a 9999:')
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print('Unidade = {}'.format(u))
print('Dezena = {}'.format(d))
print('Centena = {}'.format(c))
print('Milhar = {}'.format(m))

#EXERCICIO 24
cidade = input('Digite o nome da cidade:')
cidade.split()
if(cidade.split(' ')[0] == 'Santo'):
  print('Sua cidade começa com o nome Santo')
else:
  print('Sua cidade não começa com o nome Santo')

#EXERCICIO 25
nome = input('Digite seu nome inteiro:')
if nome.count('Silva') >= 1:
  print('Você possui Silva em seu nome')
else:
  print('Você não possui Silva em seu nome')

#EXERCICIO 26
frase = input('Digite uma frase:')
print(frase.count('a'))
print(frase.find('a'))
print(frase.rfind('a'))

#EXERCICIO 27
nome = input('Digite seu nome inteiro:')
print(nome.split(' ')[0])
print(nome.split(' ')[-1])



