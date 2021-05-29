def jogar():
  import random
  import time
  import os
  clear = lambda: os.system('clear')
  clear()

  print("##################################")
  print("Bem vindo ao jogo de Adivinhação!")
  print("##################################\n");
  print('\n')
  print('(1) Iniciar Jogo\n(2) Instruções\n')
  opcao = int(input('Escolha uma opção:\n')) #Convertendo a entrada de inout para int

  if(opcao == 1): # Verificando se a opção passada no input acima é verdadeira

      numero_secreto = random.randrange(1, 100, + 1) #Usando a biblioteca random.randrange onde os parâmetros são: inicio e fim da contagem randomizada 
      rodada = 1 # indicando a rodada onde o jogador se encontra
      name_player = input('Digite seu nome:\n') #Solicitando o nome do jogador
      player_points = 1000 # Passando a quantidade de pontos que o jogador terá
      print('Selecione o nivel de dificuldade:\n(1) Fácil \n(2) Médio \n(3) Díficil \n')
      dificuldade_jogo = int(input('Selecione a dificuldade:'))
      print('Bem vindo ao jogo de Adivinhação, {}, sua pontuação inicial é {}, boa sorte!'.format(name_player, player_points))
      

      if(dificuldade_jogo == 1):
          tentativas = 20
      elif(dificuldade_jogo == 2):
          tentativas = 10
      else:
          tentativas = 5
      while(player_points >= 0): #laço de repetição que define o parâmetro de pontuação do jogador
        while (rodada <= tentativas): #laço de repetição que define a quantidade de tentativas que o jogador ainda possui
            print('Tentativa {} de {} sua pontuação está com {}'.format(rodada, tentativas, player_points))
            numero_escolhido = int(input('Digite um numero: \n'))
            clear()
            acertou = numero_escolhido == numero_secreto;
            maior = numero_escolhido > numero_secreto;
            menor = numero_escolhido < numero_secreto;
            if (numero_escolhido < 1 or numero_escolhido > 100): #parâmetro condicional que define um range de limitação para o numero escolhido
                print("O numero digitado dever ser maior que 0 ou menor que 100");
                continue;
            if (acertou): 
                print("O numero digitado pelo jogador {} é: {} o numero secreto foi {} e você ficou com total de {} pontos , parabens você ganhou!".format(name_player, numero_escolhido, numero_secreto, player_points));
                break
            else:
                if (maior):
                    print("Você errou, o numero digitado foi maior que o numero secreto!");
                elif (menor):
                    print("Voce errou, o numero digitado é menor que o numero a ser adivinhado");
            rodada = rodada + 1 #parâmetro de incremento da variavel rodada que define a quantidade de tentativas do jogador
            pontos_perdidos = abs(numero_secreto - numero_escolhido) #parâmetro de decremento que define quantos pontos o jogador perdeu por erro
            player_points= player_points - pontos_perdidos
            while(rodada==tentativas):
              print('Deseja sacrificar alguns pontos seus por mais tentativas')
              print('Digite 1 para sacrificar 200 pontos e ganhar 10 chances')
              print('Digite 2 para sacrificar 100 pontos e ganhar 5 chances')
              print('Digite 3 para sair do jogo ')
              select_option = int(input('Digite sua opção: '))
              if(select_option == 1):
                tentativas = tentativas + 10
                player_points = player_points - 200
                clear()
              else:
                if(select_option==2):
                  tentativas = tentativas + 5
                  player_points = player_points - 100
                  clear()
                elif(select_option==3):
                  player_points = 0
                  break
                else:
                  print('opcao invalida')
                  time.sleep(3)
                  clear()

            if(player_points <= 0):
                break
        break

      print('Fim do Jogo, o numero secreto foi {}!'.format(numero_secreto))
  else:
    print('1 - O jogo consiste em você adivinhar o respectivo numero secreto. \n2 - O jogador pode optar por três niveis de dificuldade \n3 - Existe uma tabela de pontuação onde a cada erro sua pontuação vai diminuindo, você pode perder zerando suas tentativas ou zerando sua pontuação.\n4 - Você começa com 1000 pontos. \n5 - Existe uma logica por trás da pontuação, talvez você descubra o numero secreto, basta observar. ')
  

if(__name__=='__main__'):
    jogar()