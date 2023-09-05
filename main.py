# A estrutura condicional permite o desvio de fluxo de controle, quando determinadas exprressões lógicas são atendidas.

saldo = 2000
saque = float(input("Informe o valor do saque: "))

if saldo >= saque:
    print("Realizando saque!")
    print("SAQUE REALIZADO COM SUCESSO!")
if saldo < saque:
    print("Saldo insuficiente!")
