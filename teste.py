import random

minimo = int(input("Digite o número minimo: "))
maximo = int(input("Digite o número maximo: "))

numero_sorteado = random.randint(minimo, maximo)

tentativa = 0

while True:
    if tentativa >= 5:
        print("voce perdeu")
        break
    
    numero_digitado = int(input(" "))
    tentativa += 1

    if numero_digitado > numero_sorteado:
        print("O número sorteado é menor!")

    elif numero_digitado < numero_sorteado:
        print("O número sorteado é maior!")

    else:
        print("Parabéns, o número sorteado foi: ", numero_sorteado)
        print(f"Voce conseguiu em {tentativa} tentativas")
        break



