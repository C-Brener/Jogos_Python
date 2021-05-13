import jogo_da_forca
import adivinhacao

print('####################################')
print('########Escolha o seu jogo##########')
print('####################################\n')

print('(1)Jogo da Forca \n(2)Jogo de Adivinhação')
escolha = int(input('Qual o jogo que deseja iniciar?\n'))

if(escolha == 1):
    print('Jogando forca')
    jogo_da_forca.jogar()
else:
    print('Jogando Adivinhação')
    adivinhacao.jogar()