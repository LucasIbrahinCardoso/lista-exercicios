import os
import sys
import time

listona = []

def apresentacao():
    os.system("cls")
    print("""                   ----> Olá! <----
          Este é um algoritmo para ajudar com a folha de pagamento!
          
          
          Deseja iniciar?
          
          1) Sim
          2) Não""")
    
def primeiraResposta():
    x = "0"
    while True:
        try:
            while type(x) != type(0) or (x < 1 and x > 2):
                print("\n(Responda com 1 ou 2)")
                x = int(input("\nR: "))
            if x == 1:
                print("\n\n   -->Iniciando!\n\n")
                break
            else:
                os.system("cls")
                print("Bye bye!")
                print(".")
                time.sleep(1.5)
                print(".")
                time.sleep(1)
                print(".")
                time.sleep(1.5)
                sys.exit()
        except ValueError:
            print("\n\nResponda com números! E com os corretos!")

def coletarInformacoes():
    x = []
    x.append(input("Digite seu nome: ")) ## 0
    while True:
        try:
            x.append(float(input("Digite a quantidade de horas trabalhadas no mês\nR: "))) ## 1
            break
        except ValueError:
            print("\nResponda com um número!\n")
    
    while True:
        turno = input("Digite o turno de trabalho (M = Matutino, V = Vespertino e N = Noturno)\nR:").lower() ## 2
        if turno == "m" or turno == "v" or turno == "n":
            x.append(turno)
            break
        else:
            print("Não digitou uma resposta adequada (M, V ou V)!")
        
    while True:
        category = input("Digite sua categoria (G = Gerente e O = Operário)\nR:").upper() ## 3
        if category == "G" or category == "O":
            x.append(category)
            break
        else:
            print("Não digitou uma resposta adequada (G ou O)!")
    return x
    
def valor(porcentagem, horas):
    return (((porcentagem / 100) * 1621.00) * horas)

def calculo(info):
    if info[3] == "G":
        if info[2] == "n":
          print(f"{info[0]}, salário deste mês será de {valor(10.0, info[1]):.2f}")  
        else:
          print(f"{info[0]}, salário deste mês será de {valor(15.0, info[1]):.2f}")  
    if info[3] == "O":
        if info[2] == "n":
          print(f"{info[0]}, salário deste mês será de {valor(9.0, info[1]):.2f}")  
        else:
          print(f"{info[0]}, salário deste mês será de {valor(14.0, info[1]):.2f}") 





def main():
    apresentacao()
    primeiraResposta()
    lista = coletarInformacoes()
    calculo(lista)



if __name__ == "__main__":
    main()