class Game:
    nome = ""
    anoLancamento = 0
    multiplayer = False
    nota = 0.0

# Primeiro Jogo
game1 = Game()
game1.nome = "The Last of Us"
game1.anoLancamento = 2013
game1.multiplayer = False
game1.nota = 9.5


print("Dados do Jogo 1:")
print("Nome:", game1.nome)
print("Ano de Lançamento:", game1.anoLancamento)
print("Multiplayer:", game1.multiplayer)
print("Nota:", game1.nota)

# Segundo Jogo
game2 = Game()
game2.nome = "Call of Duty: Modern Warfare"
game2.anoLancamento = 2019
game2.multiplayer = True
game2.nota = 8.5

print("\nDados do Jogo 2:")
print("Nome:", game2.nome)
print("Ano de Lançamento:", game2.anoLancamento)
print("Multiplayer:", game2.multiplayer)
print("Nota:", game2.nota)