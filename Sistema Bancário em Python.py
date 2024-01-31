menu_inicio = (f"""
    Seja bem-vindo ao Banco Dio Brasil 
    Escolha qual operação deseja realizar:
    [1] Sacar 
    [2] Depositar 
    [3] Visualizar Extrato 
    [4] Sair
    """)

print(menu_inicio)

escolha_menu = -1
saldo_em_conta = 0
limite = 500
extrato = ""
numero_de_saques = 0
LIMITE_SAQUES = 3

while escolha_menu  != 0:
    escolha_menu = int(input("Digite o número da operação escolhida:"))

    if escolha_menu == 1:
        valor = float(input("Você escolheu saque, digite quanto deseja sacar:\n"))

        excedeu_saldo = valor > saldo_em_conta

        excedeu_limite = valor > limite

        excedeu_saque = numero_de_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print('Saldo insuficiente')

        elif excedeu_limite:
            print('O seu limite de saque é de 500 reais, refaça a operação')
                
        elif excedeu_saque:
            print('Você ultrapassou o seu limite de saque, você pode fazer 3 operações de saque por dia')

        elif valor > 0: 
            saldo_em_conta = saldo_em_conta - valor
            extrato += f"Saque: R$ {valor:.2f}\n "
            numero_de_saques = numero_de_saques + 1
        
        else:
            print("Operação falha, valor negativo")

    elif escolha_menu == 2:
        valor = float(input("Você escolheu deposito, digite quanto deseja depositar:\n"))
        if valor > 0:
            saldo_em_conta = valor + saldo_em_conta
            extrato += f"Deposito: R$ {valor:.2f}\n "
        else:
            print("Valor negativo, não é possível depositar")

    elif escolha_menu == 3:
        print("--------------------------")
        print("  Você escolheu extrato")
        print("--------------------------")
        print("Não foram realizadas operações." if not extrato else extrato)
        print(f"\n Saldo: R$:{saldo_em_conta:.2f}")
        print("--------------------------")

    elif escolha_menu == 4:
        print("\nVocê escolheu sair, Obrigada por usar o nosso banco!")
        break

    else: 
        print("Opção inválida")

