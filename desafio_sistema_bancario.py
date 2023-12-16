menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=> """

cerquilho = "###################################"

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = int(input(menu))

    if opcao == 1:
        valor_deposito = float(input("Informe o valor a ser depositado: "))
        if valor_deposito > 0:
            saldo += valor_deposito
            extrato += f"Depósito: R$ {valor_deposito:.2f}\n"
            print("Depositando ... ")
        else:
            print("Não foi possível realizar o depósito, o valor informado deve ser maior que zero.")
    
    elif opcao == 2:
        valor_saque = float(input("Informe o valor a ser sacado: "))

        excedeu_saldo = valor_saque > saldo
        excedeu_limite = valor_saque > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES
    
        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        
        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")
        
        elif excedeu_saques:
            print("Operação falhou! O número máximo de saques permitidos foi ultrapassado")
        
        elif valor_saque > 0:
            saldo -= valor_saque
            extrato += f"Saque: R$ {valor_saque:.2f}\n"
            numero_saques += 1
        
        else:
            print("Não foi possível realizar o saque, o valor informado é inválido.")

    elif opcao == 3:
        print(cerquilho)
        print("Extrato".center(35) + "\n")
        print("Não foram realizadas movimentações" if not extrato else extrato)
        print(f"\nSaldo --> R$ {saldo:.2f}")
        print(cerquilho)
    
    elif opcao == 0:
        break

    else:
        print("Operação inválida, por favor selecione novamente a opção desejada.")