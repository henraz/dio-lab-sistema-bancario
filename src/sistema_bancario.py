mensagem_input = f"""\n{' Sistema Bancário ':-^60}
Opções disponíveis:

[D] - Depósito
[S] - Saque
[E] - Extrato
[Q] - Sair

Qual operação deseja realizar? """

saldo = 0
quantidade_saque = 0
extrato = ""

while True:

    operacao = input(mensagem_input).upper()

    if operacao not in 'DSEQ':
        print(f"\n{'Operação inválida!':^60}")

    if operacao == 'D':
        print("\nOpção selecionada: [D] - Depósito.")
        deposito = float(input("Digite a quantidade desejada para depósito: "))

        if deposito > 0:
            saldo += deposito
            extrato = extrato + "\n" + "R$ +" + str(deposito)
            msg = f"Depósito realizado com sucesso: R$ {deposito:.2f}"
            print(f"\n{msg:^60}")
        else:
            print(f"\n{'Deve-se depositar um valor maior que zero.':^60}")

    if operacao == 'S':
        
        print("\nOpção selecionada: [S] - Saque.")

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

    if operacao == 'E':
        print("\nOpção selecionada: [E] - Extrato.")
        print(f"\n{' Extrato Bancário ':#^60}") 
        if extrato == "":
            print(f"\n{'Não foram realizadas movimentações.':^60}")
        else:
            print(extrato)
            print(f"Saldo atual da conta: R$ {saldo:.2f}")
        print("")
        print(60*"#")

    if operacao == 'Q':
        print("\nOpção selecionada: [Q] - Sair.")
        print("Saindo ...")
        break

    print(60*"-")