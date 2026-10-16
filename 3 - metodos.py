class Game:

    # O método __init__ é o construtor da classe, que é chamado quando um objeto é criado
    def __init__(self, nome, anoLancamento, multiplayer, nota):
        self.nome = nome
        self.anoLancamento = anoLancamento
        self.multiplayer = multiplayer
        self.nota = nota

    # O método __str__ representa o objeto como uma string
    def __str__(self):
        return f"Game: {self.nome} ({self.anoLancamento})"


game1 = Game("The Last of Us", 2013, False, 9.5)

print(game1)