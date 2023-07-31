mensagem_input = f"""\n{' Sistema Bancário ':-^60}
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
        print(f"\n{'Operação inválida!':^60}")

    if operacao == 1:
        print("\nOpção selecionada: [1] - Depósito.")
        deposito = float(input("Digite a quantidade desejada para depósito: "))

        if deposito > 0:
            saldo += deposito
            extrato = extrato + "\n" + "R$ +" + str(deposito)
            msg = f"Depósito realizado com sucesso: R$ {deposito:.2f}"
            print(f"\n{msg:^60}")
        else:
            print(f"\n{'Deve-se depositar um valor maior que zero.':^60}")

    if operacao == 2:
        
        print("\nOpção selecionada: [2] - Saque.")

        if quantidade_saque == 3:
            print(f"\n{'Não é possível realzar o saque. Limite de saques diários: 3':^60}")
        else:    
            saque = float(input("Digite a quantidade desejada para saque: "))
        
            if saque > 500:
                print(f"\n{'Não é possível realizar o saque.':^60}")
                print(f"\n{'Valor máximo diário permitido: R$ 500,00.':^60}")
            elif saque > saldo:
                msg = f"Não há saldo o suficiente. Saldo atual: R$ {saldo:.2f}."
                print(f"\n{msg:^60}")
            elif saque < 0:
                print(f"\n{'Deve-se digitar um valor maior que zero.':^60}")
            else:
                saldo -= saque
                quantidade_saque += 1
                extrato = extrato + "\n" + "R$ -" + str(saque)
                msg = f"Saque realizado com sucesso: R$ {saque:.2f}"
                print(f"\n{msg:^60}")

    if operacao == 3:
        print("\nOpção selecionada: [3] - Extrato.")
        print(f"\n{' Extrato Bancário ':#^60}") 
        if extrato == "":
            print(f"\n{'Não foram realizadas movimentações.':^60}")
        else:
            print(extrato)
            print(f"Saldo atual da conta: R$ {saldo:.2f}")
        print("")
        print(60*"#")

    if operacao == 4:
        print("\nOpção selecionada: [4] - Sair.")
        print("Saindo ...")
        break

    print(60*"-")