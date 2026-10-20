def soma(a, b):
        return a + b

def subtracao(a, b):
        return a - b

def multiplicacao(a, b):
        return a * b

def divisao(a, b):
        if b == 0:
            raise ValueError("Proibido Divisao por 0!")
        return a / b

print ("Calculadora iniciada!")



while True:
       print("\n(0) SAIR \n(1) SOMA \n(2) SUBTRACAO \n(3) MULTIPLICACAO \n(4) DIVISAO")

       try:
            opcao = int(input("Selecione uma operacao: "))
            if opcao == 0:
                break
            a = float(input("Digite o valor de A: "))
            b = float(input("Digite o valor de B: "))
       except ValueError:
            print("Digite apenas numeros!")
            continue
       
       print("\n")

       try: 
            if opcao == 1:
                   resultado = soma(a, b)
                   print("A + B = ", resultado)
            elif opcao == 2:
                   resultado = subtracao(a, b)
                   print("A - B = ", resultado)
            elif opcao == 3:
                   resultado = multiplicacao(a, b)
                   print("A x B = ", resultado)
            elif opcao == 4:
                   resultado = divisao(a, b)
                   print("A / B = ", resultado)
            else: 
                print("Nao tem essa opcao!")
       except ValueError as erro:
              print(erro)

       
              
