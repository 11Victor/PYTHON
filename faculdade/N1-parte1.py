import random

print("Seja bem vindo a Dungeon, encontre o caminho final para vencer.\n")

sala = 1
contador = 0

while(sala != 9  and contador < 7):
    if(sala == 6):
        print("\n\nVocê está na sala: {}".format(sala))
        cor = int(input("Escolha seu caminho:\n[2] - Caminho preto\n"))
        sala = sala+2
        contador = contador+1
    elif(sala == 10):
        print("\n\nVocê entrou em um local desconhecido, sua próxima sala será sorteada!!\n")
        sala = random.randint(1,5)

        print("Você está na sala: {}".format(sala))
        cor = int(input("Escolha seu caminho:\n[1] - Caminho vermelho\n[2] - Caminho preto\n"))
        sala = sala+cor
        contador = contador+1
    else:
        print("\n\nVocê está na sala: {}".format(sala))
        cor = int(input("Escolha seu caminho:\n[1] - Caminho vermelho\n[2] - Caminho preto\n"))
        sala = sala+cor
        contador = contador+1 

if(sala == 9 and contador < 7):
    print("\n\nParabéns você GANHOU !!!!!")
else:
    print("\n\n Infelizmente você PERDEU !")