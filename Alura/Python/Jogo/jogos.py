import forca
import adivinhacao

print("+------------------------------------+")
print("|         Escolha o seu jogo         |")
print("+------------------------------------+")

def escolhe_jogo():
    jogo = int(input("1- Forca | 2- Adivinhação | Qual jogo? "))

    if (jogo == 1):
        forca.jogar()
    elif (jogo == 2):
        adivinhacao.jogar()

if (__name__ == "__main__"):
    escolhe_jogo()