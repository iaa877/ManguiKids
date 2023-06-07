import os
os.system("cls")

usuarios = []

def exibir_menu():
    print("MENU:")
    print("1. Login")
    print("2. Cadastro")

def cadastro(usuario: str, senha: str, email: str):
    for u in usuarios:
        if u["usuario"] == usuario:
            return False  # Usuário já existe, retorno False
    usuarios.append({"usuario": usuario, "senha": senha, "email": email})
    return True

def login(usuario: str, senha: str):
    for u in usuarios:
        if u["usuario"] == usuario and u["senha"] == senha:
            return True
    return False

while True:  # Looping infinito
    opcao = ""
    while opcao not in ["1", "2"]:
        exibir_menu()
        opcao = input("Digite a opção desejada (1 ou 2): ")

    if opcao == "1":
        usuario = input("Digite o nome de usuário: ")
        senha = input("Digite a senha: ")
        if login(usuario, senha):
            print("Login efetuado com sucesso!")
            # Restante do código após o login...
        else:
            print("Usuário ou senha incorretos. Tente novamente.")
    elif opcao == "2":
        usuario = input("Digite o nome de usuário: ")
        senha = input("Digite a senha: ")
        email = input("Digite o e-mail: ")
        if cadastro(usuario, senha, email):
            print("Cadastro realizado com sucesso!")
            # Restante do código após o cadastro...
        else:
            print("Nome de usuário já existente. Tente novamente.")

    livros = {"Livro1": "texto1", "Livro2": "texto2", "Livro3": "texto3"}

    def escolha_livros(livros: dict):
        print("Escolha um livro para ler:")
        for livro in livros:
            print(livro)
        escolha = input("Digite o nome do livro: ")
        if escolha in livros:
            print("Você escolheu:", escolha)
            print("Texto do livro:", livros[escolha])
        else:
            print("Livro não encontrado.")

    def avaliacao():
        estrelas = int(input("Avalie sua satisfação com a leitura de 0 a 5: "))
        if estrelas < 0 or estrelas > 5:
            print("Avaliação inválida. Digite um valor entre 0 e 5.")
        else:
            print("Obrigado pela avaliação!")

    medalhas = {0: "medalha1", 30: "medalha2", 60: "medalha3"}

    def recompensas(pontuacao: int, medalhas: dict):
        for pontos, medalha in sorted(medalhas.items(), reverse=True):
            if pontuacao >= pontos:
                return medalha
        return "Nenhuma medalha"

    if login(usuario, senha):
        escolha_livros(livros)
        avaliacao()
        pontuacao = int(input("Informe a pontuação feita pelo usuário: "))
        medalha_recebida = recompensas(pontuacao, medalhas)
        print("Medalha recebida:", medalha_recebida)
