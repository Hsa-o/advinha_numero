import random


print("Advinhe o numero entre 1 e 100")
numero_sorteado = random.randint(1, 100)
tentativa = 0


while True:
    if tentativa == 5:
        print("voce perdeu")
        print("numero sorteado foi:", numero_sorteado)
        break
    try:
        numero_digitado = int(input("")) 
        while numero_digitado < 1 or numero_digitado > 100:
            print("Entre com numeros validos")
            numero_digitado = int(input("")) 
        tentativa += 1
        if numero_digitado > numero_sorteado:
            print("O número sorteado é menor!")
        elif numero_digitado < numero_sorteado:
            print("O número sorteado é maior!")
        else:
            print("Parabéns, o número sorteado foi: ", numero_sorteado)
            print(f"Voce conseguiu em {tentativa} tentativas")
            break
    except ValueError:
        print("Entre com números válido")


