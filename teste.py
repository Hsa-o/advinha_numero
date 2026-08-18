import random

min = int(input("Digite o número min: "))
max = int(input("Digite o número max: "))

numero_sorteado = random.randint(min, max)

tentativa = 0

while True:
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



