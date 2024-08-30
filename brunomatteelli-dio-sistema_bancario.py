#Valores iniciais 
saldo = 742.30
numSaques = 0
extrato = ""

menu = """"
    =========================================
    =              BANCO ATIVA              =
                  =============

    Seja bem vindo ao nosso caixa eletrônico.
    Por favor, escolha uma das opções para 
    prosseguir:
    [ E ] Extrato
    [ S ] Saque
    [ D ] Depósito

    Para encerrar, digite [ Q ]
    =========================================
"""

menu_repeticao = """
    =========================================
    Por favor, escolha uma das opções para 
    prosseguir:
    [ E ] Extrato
    [ S ] Saque
    [ D ] Depósito

    Para encerrar, digite [ Q ]
    =========================================
"""

print(menu)
opcao_selecionada = input()

while opcao_selecionada.upper() != "Q":
    if opcao_selecionada.upper() == "E":
        # Exibir extrato = R$ XXXX.XX
        if extrato == "":
            print("Não foram realizadas movimentações.\n")
        else:
            print(extrato)
        print(f"Seu saldo é de R${saldo:.2f}\n")

    if opcao_selecionada.upper() == "S":
        print("Qual o valor será retirado?")
        valor = input()
        valor = float(valor)
        # Saque limite_saque = 3; limite_valor_saque = 500;
        if valor > 500:
            print("Valor máximo de R$ 500,00 por saque.\n")
        if numSaques < 3:
            if (saldo > valor):
                saldo = saldo - valor
                numSaques = numSaques + 1
                extrato = extrato + (f"Valor R${valor:.2f} retirado com sucesso.\n")
                print(f"Valor R${valor:.2f} retirado com sucesso.\n")
                print(f"Seu saldo é de R${saldo:.2f}\n")
            else:
                extrato = extrato + ("Seu saldo é insuficiente para realizar um saque neste valor.\n")
                print("Seu saldo é insuficiente para realizar um saque neste valor.\n")
        else:
            print("Você atingiu o limite de saques diários permitidos (3).\n")

    if opcao_selecionada.upper() == "D":
        print("Qual o valor será depositado?")
        valor = input()
        valor = float(valor)
        # Depósito
        if valor < 0:
            print("Por favor, depositar um valor válido.\n")
        else:
            saldo = saldo + valor
            extrato = extrato + (f"O valor R${valor:.2f} foi adicionado a sua conta.\n")
            print(f"O valor R$ {valor:.2f} foi adicionado a sua conta.\n")
            print(f"Seu saldo é de R${saldo:.2f}\n")

    if opcao_selecionada.upper() == "Q":
        break

    if opcao_selecionada.upper() not in ('E','D','S','Q'):
        print("Opção inválida.\n")

    print(menu_repeticao)
    opcao_selecionada = input()



