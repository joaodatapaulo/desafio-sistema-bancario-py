menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do  depósito: ")) # É perguntado ao usuário qual será o valor do depósito.

        if valor > 0: # Primeira verificação para evitar depósitos de valores negativos conforme a instrução.
            saldo += valor # Se o valor for maior que 0, eu adiciono o valor (depósito) ao meu saldo em conta. Eu faço uma atribuição com uma operação de adição.
            extrato += f"Depósito: R$ {valor:.2f}\n" # Em seguida, é concatenado a string "Depósito: R$ + {valor:.2f}" que será colocada dentro do extrato para registrar o histórico.

        else:
            print("A operação falhou! O valor informado é inválido.") # Caso o valor não seja maior que 0, será mostrada essa mensagem para o usuário.
    
    elif opcao == "s":
        valor = float(input("Informe o valor do saque: ")) # É perguntado ao usuário qual será o valor do saque.
        
        excedeu_saldo = valor > saldo # Verificação para checar se excedeu o saldo.

        excedeu_limite = valor > limite # Verificação para checar se excedeu o limite.

        excedeu_saques = numero_saques >= LIMITE_SAQUES # Verificação para checar se excedeu o limite de saque.

        if excedeu_saldo: 
            print("A operação falhou! Você não tem saldo suficiente.") # Caso tenha excedido o valor do saldo, será mostrado esta mensagem.

        elif excedeu_limite:
            print("A operação falhou! O valor do saque excedeu o limite.") # Caso tenha excedido o valor do limite (mesmo tendo saldo), será mostrado esta mensagem.

        elif excedeu_saques:
            print("A operação falhou! Número máximo de saques excedido.") # Caso tenha excedido o valor de saques (mesmo tendo saldo), será mostrado esta mensagem.
        
        elif valor > 0: # Verificação para evitar saques de valores negativos.
            saldo -= valor # Se o valor para saque for válido e atender a todos os requisitos, o valor será debitado do saldo.
            extrato += f"Saque: R$ {valor:.2f}\n" # Em seguida, é concatenado a string Saque: R$ + {valor:.2f} que será colocada dentro do extrato para registrar o histórico.
            numero_saques += 1 # Incremento está variável para que os próximos saques não comecem de 0. Será contabilizado 1 + 1 = 2; no próximo 1 + 2 = 3. 
                               # Isso é feito para que a verificação LIMITE_SAQUES aconteça e ela barre o usuário.
        
        else:
            print("A operação falhou! O valor informado é inválido.") # Caso o valor não seja maior que 0, será mostrada essa mensagem para o usuário.


    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato) # If ternário verificando se o extrato está vazio. 
                                                                                 # O extrato é do tipo string e começa vazio. 
                                                                                 # Se não foi feita nenhuma operação, é exibido o extrato com a mensagem na string.
                                                                                 # Se o extrato não está vazio, é exibido o valor dentro da variável extrato.
        print(f"\nSaldo: R$ {saldo:.2f}") # É exibido o valor do saldo em qualquer circunstância. 
        print("=========================================")
        print("Extrato")
    
    elif opcao == "q": # Opção para sair.
        break

    else:
        print("Operação inválida, por favor, selecione novamente a operação desejada.") # Caso o usuário digite alguma operação desconhecida, será mostrada essa mensagem.
