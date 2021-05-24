class ArvoreBin:
    def __init__(self, dado = None):
        self.__raiz = dado

    def preOrdem(self):
        self.__auxPreOrdem(self.__raiz)
    def __auxPreOrdem(self, node):
        if(node == None):
            return
        print(node)
        print()
        self.__auxPreOrdem(node.esquerda)
        self.__auxPreOrdem(node.direita)

    def ordem(self):
        self.__auxOrdem(self.__raiz)
    def __auxOrdem(self, dado):
        if(dado == None):
            return
        self.__auxOrdem(dado.esquerda)
        print(dado)
        print()
        self.__auxOrdem(dado.direita)

    def Posordem(self):
        self.__auxPosOrdem(self.__raiz)
    def __auxPosOrdem(self, dado):
        if(dado == None):
            return
        self.__auxPosOrdem(dado.esquerda)
        self.__auxPosOrdem(dado.direita)
        print(dado)
        print()

    def rotacao_esquerda(self, node):
        aux = node.direita
        node.direita = aux.esquerda
        aux.esquerda = node
        aux.balanceamento = aux.calcularBalanceamento()
        node.balanceamento = node.calcularBalanceamento()
        return aux

    def rotacao_direita(self, node):
        aux = node.esquerda
        node.esquerda = aux.direita
        aux.direita = node
        aux.balanceamento = aux.calcularBalanceamento()
        node.balanceamento = node.calcularBalanceamento()
        return aux

    def rotacao_dupla_esquerda(self, node):
        u = self.rotacao_direita(node.direita)
        node.direita = u
        v = self.rotacao_esquerda(node)
        return v

    def rotacao_dupla_direita(self, node):
        u = self.rotacao_esquerda(node.esquerda)
        node.esquerda = u
        v = self.rotacao_direita(node)
        return v


    def inserir(self, novo_node):
        self.__raiz = self.__auxInserir(novo_node, self.__raiz)

    def __auxInserir(self, novo_node, node):
        if node == None:
            if node == self.__raiz:
                self.__raiz = novo_node
            return novo_node

        assert novo_node.chave != node.chave, 'Já existe uma música com esse ID.'

        node.balanceamento = node.calcularBalanceamento()

        if novo_node.chave < node.chave:
            node.balanceamento += 1
            if node.esquerda == None:
                node.esquerda = novo_node
            else:
                node.esquerda = self.__auxInserir(novo_node, node.esquerda)

        else:
            node.balanceamento -= 1
            if node.direita == None:
                node.direita = novo_node

            else:
                node.direita = self.__auxInserir(novo_node, node.direita)

        node.balanceamento = node.calcularBalanceamento()

        if node.balanceamento > 1:
            if node.esquerda.balanceamento >= 0:
                filho_esquerdo = self.rotacao_direita(node)
            else:
                filho_esquerdo = self.rotacao_dupla_direita(node)

            node = filho_esquerdo

        elif node.balanceamento < -1:
            if node.direita.balanceamento <= 0:
                filho_direito = self.rotacao_esquerda(node)
            else:
                filho_direito = self.rotacao_dupla_esquerda(node)

            node = filho_direito

        #node.balanceamento = node.calcularBalanceamento()
        return node

    def buscarId(self, id):
        return self.__auxBuscarId(id, self.__raiz).dado

    def __auxBuscarId(self, id, node):
        if node == None or node.chave == id:
            return node

        if node.chave > id:
            node_buscado = self.__auxBuscarId(id, node.esquerda)
        else:
            node_buscado = self.__auxBuscarId(id, node.direita)

        return node_buscado

    def buscarAno(self, ano):

        return self.__auxBuscarAno(ano, self.__raiz, [])

    def __auxBuscarAno(self, ano, node, lista):
        if node == None:
            return

        if node.esquerda != None:
            lista.extend(self.__auxBuscarAno(ano, node.esquerda, []))
        if node.dado.ano == ano:
            lista.append(node.dado)
        if node.direita != None:
            lista.extend(self.__auxBuscarAno(ano, node.direita, []))

        return lista

    def listaOrdemAlfabetica(self):
        listaMusicas = []
        listaNodes = self.__lista(self.__raiz, [])
        nodesOrdenados = sorted(listaNodes, key = lambda x: x.dado.album.upper())
        for node in nodesOrdenados:
          listaMusicas.append(node.dado)
        return listaMusicas

    def __lista(self, node, lista):
        if node == None:
            return

        if node.esquerda != None:
            lista.extend(self.__lista(node.esquerda, []))
        lista.append(node)
        if node.direita != None:
            lista.extend(self.__lista(node.direita, []))

        return lista

    def alturaArvore(self):
        altura = self.__auxAlturaArvore(self.__raiz, 0)
        if altura == - 1:
            altura = 0
        return altura
    def __auxAlturaArvore(self, node, altura):
        if node == None:
            return altura-1


        altura += 1
        alturaEsq = self.__auxAlturaArvore(node.esquerda, altura)
        alturaDir = self.__auxAlturaArvore(node.direita, altura)

        return max(alturaEsq, alturaDir)

    def printArvore(self):
        altura = self.alturaArvore()
        indentLeft = 2 ** (altura+3)
        string = f'{" " * (indentLeft)}↙ {self.__raiz.chave} ↘\n'
        # string += f'{" " * ((indentLeft) - 1)}↙ ↘'
        while altura >= 0:
            altura -= 1
            string += '\n'
            linha = self.__auxPrintArvore(self.__raiz, indentLeft-(self.alturaArvore()+1), indentLeft-(2*self.alturaArvore()+1), '', altura)
            string += linha + '\n'

        print(string)

    def __auxPrintArvore(self, node, indentLeft=0,indentRight=0, string='', altura=0):
        if node == None:
            return string

        if self.alturaNode(node) == altura:
            string += f'{" " * indentLeft} ↙ {node.chave} ↘{" "*indentRight} '

        if altura == 0:
            if node.direita == None:
                string += f'{" " * (indentRight)}'
            if node.esquerda==None:
                string += f'{" " * (indentRight)}'
        string = self.__auxPrintArvore(node.esquerda,indentLeft//2,indentRight//2-4, string, altura)
        string = self.__auxPrintArvore(node.direita, indentLeft//2,indentRight//2-4, string, altura)
        return string

    def alturaNode(self, node):
        altura = self.alturaArvore()
        return self.__auxAlturaNode(self.__raiz, node, altura)

    def __auxAlturaNode(self, atual, node, altura):

        if atual == node:
            return altura

        if atual == None:
            return 0

        if atual.direita != None or atual.esquerda != None:
            altura -= 1

        return max(self.__auxAlturaNode(atual.esquerda, node, altura),
                   self.__auxAlturaNode(atual.direita, node, altura))
