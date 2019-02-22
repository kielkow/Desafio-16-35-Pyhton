#EXERCICIO 16
import math
num = float(input('Digite um numero:'))
partInt = math.trunc(num)
print(partInt)

#EXERCICIO 17
import math
catOposto = float(input('Digite o valor do cateto oposto:'))
catAdj = float(input('Digite o valor do cateto adjacente:'))
hip = math.sqrt(pow(catOposto,2) + pow(catAdj,2))
print('A hipotenusa é igual a {}'.format(hip))

#EXERCICIO 18
import math
angulo = float(input('Digite o angulo:'))
cos_angulo = math.cos(angulo)
sin_angulo = math.sin(angulo)
tan_angulo = math.tan(angulo)
print('O cosseno de {} é {:.4f}, o seno é {:.4f} e a tangente é {:.4f} '.format(angulo,cos_angulo,sin_angulo,tan_angulo))

#EXERCICIO 19
import random
al1 = input('Digite o nome do primeiro aluno:')
al2 = input('Digite o nome do segundo aluno:')
al3 = input('Digite o nome do terceiro aluno:')
al4 = input('Digite o nome do quarto aluno:')
sorteado = random.randint(1,4)
if sorteado == 1:
  print(al1)
if sorteado == 2:
  print(al2)
if sorteado == 3:
  print(al3)
if sorteado == 4:
  print(al4)

#EXERCICIO 20
import random
al1 = input('Digite o nome do primeiro aluno:')
al2 = input('Digite o nome do segundo aluno:')
al3 = input('Digite o nome do terceiro aluno:')
al4 = input('Digite o nome do quarto aluno:')
ordem = random.sample([al1, al2, al3, al4], 4)
print(ordem)

#EXERCICIO 21
import pygame
pygame.init()
pygame.mixer.music.load('musica.mp3')
pygame.mixer.music.play()
pygame.event.wait()

