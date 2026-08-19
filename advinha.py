from advinha_funcoes import tela_inicial, menu, escolher_dificuldade, dificuldades, pedir_opcao, jogar, pedir_numero 

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