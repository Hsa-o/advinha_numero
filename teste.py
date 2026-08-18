import random

def tela_inicial():
    print("Jogo de Advinhação")
    print("1 - Jogar")
    print("2 - Sair")

    while True:
        try:
            opcao = int(input("Digite a opção: "))
            while opcao not in [1,2]:
                opcao = int(input("(1,2)" ))
            break
        except ValueError:
            print("Digite apenas números")

    return opcao

def menu ():
    print("1 - Fácil")
    print("2 - Médio")
    print("3 - Dificil")

def escolher_dificuldade():
    while True:
        try:
            n = int(input("Digite a dificuldade: "))

            while n not in [1,2,3]:
                n = int(input("Digite a dificuldade(1, 2, 3): "))
            print("------------------------")
            break
        except ValueError:
                    print("Digite apenas números")
    return n
    

def dificuldades(n):
    if n == 1:
        tentativas = 10
        minimo = 1
        maximo = 50
        numero_sorteado = random.randint(minimo, maximo)
        print(f"{tentativas} tentativas , numeros entre 1-50")
    elif n == 2:
        tentativas = 7
        minimo = 1
        maximo = 100
        numero_sorteado = random.randint(minimo, maximo)
        print(f"{tentativas} tentativas, numeros entre 1-100")
    else:
        tentativas = 5
        minimo = 1
        maximo = 500
        numero_sorteado = random.randint(minimo, maximo)
        print(f"{tentativas} tenativas, numeros entre 1-500")
    return tentativas, minimo, maximo, numero_sorteado

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
        break
