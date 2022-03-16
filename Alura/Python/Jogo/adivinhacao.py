import random
import jogos

def jogar():
    print("+------------------------------------+")
    print("|  Bem vindo no jogo de Adivinhação  |")
    print("+------------------------------------+")

    numero_secreto = random.randrange(1,101)
    total_tentativas = 0
    pontos = 1000

    nivel= int(input("""Qual o nível de dificuldade?
    1- Fácil
    2- Média
    3- Difícil: """))

    if nivel == 1:
        total_tentativas = 10
    elif nivel == 2:
        total_tentativas = 5
    elif nivel == 3:
        total_tentativas = 3

    for rodada in range (1, total_tentativas+1):
        print("Tentativa {} de {}".format(rodada, total_tentativas))
        numero_usuario = int(input("Informe um número entre 1 e 100: "))
        print("Você digitou", str(numero_usuario) + ".")

        if numero_usuario < 1 or numero_usuario > 100:
            print("Você deve digitar um número entre 1 e 100!")
            continue

        acertou = numero_secreto == numero_usuario
        maior = numero_usuario > numero_secreto
        menor = numero_usuario < numero_secreto

        if acertou:
            print("VOCÊ ACERTOOOOUUU!!!. Seus pontos: {}".format(pontos), "!")
            break
        else:
            if maior:
                print("Você errou :( O seu chute foi maior do que o número secreto.")
            elif menor:
                print("Você errou :( O seu chute foi menor do que o número secreto.")
            pontos_perdidos = abs(numero_secreto - numero_usuario)
            pontos = pontos - pontos_perdidos
            print("Seus pontos: {}".format(pontos))

    print("O número secreto era", numero_secreto)
    continuar()
    
    print("Fim do jogo")

def continuar():
    opcao= int(input("Escolha [1] Jogar novamente | [2] Trocar de jogo: "))
 
    if (opcao == 1):
        jogar()
    elif (opcao == 2):
        jogos.escolhe_jogo()

if(__name__ == "__main__"):
    jogar()