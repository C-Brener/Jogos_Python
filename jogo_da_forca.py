def jogar():
    import random

    mensagem_inicial()

    palavra_secreta = palavras_escondidas() #Estamos chamando a função palavra secreta e definindo-a dentro da variavel

    letras_acertadas =  iniciar_palavra_secreta(palavra_secreta)

    enforcou = False
    acertou = False
    erros = 0
    rodadas = 6

    print(letras_acertadas)

    while(not enforcou and not acertou):

        chute = solicita_chute()

        if(chute in palavra_secreta):
          contagem_correta(chute, letras_acertadas, palavra_secreta)

        else: 
          erros +=1 #Essa variavel está definida para verificar, pois caso a letra chutada não esteja dentro da palavra executara o else, por sua vez introduzirar uma numereção na variavel onde o enforcou se tornará verdadeiro quando atingir 6 erros.
          print('Você está na rodada {}, de {} tentatativas'.format(erros, rodadas))
          desenha_forca(erros)

        enforcou = erros == 6
        acertou = '_' not in letras_acertadas
        print(letras_acertadas)
        
    if(acertou):
        imprime_vencedor()
    else:
        imprime_perdedor(palavra_secreta)




###########################FUNÇÕES###############################

def mensagem_inicial():
  print("*********************************")
  print("***Bem vindo ao jogo da Forca!***")
  print("*********************************")

def palavras_escondidas():
    import random
    arquivo = open("arquivo.txt", "r")
    palavras = []
    for linha in arquivo: #fazendo a leitura do arquivo po linha
      linha = linha.strip()#cortando a separação de linhas 
      palavras.append(linha) #adicionando o resultado do for na lista
    
    arquivo.close #fechando o arquvo para nao ocorrer interferencia

    numero = random.randrange(0, len(palavras))

    palavra_secreta = palavras[numero].upper()
    return palavra_secreta # como definimos a função anteriormente no começo do codigo esse return serve para demonstrar que ela estará retornando com resultado final da execução a "palavra secreta"

def iniciar_palavra_secreta(var):
  return ["_" for letra in var] 
  # comando para transformar o espaçamento que  dinâmico de acordo com a quantidade de palavras, ou seja a cada "letra" dentro da palavra_secreta adiciona um underscore.
  #quando uma função tem como retorno uma variavel, ou executa uma ação que necessita de uma variavel externa, faz-se necvessário passar como parametro 

def solicita_chute():
    chute = input("Qual letra? ")
    chute = chute.strip().upper()
    return chute
def contagem_correta(chute, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta: #Quando a letra for achada dentro da palavra secreta executará o codigo abaixo 
        if(chute.upper() == letra.upper()): 
          letras_acertadas[index] = letra
        index +=1 # Operador de Incremento onde ele soma a propria variavel adicionando mais 1
def imprime_vencedor():

    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def imprime_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

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
          
if(__name__ == "__main__"):
    jogar()

