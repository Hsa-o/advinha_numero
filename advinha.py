import random

def tela_inicial():
    print("------------------------")
    print("Jogo de Advinhação")
    print("1 - Jogar")
    print("2 - Sair")

    return pedir_opcao([1, 2])

def menu ():
    print("------------------------")
    print("Escolha a dificuldade")
    print("1 - Fácil")
    print("2 - Médio")
    print("3 - Dificil")

def escolher_dificuldade():

    return pedir_opcao([1, 2, 3])
    
def dificuldades(n):
    minimo = 1

    if n == 1:
        tentativas = 10
        maximo = 50
    elif n == 2:
        tentativas = 7
        maximo = 100
    else:
        tentativas = 5
        maximo = 500
    print("------------------------")
    print(f"{tentativas} tentativas , numeros entre {minimo}-{maximo}")
    numero_sorteado = random.randint(minimo, maximo)

    return tentativas, minimo, maximo, numero_sorteado

def pedir_opcao (opcao):
    while True:
        try:
            entrada = int(input(""))

            if entrada in opcao:
                return entrada
            print("Escolha uma opção válida!")
            print("------------------------")

        except ValueError:
            print("Digite apenas números")

def jogar(tentativas, minimo, maximo, numero_sorteado):
    palpite = 0
    
    while True:
        if palpite == tentativas:
            print("voce perdeu")
            print("O numero sorteado foi:", numero_sorteado)
            break

        try:
            numero_digitado = int(input("")) 
            while numero_digitado < minimo or numero_digitado > maximo:
                print(f"Entre com numeros válidos entre {minimo}-{maximo}")       
                numero_digitado = int(input("")) 
            palpite += 1
            if numero_digitado > numero_sorteado:
                print("O número sorteado é menor!")
            elif numero_digitado < numero_sorteado:
                print("O número sorteado é maior!")
            else:
                print("Parabéns, o número sorteado foi: ", numero_sorteado)
                print(f"Voce conseguiu em {palpite} tentativas")
                print("------------------------")
                break
            print(f"Palpite {palpite}!")
            print("------------------------")

        except ValueError:
            print("Entre apenas com números")

while True:
    opcao = tela_inicial()
    if opcao == 1:
        menu()

        n = escolher_dificuldade()

        tentativas, minimo, maximo, numero_sorteado = dificuldades(n)

        jogar(tentativas, minimo, maximo, numero_sorteado)
    else:
        print("------------------------")
        print("Hsa-o")
        break