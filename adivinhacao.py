import random

def jogar():

    resposta = random.randrange(1, 11);2
    rodada = 1;

    #code
    print('--------------------------------');
    print('Bem vindo ao jogo de Adivinhação');
    print('--------------------------------');

    print('Por favor, escolha um nível de dificuldade: \n', '1 para Monkey \n', '2 para Fácil \n', '3 para Médio \n', '4 para Difícil \n', '5 para Impossível')

    nivel = input('O nível escolhido é: ')
    dificuldade = int(nivel)

    print('Tente adivinhar um número entre 1 e 10');

    if(dificuldade == 1):
        print(resposta);
        tentativas = 999;
    elif(dificuldade == 2):
        tentativas = 5;
    elif(dificuldade == 3):
        tentativas = 3;
    elif(dificuldade == 4):
        tentativas = 2;
    elif(dificuldade == 5):  
        tentativas = rodada;
        print('Você perdeu');
            

    while(rodada <= tentativas):
        if (dificuldade == 5):
            break;


        print ("Rodada {} de {}".format(rodada, tentativas))
        
        chute = input('Seu chute é: ' );
        numero = int(chute);

        acertou = numero == resposta;
        maior   =numero>resposta;
        menor   =numero<resposta;

            
        


        if (numero <= 0 or numero>=11):
            print('Por favor tente um número entre 1 e 10');
            continue;
        elif (acertou):
            print('Você acertou');
            break;
        else:
            rodada += 1;
            if(menor):
                print ('Você errou, seu chute foi menor do que a resposta');
            elif(maior):
                print ('Você errou, seu chute foi maior doque a resposta');
        if (rodada > tentativas):
            print('você perdeu');
if(__name__=='__main__'):
    jogar();