def menu():
   menu = """
   \n================ MENU ===================================
   [d] Depositar
   [s] Sacar
   [e] Extrato
   [c] Criar Cliente
   [f] Criar Conta
   [l] Listar Clientes
   [q] Sair
   ============================================================
   => """
   return input(menu)

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

def main():
  saldo = 0
  limite = 500
  extrato = ""
  numero_saques = 0
  LIMITE_SAQUES = 3
  AGENCIA = "0001"
  clientes = []
  contas = []

  while True:
     
     opcao = menu()

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
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, clientes)
            
            if conta:
                 contas.append(conta)


     elif opcao == "q":
        print("\n================ DESCONECTANDO ================")
        print("Saindo do Sistema, muito obrigado por utilizar nosso banco.")
        print("=================================================")
        break

     else:
        print("Operação Inválida, por favor selecione novamente a operação desejada.")


main()