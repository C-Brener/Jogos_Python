def pesquisando(palpite,palavra_secreta):
  index=0
  for letra in palavra_secreta: 
      if(palpite.lower()==letra.lower()):
          print('A letra {} está na posição {}'.format(letra, index))
      index = index+1
  if(__name__=='__main__'):
        pesquisando()
