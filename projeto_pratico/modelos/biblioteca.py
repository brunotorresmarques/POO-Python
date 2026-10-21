from modelos.avaliacao import Avaliacao

class Biblioteca:
    bibliotecas = []

    def __init__(self, nome):
        self.nome = nome
        self._ativo = False
        self.avaliacoes = []  # Lista para armazenar avaliações da biblioteca
        Biblioteca.bibliotecas.append(self)

    def __str__(self):
        return f"Biblioteca: {self.nome}"

    @classmethod # Método de classe para listar todas as bibliotecas
    def listar_bibliotecas(cls):
        print(f"{'Nome da Biblioteca'.ljust(30)} | {'Status'}")
        print("-" * 45)
        for biblioteca in Biblioteca.bibliotecas:
            print(f"{biblioteca.nome.ljust(30)} | {biblioteca.ativo}")

    # Setter para o atributo _ativo
    def alterar_status(self):
        self._ativo = not self._ativo

    # Getter para o atributo _ativo
    @property
    def ativo(self):
        return "Ativada" if self._ativo else "Desativada"

    def receber_avaliacao(self, cliente, nota):
        """Recebe uma avaliação de um cliente e adiciona à lista de avaliações."""
        avaliacao = Avaliacao(cliente, nota)
        self.avaliacoes.append(avaliacao)

