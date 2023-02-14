import random;

def nomeJogo():
    print('--------------------------');
    print('Bem Vindo ao jogo de Forca');
    print('--------------------------');

def palavra_secreta():
    file = open('libraries/palavras.txt', 'r');
    palavras =[];
    for line in file:
        line = line.strip();
        palavras.append(line);
    file.close();
    numeroLinha =   random.randrange(0, len(palavras))
    segredo = palavras[numeroLinha];
    palavra = segredo.upper();
    return palavra;

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()
    
    

def jogar():

    palavra = palavra_secreta();

   
    letras_acertadas = ['_' for letra in palavra];


    enforcou = False
    acertou = False
    erros = 0;

    print('A palavra é: ', letras_acertadas)
    while(not enforcou and not acertou):
        entrada = input('escolha uma letra: ')   
        chute = entrada.upper()
        chute = chute.strip();
        
        desenha_forca(erros+1)
        
        if(chute in palavra):
            index = 0
            for letra in palavra:
                if( chute == letra):
                    letras_acertadas[index] = letra;  
                index = index + 1
            print(letras_acertadas)   
        else:
            erros +=1;
            print('Você errou.')
            print('O número de erros é: ', erros)
        acertou = "_" not in letras_acertadas
        enforcou = erros == 7;
        if(acertou == True):
            print('Parabéns, Você ganhou')
        
        if(enforcou == True):
            print('Você foi enforcado');
    





if(__name__=='__main__'):   
    jogar();