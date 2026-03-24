''' 13/05/2025 - Criação do menu do adm (CRUD)
Henrique Kazuo Shirai Takahashi 13/05/2025
19/05/2025 - Criação do menu
           - Utilização das funções do func.py
           - Adicionado a biblioteca questionary
'''


import os
import func as fc
import questionary

def menu_adm():
    DB = fc.carregar_dados()

    while True:
        os.system("cls")
        opt = questionary.select(
            "Escolha a opção desejada: ",
            choices=[
                "1 - Listar todos os carros",
                "2 - Pesquisar por placa",
                "3 - Criar registro",
                "4 - Atualizar registro",
                "5 - Deletar registro",
                "6 - Sair"
            ]
        ).ask()

        if opt.startswith("1"):
            fc.listar_carros(DB)
        elif opt.startswith("2"):
            fc.pesquisar_por_placa(DB)
        elif opt.startswith("3"):
            DB = fc.criar_registro(DB)
            DB = fc.salvar_dados(DB)
        elif opt.startswith("4"):
            DB = fc.atualizar_registro(DB)
            DB = fc.salvar_dados(DB)
        elif opt.startswith("5"):
            DB = fc.deletar_registro(DB)
            DB = fc.salvar_dados(DB)
        elif opt.startswith("6"):
            os.system("cls")
            print("Saindo do sistema...")
            break

menu_adm()
    






