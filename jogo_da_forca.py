def jogar():
    import interando_palavras
    print("##################################")
    print("Bem vindo ao jogo de Adivinhação!")
    print("##################################\n")

    palavra_secreta = ('laranja')
    enforcou = False
    acertou = False
    while(not enforcou and not acertou):
      contagem = len(palavra_secreta)
      print('A palavra secreta possui {} letras'.format(contagem))
      palpite = input('Digite uma letra:').lower()
      interando_palavras.pesquisando(palavra_secreta,palpite)
    print('Continue Jogando')

if(__name__ == '__main__'):
        jogar()