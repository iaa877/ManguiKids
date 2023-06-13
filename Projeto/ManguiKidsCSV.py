import csv
import os

os.system("cls")

usuarios = []

def exibir_menu():
    print("MENU:")
    print("1. Login")
    print("2. Cadastro")
    print("3. Sair")

def cadastro(usuario: str, senha: str, email: str):
    for u in usuarios:
        if u["usuario"] == usuario:
            return False  

    if "@" not in email or "." not in email:
        return False  

    usuarios.append({"usuario": usuario, "senha": senha, "email": email})
    return True

def login(usuario: str, senha: str):
    for u in usuarios:
        if u["usuario"] == usuario and u["senha"] == senha:
            return True
    return False

def salvar_usuarios():
    try:
        with open("usuarios.csv", "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["usuario", "senha", "email"])
            writer.writeheader()
            writer.writerows(usuarios)
    except Exception as e:
        print("Erro ao salvar usuários:", str(e))

def carregar_usuarios():
    try:
        if os.path.exists("usuarios.csv"):
            with open("usuarios.csv", "r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    usuarios.append(row)
    except Exception as e:
        print("Erro ao carregar usuários:", str(e))

def recompensas(pontuacao: int, medalhas: dict):
    for pontos, medalha in sorted(medalhas.items(), reverse=True):
        if pontuacao >= pontos:
            return medalha
    return "Nenhuma medalha"

carregar_usuarios()

logado = False

while True:
    try:
        if logado:
            print("Bem-vindo! O que você deseja fazer?")
            print("1. Escolher livro")
            print("2. Sair da conta")
            opcao = input("Digite a opção desejada (1 ou 2): ")
            if opcao == "1":
                livros = {"Livro1": "texto1", "Livro2": "texto2", "Livro3": "texto3"}
                print("Escolha um livro para ler:")
                for livro in livros:
                    print(livro)
                escolha = input("Digite o nome do livro: ")
                if escolha in livros:
                    print("Você escolheu:", escolha)
                    print("Texto do livro:", livros[escolha])
                    medalhas = {0: "Carangueijo de bronze", 30: "Caragueijo de Prata", 60: "Carangueijo de Ouro"}
                    pontuacao = int(input("Digite a sua pontuação: "))
                    print("Você ganhou o distintivo:", recompensas(pontuacao, medalhas))
                else:
                    print("Livro não encontrado.")
            elif opcao == "2":
                logado = False
                print("Conta encerrada. Volte sempre!")
            else:
                print("Opção inválida. Tente novamente.")
        else:
            exibir_menu()
            opcao = input("Digite a opção desejada (1, 2 ou 3): ")
            if opcao == "1":
                usuario = input("Digite o nome de usuário: ")
                senha = input("Digite a senha: ")
                if login(usuario, senha):
                    logado = True
                    print("Login efetuado com sucesso!")
                else:
                    print("Usuário ou senha incorretos. Tente novamente.")
            elif opcao == "2":
                usuario = input("Digite o nome de usuário: ")
                senha = input("Digite a senha: ")
                email = input("Digite o e-mail: ")
                if cadastro(usuario, senha, email):
                    print("Cadastro realizado com sucesso!")
                else:
                    print("Nome de usuário já existente ou e-mail inválido. Tente novamente.")
            elif opcao == "3":
                print("Encerrando o programa...")
                break
            else:
                print("Opção inválida. Tente novamente.")

        salvar_usuarios()
    except Exception as e:
        print("Ocorreu um erro:", str(e))
