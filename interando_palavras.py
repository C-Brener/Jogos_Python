def pesquisando(palavra_secreta,palpite):
  index=0
  for letra in palavra_secreta: 
      if palpite==letra:
          print('A letra {} está na posição {}'.format(letra, index))
      index = index+1
  if(__name__=='__main__'):
        pesquisando()
