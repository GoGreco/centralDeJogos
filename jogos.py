import adivinhacao
import forca

print('----------------------------');
print('Bem vindo a central de jogos');
print('----------------------------');

print('Qual jogo você gostaria de jogar?');

print('1 para Adivinhação \n2 para Forca');
escolha = input('Qual jogo você escolhe? ');
jogo = int(escolha);

if(jogo == 1):
    adivinhacao.jogar();
elif(jogo == 2):
    forca.jogar();
else:
    print('Por Favor escolha 1 ou 2.')

