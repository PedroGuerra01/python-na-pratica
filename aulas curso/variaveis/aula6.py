salario = float(input("Informe o salário: "))

# Verifica o cargo com base no salário

# maior ou menor que o valor.
if salario <= 3000:
    print("Programador junior")
    # então
elif salario > 3000 and salario <= 6000:
    print("Programador pleno")
elif salario> 6000 and salario <= 15000:
    print("Programador senior")
    # maior
else:
    print("Gerente de projetos")