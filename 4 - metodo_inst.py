class Game:

    # O método __init__ é o construtor da classe, que é chamado quando um objeto é criado
    def __init__(self, nome, anoLancamento, multiplayer, nota):
        self.nome = nome
        self.anoLancamento = anoLancamento
        self.multiplayer = multiplayer
        self.nota = nota
        self.totalEvaluation = 0
        self.numEvaluations = 0

    # O método __str__ representa o objeto como uma string
    def __str__(self):
        return f"Game: {self.nome} ({self.anoLancamento})"

    def exibir_dados(self):
        print("Dados do Jogo:")
        print("Nome:", self.nome)
        print("Ano de Lançamento:", self.anoLancamento)
        print("Multiplayer:", self.multiplayer)
        print("Nota:", self.nota)

    def evaluate(self, aval):
        self.totalEvaluation += aval
        self.numEvaluations += 1

    def averageEvaluation(self):
        if self.numEvaluations == 0:
            return 0
        print(f"Média das avaliações de {self.nome}: {self.totalEvaluation / self.numEvaluations}")        


game1 = Game("The Last of Us", 2013, False, 9.5)

game1.exibir_dados()

game1.evaluate(9)
game1.evaluate(10)

game1.averageEvaluation()