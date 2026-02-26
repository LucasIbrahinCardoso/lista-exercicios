import os
import sys
import time



def apresentacao():
    os.system("cls")
    print("""                   ----> Olá! <----
          Este é um algoritmo para ajudar com a folha de pagamento!
          
          
          Deseja iniciar?
          
          1) Sim
          2) Não""")
    
def primeiraResposta():
    x = "0"
    while type(x) != type(0) or (x < 1 and x > 2):
        print("\n(Responda com 1 ou 2)")
        x = int(input("\nR: "))
    if x == 1:
        print("\n\n   -->Iniciando!\n\n")
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








def main():
    apresentacao()
    primeiraResposta()




if __name__ == "__main__":
    main()