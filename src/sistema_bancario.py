mensagem_input = """\n#### Sistema Bancário ####
Opções disponíveis:

[1] - Depósito
[2] - Saque
[3] - Extrato
[4] - Sair

Qual operação deseja realizar? """

saldo = 0
quantidade_saque = 0
extrato = ""

while True:

    operacao = int(input(mensagem_input))

    if operacao > 4 or operacao < 1:
        print("Operação inválida!")

    if operacao == 1:
        print("\nOpção selecionada: [1] - Depósito.")
        deposito = float(input("Digite a quantidade desejada para depósito: "))

        if deposito > 0:
            saldo += deposito
            extrato = extrato + "\n" + "R$ +" + str(deposito)
        else:
            print("Deve-se depositar um valor maior que zero.")

    if operacao == 2:
        
        print("\nOpção selecionada: [2] - Saque.")

        if quantidade_saque == 3:
            print("Não é possível realzar o saque. Limite de saques diários: 3.")
        else:    
            saque = float(input("Digite a quantidade desejada para saque: "))
        
            if saque > 500:
                print("\nNão é possível realizar o saque. Valor máximo diário permitido: R$ 500,00.")
            elif saque > saldo:
                print(f"\nNão há saldo o suficiente. Saldo atual: {saldo}.")
            else:
                saldo -= saque
                quantidade_saque += 1
                extrato = extrato + "\n" + "R$ -" + str(saque)

    if operacao == 3:
        print("\nOpção selecionada: [3] - Extrato.")
        print("\n#### Extrato ####")
        if extrato == "":
            print("\n--- Não foram realizadas movimentações. ---")
        else:
            print(extrato)
            print(f"Saldo atual da conta: R$ {saldo}")

    if operacao == 4:
        print("\nOpção selecionada: [4] - Sair.")
        print("Saindo ...")
        break


    

    

