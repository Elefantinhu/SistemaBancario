def menuInicial():
   menuInicial = """
   \n================ MENU ===================================
   [1] Contas
   [2] Saldos
   [q] Sair
   ============================================================
   => """
   
   return input(menuInicial)

def menuContas():
   menuContas = """
   \n========================================================
   [c] Criar Cliente
   [f] Criar Conta
   [l] Listar Contas
   [x] Listar Clientes
   [i] Voltar pro Menu Inicial
   [q] Sair
   ============================================================
   => """
   return input(menuContas)

def menuSaldos():
   menuSaldos = """
   \n=======================================================
   [d] Depositar
   [s] Sacar
   [e] Extrato
   [i] Voltar pro Menu Inicial
   [q] Sair
   ============================================================
   => """
   return input(menuSaldos)

        
def sair():
     print("\n================ DESCONECTANDO ================")
     print("Saindo do Sistema, muito obrigado por utilizar nosso banco.")
     print("=================================================")
     
     




   
       

def depositar(saldo, valor_deposito, extrato, /):

    if valor_deposito < 0:
           print("\n================ VALOR INVALIDO ======================")
           print("Não é possível depositar valores negativos, por favor digite um valor positivo")
           print("============================================================")
           

    else:
           saldo += valor_deposito
           extrato += f"Deposito: R$ {valor_deposito:.2f}\n"
           print("\n================ DEPOSITO REALIZADO ======================")
           print(f"Foi realizado o deposito no valor de: R${valor_deposito:.2f} seu saldo atual é: R${saldo:.2f}")
           print("============================================================")

    return saldo, extrato
        
def sacar(*, saldo, valor_saque, extrato, limite, numero_saques, limite_saques):
    if numero_saques < limite_saques:
                  if valor_saque > limite:
                     print("\n================ LIMITE ======================")
                     print("O valor é maior que o limite por saque")
                     print("=================================================")

                  elif valor_saque > saldo:
                     print("\n================ SALDO INSUFICIENTE ======================")
                     print("Não possui saldo suficiente na conta")
                     print("=================================================")

                  elif valor_saque < 0:
                     print("\n================ VALOR INVALIDO ======================")
                     print("Não é possível sacar valores negativos, por favor digite um valor positivo")
                     print("============================================================")

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

    return saldo, extrato, numero_saques

def exibir_extrato(saldo, /, *, extrato):
     print("\n================ EXTRATO ======================")
     print("Não foram realizadas movimentações." if not extrato else extrato)
     print(f"\nSaldo: R$ {saldo:.2f}")
     print("=================================================")
     return extrato
     
def criar_cliente(clientes):
     print("\n================ INSERIR CPF ======================")
     cpf = input("Digite o CPF do Cliente (Somente Numeros): ")
     print("============================================================") 
     cliente = validar_cpf(cpf, clientes)

     if cliente:
      print("\n================ CPF INVALIDO ======================")
      print("Já existe um Cliente com esse CPF")
      print("============================================================")
      return
     
     nome = input("Digite o Nome do Cliente: ")
     data_de_nascimento = input("Digite o Data de Nascimento do Cliente: ")
     endereco = input("Digite o Endereço do Cliente no formato: Logradouro, Número, Bairro, Cidade/Sigla do Estado: ")

     clientes.append({"nome": nome,"data_de_nascimento": data_de_nascimento,"cpf": cpf, "endereco": endereco})
     print("\n================ CLIENTE CRIADO ======================")
     print("Cliente Criado com Sucesso!")
     print("============================================================")
       

def validar_cpf(cpf, clientes):
     clientes_validados = [cliente for cliente in clientes if cliente["cpf"] == cpf]
     return clientes_validados[0] if clientes_validados else None

def validar_conta(cpf, contas):
     contas_validadas = [conta for conta in contas if conta["numero_conta"] == conta]
     return contas_validadas[0] if contas_validadas else None

def listar_contas(contas):
     
     for conta in contas:
         linha = f"""\
               Agência: {conta['agencia']}
               Conta: {conta['numero_conta']}
               Titular: {conta['cliente']['nome']}
         """
         print("=" * 100)
         print(linha)


def criar_conta(agencia, numero_conta, clientes):
     print("\n================ INSERIR CPF ======================")
     cpf = input("Digite o CPF do Cliente (Somente Numeros): ")
     print("============================================================") 
     cliente = validar_cpf(cpf, clientes)
     if cliente:
         print("\n================ CONTA CRIADA ======================")
         print("Conta Criada com Sucesso!")
         print("============================================================")
         return {"agencia": agencia, "numero_conta": numero_conta, "cliente": cliente}
     print("\n================ CLIENTE NAO ENCONTRADO ======================")
     print("Cliente Não Encontrando, Realizar o Cadastro do Cliente.")
     print("============================================================")

def deletar_conta(numero_conta, contas):
     numero_conta = input("Digite a Conta que deseja Deletar: ")
     conta = validar_conta(numero_conta, contas)
     if conta:
       print("============================================================")
       print("Conta Deletada com Sucesso")
       return {"numero_conta": numero_conta, "conta": conta}
     print("\n================ CONTA NAO ENCONTRADA ======================")
     print("Conta Não Encontrando, Por Favor tente novamente com uma Conta Valida.")
     print("============================================================")


def main():
  saldo = 0
  limite = 500
  extrato = ""
  numero_saques = 0
  LIMITE_SAQUES = 3
  AGENCIA = "0001"
  clientes = []
  contas = []
  nmr_conta = 0
  

  while True:
     
     opcaoInicial = menuInicial()

     if opcaoInicial == "1":
          opcao = menuContas()
     elif opcaoInicial == "2":
          opcao = menuSaldos()
     elif opcaoInicial == "q":
          opcao = "q"
     else:
          print("Digite uma Opção Válida")
          opcaoInicial = menuInicial()
          if opcaoInicial == "1":
           opcao = menuContas()
          elif opcaoInicial == "2":
           opcao = menuSaldos()
          elif opcaoInicial == "q":
           opcao = "q"
          
     

     if opcao == "d":
          
        print("\n================ INSERIR VALOR ======================")
        valor_deposito = float(input("Digite o Valor que deseja Depositar: "))
        print("============================================================")

        saldo, extrato = depositar(saldo, valor_deposito, extrato)
           
     elif opcao == "s":
               
            print("\n================ INSERIR VALOR ======================")
            valor_saque = float(input("Digite o Valor que deseja Sacar: "))
            print("============================================================")
            
            saldo, extrato, numero_saques = sacar(
                                   saldo = saldo, 
                                   valor_saque = valor_saque, 
                                   extrato = extrato, 
                                   limite = limite, 
                                   numero_saques = numero_saques, 
                                   limite_saques = LIMITE_SAQUES
                                   )
      
     elif opcao == "e":
        
         exibir_extrato(saldo, extrato = extrato)

     elif opcao == "c":
             criar_cliente(clientes)

     elif opcao == "l":
             listar_contas(contas)

     elif opcao == "f":
             
            nmr_conta = nmr_conta + 1
            conta = criar_conta(AGENCIA, nmr_conta, clientes)
            
            if conta:
                 contas.append(conta)

     elif opcao == "d":
             deletar_conta(nmr_conta, contas)
             
             if conta:
                  contas.remove(conta)
            

     elif opcao == "q":
        sair()
        break

     elif opcao == "i":
          continue

     else:
        print("Operação Inválida, por favor selecione novamente a operação desejada.")


main()