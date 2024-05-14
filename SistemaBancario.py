menu = """
\n================ MENU ===================================
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
============================================================
=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3


while True:
     
     opcao = input(menu)


     if opcao == "d":
          
        print("\n================ INSERIR VALOR ======================")
        valor_deposito = float(input("Digite o Valor que deseja Depositar: "))
        print("============================================================")

        if valor_deposito < 0:
           print("\n================ VALOR INVALIDO ======================")
           print("Não é possível depositar valores negativos, por favor digite um valor positivo")
           print("============================================================")
           

        else:
           saldo = valor_deposito + saldo
           extrato += f"Deposito: R$ {valor_deposito:.2f}\n"
           print("\n================ DEPOSITO REALIZADO ======================")
           print(f"Foi realizado o deposito no valor de: R${valor_deposito:.2f} seu saldo atual é: R${saldo:.2f}")
           print("============================================================")
           
    





     elif opcao == "s":
               
            print("\n================ INSERIR VALOR ======================")
            valor_saque = float(input("Digite o Valor que deseja Sacar: "))
            print("============================================================")

            if numero_saques < LIMITE_SAQUES:

                   if valor_saque > saldo:
                    print("\n================ SALDO INSUFICIENTE ======================")
                    print("Não possui saldo suficiente na conta")
                    print("=================================================")
                    

                   elif valor_saque > limite:
                     print("\n================ LIMITE ======================")
                     print("O valor é maior que o limite por saque")
                     print("=================================================")
                     

                   else:
                      saldo = saldo - valor_saque
                      extrato += f"Saque: R$ {valor_saque:.2f}\n"
                      print("\n================ SAQUE REALIZADO ======================")
                      print(f"Foi realizado o saque no valor de: R${valor_saque:.2f} seu saldo atual é: R${saldo:.2f}")
                      print("=================================================")
                      numero_saques += 1
    

            else:
                print("\n================ LIMITE ======================")
                print("Limite máximo de saques já realizados")
                print("=================================================")
        



     elif opcao == "e":
        print("\n================ EXTRATO ======================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("=================================================")


    
     
     elif opcao == "q":
        print("\n================ DESCONECTANDO ================")
        print("Saindo do Sistema, muito obrigado por utilizar nosso banco.")
        print("=================================================")
        break

     else:
        print("Operação Inválida, por favor selecione novamente a operação desejada.")