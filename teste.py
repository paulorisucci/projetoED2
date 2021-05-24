from NodeBin import *
from catalogo import *
from arvoreBin import *



a1 = ArvoreBin()


n1 = NodeBin(Musica("A", 2009, "h", 1))
n2 = NodeBin(Musica("B", 1998, "g", 2))
n3 = NodeBin(Musica("C", 1998, "f", 3))
n4 = NodeBin(Musica("D", 1998, "e", 4))
n5 = NodeBin(Musica("E", 1998, "d", 5))
n6 = NodeBin(Musica("F", 1998, "c", 6))
n7 = NodeBin(Musica("G", 1998, "b", 7))
n8 = NodeBin(Musica("H", 1998, "a", 8))
n9 = NodeBin(Musica("H", 1998, "a", 9))
n10 = NodeBin(Musica("H", 1998, "a", 10))


a1.inserir(n1)
a1.inserir(n2)
a1.inserir(n3)
a1.inserir(n4)
a1.inserir(n5)
a1.inserir(n6)
a1.inserir(n7)
a1.inserir(n8)
a1.inserir(n9)
a1.printArvore()
#a1.inserir(n10)
#a1.preOrdem()
#print(a1.alturaNode(n4))

#a1.printarArvore()
'''
a1.inserir(n6)
a1.inserir(n1)
a1.inserir(n8)
a1.inserir(n3)
a1.inserir(n2)
a1.inserir(n7)
a1.inserir(n5)
a1.inserir(n4)
a1.inserir(n9)
a1.inserir(n10)
a1.inserir(NodeBin(Musica("H", 1998, "a", 11)))
a1.inserir(NodeBin(Musica("H", 1998, "a", 12)))
'''
'''

print('A:',n1.balanceamento)
print('B:',n2.balanceamento)
print('C:',n3.balanceamento)
print('D:',n4.balanceamento)
print('E:',n5.balanceamento)
print('F:',n6.balanceamento)
print('G:',n7.balanceamento)
print('H:',n8.balanceamento)
'''
#print(a1.altura())


#a1.preOrdem()
'''print('A:',n1.balanceamento)
print('B:',n2.balanceamento)
print('C:',n3.balanceamento)
print('D:',n4.balanceamento)
print('E:',n5.balanceamento)
print('F:',n6.balanceamento)
print('G:',n7.balanceamento)
print('H:',n8.balanceamento)


lista = a1.buscarAno(1998)

for i in lista:
    print(i)

'''
'''
l1 = a1.listaOrdem()
for l in l1:
    print(l)

'''


#a1.ordem()
#a1.preOrdem()
'''
print(n1.balanceamento)

print(n2.balanceamento)

print(n3.balanceamento)

print(n4.balanceamento)

print(n5.balanceamento)'''
'''
print('   ')
print('↙   ↘')
print('     ')
'''

#print('    a'.find('a'))