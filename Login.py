''' 12/05/2025 - Entrar como clientes ou funcionários(ADM) (funcionários precisam de login)
Henrique Kazuo Shirai Takahashi 
Otavio Henrique Neves de Lima
12/05/25 - Criação das escolha de entrada (Administrador/ Cliente)
         - Verificação e entrada de Usuário e Senha (Caso tente entrar como Administrador)
         - Caso Usuário e Senha corretos, vai para o Painel_ADM.py
         - Caso o usuário escolha a opção 2, vai para o Painel_Cleinte
13/05/25 - Colocando e usando a biblioteca questionary
20/05/25 - Colocando cores
'''

# Bibliotecas
import os
import Cores
import questionary
import Painel_ADM
import Painel_Cliente

# Enfeites
TELA = (f"""
{"="*60}
{"LOGIN":^60}
{"="*60}"""
)

# Verificação de login
def verificar_login(usuario, senha):
    try:
        with open('DB_funcionarios.txt', 'r') as adm:
            for linha in adm:
                linha = linha.strip()
                if not linha:
                    continue
                usuario_adm, senha_adm = linha.split(',')
                if usuario == usuario_adm and senha == senha_adm:
                    return True
        return False
    except FileNotFoundError:
        print(f"{Cores.Vermelho}ERRO: Arquivo de usuários não encontrado.{Cores.Reset}")
        return False

# Entrada
while True:
    os.system("cls")
    entrada = questionary.select(
        "Escolha como deseja entrar: ",
        choices=[
            "1 - Fazer login como administrador",
            "2 - Entrar como cliente",
            "3 - Encerrar o programa"
        ]
    ).ask()

    os.system("cls")
    print(TELA)

    if entrada.startswith("1"):
        usuario = input("Usuário: ").strip().upper()
        senha = input("Senha: ").strip().upper()

        if verificar_login(usuario, senha):
            Painel_ADM.menu_adm()
            break
        else:
            print(f"{Cores.Vermelho}ERRO: Usuário ou senha incorretos.{Cores.Reset}")
            input(f"{Cores.Amarelo}Pressione Enter para tentar novamente.{Cores.Reset}")
    elif entrada.startswith("2"):
        Painel_Cliente.menu_cliente()
        break
    elif entrada.startswith("3"):
        os.system("cls")
        input("Pressione Enter para sair do programa.")
        break
    else:
        print(f"{Cores.Vermelho}ERRO: Opção inválida.{Cores.Reset}")
        input(f"{Cores.Amarelo}Pressione Enter para continuar.{Cores.Reset}")
