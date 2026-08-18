import random

def menu ():
    print("1 - Fácil")
    print("2 - Médio")
    print("3 - Dificil")

menu()

n = int(input("Digite a dificuldade: "))

while n not in [1,2,3]:
    n = int(input("Digite a dificuldade: "))
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
        
palpite = 0

while True:

    if palpite == tentativas:
        print("voce perdeu")
        print("O numero sorteado foi:", numero_sorteado)
        break

    try:
        numero_digitado = int(input("")) 
        while numero_digitado < minimo or numero_digitado > maximo:
            print(f"Entre com numeros válidos{minimo}-{maximo}")       
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

    except ValueError:
        print("Entre apenas com números")





