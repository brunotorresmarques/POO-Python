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

class GameStudio:
    def __init__(self, nome):
        self.nome = nome
        self.games = []  # Lista para armazenar os jogos do estúdio

    def adicionar_jogo(self, game):
        self.games.append(game)

    def evaluate_studio_quality(self):
        total_notes = sum(game.nota for game in self.games)
        num_games = len(self.games)
        if num_games == 0:
            print(f"O estúdio {self.nome} não possui jogos para avaliação.")
        else:
            average_quality = total_notes / num_games
            print(f"A qualidade média dos jogos do estúdio {self.nome} é: {average_quality:.2f}")

# Criando instâncias de Game
game1 = Game("The Last of Us", 2013, False, 9.5)
game2 = Game("Call of Duty: Modern Warfare", 2019, True, 8.5)
game3 = Game("God of War", 2018, False, 9.0)


# Criando uma instância de GameStudio e adicionando jogos a ele
studio = GameStudio("Naughty Dog")
studio.adicionar_jogo(game1)
studio.adicionar_jogo(game2)
studio.adicionar_jogo(game3)
studio.evaluate_studio_quality()

for game in studio.games:
    game.exibir_dados()
