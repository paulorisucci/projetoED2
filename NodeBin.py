class NodeBin:
    def __init__(self, dado):
        self.__esquerda = None
        self.__direita = None
        self.__dado = dado
        self.__chave = self.__dado.id
        self.__balanceamento = 0

    @property
    def esquerda(self):
        return self.__esquerda
    @esquerda.setter
    def esquerda(self, nova_esquerda):
        self.__esquerda = nova_esquerda

    @property
    def direita(self):
        return self.__direita
    @direita.setter
    def direita(self, nova_direita):
        self.__direita = nova_direita

    @property
    def dado(self):
        return self.__dado
    @dado.setter
    def dado(self, novo_dado):
        self.__dado = novo_dado

    @property
    def chave(self):
        return self.__chave
    @chave.setter
    def chave(self, nova_chave):
        self.__chave = nova_chave

    @property
    def balanceamento(self):
        return self.__balanceamento
    @balanceamento.setter
    def balanceamento(self, novo_balanceamento):
        self.__balanceamento = novo_balanceamento

    def calcularBalanceamento(self):
        return self.__auxCalcularBalanceamento(self, 0)

    def __auxCalcularBalanceamento(self, dado, balanceamento):
        if dado == None:
            return balanceamento

        FB_esquerdo = self.profundidade(dado.esquerda, balanceamento)
        FB_direito = self.profundidade(dado.direita, balanceamento)

        return FB_esquerdo - FB_direito

    def profundidade(self, dado, fator):
        if dado == None:
            return fator - 1
        fator_esquerdo = self.profundidade(dado.esquerda, fator+1)
        fator_direito = self.profundidade(dado.direita, fator+1)

        return max(fator_esquerdo, fator_direito)



    def __str__(self):
        return f'{self.__dado}'