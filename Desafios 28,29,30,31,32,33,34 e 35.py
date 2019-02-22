# DESAFIO 28
import random

num = random.randint(0, 5)
num_chute = int
print('Pensei em um número de 0 a 5, tente advinhar!')
while num_chute != num:
    num_chute = int(input('Digite o número:'))
    if num_chute == num:
        print('Parabéns, você acertou!')
    else:
        print('Putz, você errou, tente novamente!')
print('FIM DO JOGO')

# DESAFIO 29
velocidade = float(input(print('Qual a velocidade do carro?')))
if velocidade > 80:
    print('Voce foi multado! :0')
    multa = (velocidade - 80) * 7
    print('Sua multa foi de R$ {},00'.format(multa))
else:
    print('Continue assim :)')

# DESAFIO 30
num = int(input('Digite um numero:'))
if num % 2 == 0:
    print('Este numero é par')
else:
    print('Este numero é impar')

# DESAFIO 31
distancia = float(input('Digite a distancia da viagem:'))
if distancia <= 200:
    passagem = distancia * 0.50
    print('Preço da passagem ficou em R$ {}'.format(passagem))
else:
    passagem = distancia * 0.45
    print('Preço da passagem ficou em R$ {}'.format(passagem))

# DESAFIO 32
ano = int(input('Digite um ano:'))
if (ano % 4 == 0 and (ano % 100 != 0 and ano % 400 != 0)):
    print('Este ano é bissexto')
else:
    print('Este ano não é bissexto')

# DESAFIO 33
num1 = float(input('Digite o primeiro numero:'))
num2 = float(input('Digite o segundo numero:'))
num3 = float(input('Digite o terceiro numero:'))

if num1 > num2 and num1 > num3:
    print('{} é o maior numero'.format(num1))
if num2 > num1 and num2 > num3:
    print('{} é o maior numero'.format(num2))
if num3 > num1 and num3 > num2:
    print('{} é o maior numero'.format(num3))

if num1 < num2 and num1 < num3:
    print('{} é o menor numero'.format(num1))
if num2 < num1 and num2 < num3:
    print('{} é o menor numero'.format(num2))
if num3 < num1 and num3 < num2:
    print('{} é o menor numero'.format(num3))

# DESAFIO 34
salario = float(input('Qual o valor de seu salário?'))
if salario > 1250:
    aumento = salario * 0.10
    salario = salario + aumento
    print('Seu salário foi aumentado para R$ {}'.format(salario))
else:
    aumento = salario * 0.15
    salario = salario + aumento
    print('Seu salário foi aumentado para R$ {}'.format(salario))

# DESAFIO 35
r1 = float(input('Digite o valor da 1° reta:'))
r2 = float(input('Digite o valor da 2° reta:'))
r3 = float(input('Digite o valor da 3° reta:'))

mod1 = abs(r2 - r3)
mod2 = abs(r1 - r3)
mod3 = abs(r1 - r2)

if mod1 < r1 < r2 + r3:
    if mod2 < r2 < r1 + r3:
        if mod3 < r3 < r1 + r2:
            print('Forma um triangulo')
else:
    print('Nao forma um triangulo')

