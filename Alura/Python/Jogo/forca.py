import random
import jogos

def jogar():
    imprime_abertura()
    opcao = assunto()
    palavra_secreta = carrega_palavra_secreta(opcao)
    
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    print(letras_acertadas)

    enforcou = False
    acertou = False
    erros = 0

    while (not enforcou and not acertou):
        
        chute = pede_chute()
        
        if (chute in palavra_secreta):
            chute_correto(palavra_secreta, chute, letras_acertadas)
        else:
            erros +=1
            desenha_forca(erros)
            
        
        enforcou = erros == 7
        acertou = "_" not in letras_acertadas
    
        print(letras_acertadas)

    if(acertou):
        imprime_ganhador()
    else:
        imprime_perdedor(palavra_secreta)
    
    continuar()
    
def continuar():
    opcao= int(input("Escolha [1] Jogar novamente | [2] Trocar de jogo: "))
 
    if (opcao == 1):
        jogar()
    elif (opcao ==2 ):
        jogos.escolhe_jogo()

def imprime_abertura():
    print("+------------------------------------+")
    print("|     Bem vindo no jogo de Forca     |")
    print("+------------------------------------+")

def assunto():
    print("Qual o assunto do jogo?")
    print("1 - Frutas | 2 - Paises | 3 - Animais")
    opcao = int(input("Qual opção você escolhe? "))
    return opcao

def carrega_palavra_secreta(opcao):
    if (opcao == 1):
        arquivo = open('frutas.txt', 'r', encoding="UTF-8")
    elif (opcao == 2):
        arquivo = open('paises.txt', 'r', encoding="UTF-8")
    elif (opcao == 3):
        arquivo = open('animais.txt', 'r', encoding="UTF-8")

    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta

def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]

def pede_chute():
    chute = input("Qual letra? ")
    chute = chute.strip().upper()
    return chute

def chute_correto(palavra_secreta, chute, letras_acertadas):
    index = 0
    for letra in palavra_secreta:
        if(chute == letra):
            letras_acertadas[index] = letra
        index += 1

def imprime_ganhador():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def imprime_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

if (__name__ == "__main__"):
    jogar()