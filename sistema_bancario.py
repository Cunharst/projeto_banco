menu = """
[01] Depositar
[02] Sacar
[03] Extrato
[04]Sair

        Obrigado por acessar nosso banco!
=> """

saldo = 0
limite = 500
extrato = " "
numero_saque = 0
LIMITE_SAQUES = 3

while True:
    print(menu)
                  
    opcao = input("Escolha uma opção")

    if opcao == "1":
        deposito = float(input("Quando você deseja depositar?"))
        if deposito > 0:
         saldo += deposito
         print ("f:{deposito}depositados com sucesso")
        else:
            print("Depósito inválido")

    elif opcao == "2":
        valor = float(input("Quanto você deseja sacar?"))
        
        excedeu_limite = valor > limite
        excedeu_saque = numero_saque >= LIMITE_SAQUES
        excedeu_saldo = saldo < valor
        
        if excedeu_limite:
            print("Você excedeu o limite")
        elif excedeu_limite:
            print("Você excedeu os saques diários")
        elif excedeu_saldo:
            print("Você não possui saldo")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor: .2f} \n"
        else :
            print("Inválido")
            break

    elif opcao == "3":
        print("Não foram realizadas movimentações" if extrato else extrato)
        print(f"Extrato Saldo = {saldo:.2f}")


    elif opcao == "4": 
        print ("Até logo!")
        break

    else:
        print("Inválido")
