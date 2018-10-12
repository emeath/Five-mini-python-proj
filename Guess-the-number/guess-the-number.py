from random import *

print('Proj 2: Guess the number!')
print('===================================')
print('O computador gera um numero inteiro de 1 a 100. Tente adivinhar o numero'
        + ' gerado pelo computador.')
print('')

loop = True #Variavel que controla a execuçao do while
adv = 0 #contagem do numero de tentativas

computer_number = randint(1, 100) # Gera o numero a ser adivinhado

while loop:
    adv += 1
    guessed_number = input("Adivinhe um numero inteiro gerado: ")

    #verifica a distancia do numero adivinhado em relacao ao numero gerado pelo computador

    if abs(guessed_number - computer_number) < 30:
        if abs(guessed_number - computer_number) < 15:
            if abs(guessed_number - computer_number) < 5:
                if guessed_number == computer_number:
                    print("Parabens! Voce ganhou!")
                    print("seu numero: " + str(guessed_number))
                    print("Numero do computador: " + str(computer_number))
                    print("numero de tentativas: " + str(adv))
                    loop = False #encerra o loop while quando o jogador acertou
                else:
                    print('mto quente...')
            else:
                print('quente...')
        else:
            print('frio...')
    else:
        print('mto frio...')


        
        
