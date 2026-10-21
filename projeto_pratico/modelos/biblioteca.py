class Biblioteca:
    bibliotecas = []

    def __init__(self, nome):
        self.nome = nome
        self._ativo = False
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

biblioteca1 = Biblioteca("Biblioteca Central")
biblioteca1.alterar_status()  # Ativa a biblioteca
biblioteca2 = Biblioteca("Biblioteca Comunitária")
biblioteca2.alterar_status()  # Ativa a biblioteca

Biblioteca.listar_bibliotecas()