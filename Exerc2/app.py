listinhabonita = []
while True:
    while True:
        try:
            elevador = (input("\n\nDigite qual elevador tu mais usa, meu bom (A, B ou C)\nR: "))
            if elevador.upper() == "A" or elevador.upper() == "B" or elevador.upper() == "C":
                break
            else:
                print("\n\nParceiro, não foi isso que eu pedi...\n\n")
        except ValueError:
            print("\n\nNaum tah serto n. Tente again.\n\n")
    listinhabonita.append(elevador)

    while True:
        try:
            periodo = input("\nDigite em qual período usted tá uzano u subidô (M = Matutino, V = Vespertino, N = Noturno)\nR: ")
            if periodo.upper() == "M" or periodo.upper() == "V" or periodo.upper() == "N":
                break
            else:
                print("\nPessoa, use as letras corretas taokay?\n\n")
        except ValueError:
            print("\n\nPutz, errou, meu amigãozona (n sei seu genero, sorry). Faz novamente, por gentenleza.\n\n")
    listinhabonita.append(periodo)

    try:
        if input("\n\n\nSalve! Terminou, amigones? Vou aparecer aqui todas as vezes pra te perguntar, então tenha paciência. (0 = SIM e 1 = NÃO)\nR:") == "0":
            break
    except ValueError:
        print("\n\nResponde direito, zé cabecinha. (0 = SIM e 1 = NÃO)\n")
        if input("Queres parar ou não? Digame, jóvem.\nR: ") == "0":
            break

