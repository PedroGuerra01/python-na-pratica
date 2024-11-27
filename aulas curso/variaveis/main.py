# Solicita o nome do usuário e armazena na variável 'nome'
nome = input("Digite seu nome: ")

# Loop para garantir que o usuário insira uma idade válida (um número inteiro)
while True:
    try:
        # Solicita a idade e tenta convertê-la para inteiro
        idade = int(input("Digite sua idade: "))
        break  # Se a conversão for bem-sucedida, sai do loop
    except ValueError:
        # Exibe uma mensagem de erro caso o usuário insira algo que não seja um número
        print("Por favor, insira um número válido para a idade.")

# Loop para garantir que o usuário insira um peso válido (um número float)
while True:
    try:
        # Solicita o peso e tenta convertê-lo para float
        peso = float(input("Digite seu peso: "))
        break  # Se a conversão for bem-sucedida, sai do loop
    except ValueError:
        # Exibe uma mensagem de erro caso o usuário insira algo que não seja um número
        print("Por favor, insira um número válido para o peso.")

# Loop para garantir que o usuário insira uma altura válida (um número float)
while True:
    try:
        # Solicita a altura e tenta convertê-la para float
        altura = float(input("Digite sua altura: "))
        break  # Se a conversão for bem-sucedida, sai do loop
    except ValueError:
        # Exibe uma mensagem de erro caso o usuário insira algo que não seja um número
        print("Por favor, insira um número válido para a altura.")

# Exibe uma mensagem personalizada com os dados inseridos pelo usuário
print(f"Fala {nome}, espero que esteja bem.")
print(f"Pelo visto você tem {idade} anos.")
print(f"Seu peso seria {peso}.")
print(f"Você tem {altura} metros de altura.")

# Mensagem final agradecendo pelas informações fornecidas
print("AGRADEÇO PELAS INFORMAÇÕES, VAMOS PREENCHER NOSSO BANCO DE DADOS, TENHA UM OTIMO DIA.")
