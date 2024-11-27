fluxo_caixa = []

print("---------")
print("@ Fluxo caixa")
print("---------")
print("1 - Adicionar receita")
print("2 - Adicionar despesa")
print("\n# digite outro número para encerrar #\n")

# Função para adicionar transação (receita ou despesa)
def adicionar_transacao(opcao):
    nome = input("Nome: ")
    valor = float(input("Valor: R$ "))
    if opcao == 1:
        # Adiciona a receita
        fluxo_caixa.append({
            "nome": nome,
            "Valor": valor,
            "tipo": "Receita"
        })
    elif opcao == 2:
        # Adiciona a despesa como valor negativo
        fluxo_caixa.append({
            "nome": nome,
            "Valor": -valor,
            "tipo": "Despesa"
        })

while True:
    # Solicita a opção do usuário
    opcao = int(input("Digite a opção: "))

    if opcao == 1 or opcao == 2:
        # Chama a função para adicionar transação
        adicionar_transacao(opcao)
    else:
        # Encerra o loop se a opção for diferente de 1 ou 2
        break

    # Calcula o saldo total
    total = 0
    for fc in fluxo_caixa:
        total += fc["Valor"]

    # Exibe o saldo atual
    print(f"Saldo atual: R$ {total:.2f}\n")

# Exibe as transações ao final
print("\nResumo das transações:")
for fc in fluxo_caixa:
    print(f"{fc['tipo']} - {fc['nome']}: R$ {fc['Valor']:.2f}")
