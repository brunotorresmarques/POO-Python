class Game:

    total_games = 0 # Atributo de classe para contar o número total de jogos

    # O método __init__ é o construtor da classe, que é chamado quando um objeto é criado
    def __init__(self, nome, anoLancamento, multiplayer, nota):
        self.nome = nome
        self.anoLancamento = anoLancamento
        self.multiplayer = multiplayer
        self.nota = nota

        Game.total_games += 1 # Incrementa o contador de jogos ao criar um novo objeto

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


class SinglePlayerGame(Game):
    def __init__(self, nome, anoLancamento, nota, storyLine):
        super().__init__(nome, anoLancamento, False, nota)
        self.storyLine = storyLine

    def exibir_dados(self):
        super().exibir_dados()
        print("Enredo:", self.storyLine)


multiplayer_game = Game("Call of Duty: Modern Warfare", 2019, True, 8.5)
multiplayer_game.exibir_dados()

singleplayer_game = SinglePlayerGame("The Last of Us", 2013, 9.5, "A journey of survival and hope")
singleplayer_game.exibir_dados()