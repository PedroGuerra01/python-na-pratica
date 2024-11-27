import os 

mensagens = []

nome = input("nome: ")

while True:
    # Limpa a tela antes de exibir as mensagens
    os.system('cls')

    # Exibe as mensagens já enviadas
    if len(mensagens) > 0:
        for m in mensagens:
            print(m['nome'], "-", m['texto'])
            
            print("__________________")
    
    # Solicita a nova mensagem ao usuário
    texto = input('mensagem (digite "fim" para terminar): ')
    
    if texto == "fim":
        break
    
    # Adiciona a nova mensagem à lista
    mensagens.append({
        "nome": nome,
        "texto": texto
    })

