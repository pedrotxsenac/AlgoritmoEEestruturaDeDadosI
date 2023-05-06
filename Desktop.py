from Computador import Computador

class Desktop(Computador):
    def __init__(self, modelo, cor, preco, potenciaDaFonte):
        super().__init__(modelo, cor, preco)
        self._potenciaDaFonte = potenciaDaFonte

    def getInformacoes(self):
        return f"| Modelo: {self.modelo} | Cor: {self.cor} | Preço: {self.preco} | Potência da Fonte: {self._potenciaDaFonte} |"

    def cadastrar(self):
        print("Cadastro do Desktop realizado com sucesso.")