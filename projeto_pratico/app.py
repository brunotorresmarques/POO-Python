from modelos.biblioteca import Biblioteca

biblioteca1 = Biblioteca("Biblioteca Central")
biblioteca1.alterar_status()  # Ativa a biblioteca
biblioteca1.receber_avaliacao("Cliente A", 5)  # Recebe uma avaliação
biblioteca1.receber_avaliacao("Cliente B", 4)  # Recebe outra avaliação


biblioteca2 = Biblioteca("Biblioteca Comunitária")
biblioteca2.alterar_status()  # Ativa a biblioteca

# A função main() é chamada para listar todas as bibliotecas e seus status
def main():
    Biblioteca.listar_bibliotecas()

# Executa a função main() apenas se este arquivo for executado diretamente
if __name__ == "__main__":
    main()