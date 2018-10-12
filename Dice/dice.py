from random import *

print('Proj 1: Dice simulator!')
print('===================================')
print('')

loop = True #flag para while loop

while loop:
    print("Rolando dado...")
    res = randint(1,6) #gera valor random inteiro entre 1 a 6
    print("Resultado: " + str(res)) 
    test = raw_input('Rolar dado novamente? (s/n): ') #le uma string do usuario - 's' rolar novamente; 'n' nao rolar; outra coisa error.
    if test == 's':
        loop = True # while loop ira continuar
    elif test == 'n':
        loop = False # encerra o loop
    else:
        # tratamento de input. Caso usuario entre com qualquer outro valor sem ser s - sim
        #ou n - nao.
        while test != 'n' and test != 's':          
            print("Input invalido Digite s/n!")
            test = raw_input('Rolar dado novamente? (s/n): ')
            if test == 'n':
                loop = False # encerra o loop