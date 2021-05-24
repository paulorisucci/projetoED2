
from NodeBin import *
from catalogo import *
from arvoreBin import *

div = '==========='


loop = True
while loop == True:
  print(f'''[MENU]
  (1) Inserir música 
  (2) Buscar música pelo id 
  (3) Buscar músicas pelo ano  
  (4) Listar músicas em ordem alfabética  
  (5) Altura da árvore  
  (6) Exibir a árvore 
  (7) Sair do programa.
  ''')
  select = input('Número: ')

  #Inserir música 
  if select == '1':
    print('[Inserindo música]')
    try:
      nome = input('Nome: ')
      ano = int(input('Ano: '))
      album = input('Álbum: ')
      iden = int(input('Coloque o identificador desejado: '))
      print('')
      m1 = Musica(nome, ano, album, iden) # Musica -> NodeBin -> ArvoreBin
      arvore.inserir(NodeBin(m1))  # arvore = ArvoreBin(NodeBin(Musica()))
    except AssertionError as AE:
      print(AE)
    except Exception as EXC:
      print(EXC)
  #Buscar música pelo id 
  elif select == '2':
    try:
      print('[Buscando música (ID)]')
      iden = int(input('Coloque o identificador desejado: '))
      m = arvore.buscarId(iden)
      print(div)
      print(m)
      print(div)
    except Exception as AE:
      print(AE)



  #Buscar músicas pelo ano 
  elif select == '3':
    print('[Buscando música (ANO)]')
    try:
      ano = int(input('Ano desejado: '))
      m = arvore.buscarAno(ano)
      print(div)
      for i in m:
        print(i)
      print(div)
    except Exception as AE:
      print(AE)
  #Listar músicas em ordem alfabética
  elif select == '4':
    print('[Listando músicas (ORDEM ALFABÉTICA)]')
    lista = arvore.listaOrdemAlfabetica()
    print(div)
    for i in range(len(lista)):
      if i == len(lista)-1:
        print(f'{lista[i].nome}.')
      else:
        print(f'{lista[i].nome},')
    print(div)

  #Altura da árvore 
  elif select == '5':
    print('[Altura da árvore]')
    alt = arvore.alturaArvore()
    print(div)
    print(f'Altura: {alt}')
    print(div)

  #Exibir a árvore
  elif select == '6':
    try:
      arvore.printArvore()
    except AssertionError as AE:
      print(AE)
    pass

  #Sair do programa
  elif select == '7':
    loop = False
  
print('DESLIGANDO PROGRAMA...')
ok = input('ENTER PARA SAIR! ')


