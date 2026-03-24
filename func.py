"""Funções para manipulação de dados de carros
Henrique Kazuo Shirai Takahashi - 19/05/2025
19/05/2025 - Criação das funções carregar, salvar(aparentemente n está funcionando), listar e pesquisar
           - Criar e atualizar registro criados
           - Deletar registro criado
           - Confirmação de atualização e exclusão de registro, tanto no início quanto no final
20/05/2025 - Validação da entrada de dados
           - Colocando cores
           - Salvar está funcionando"""

import os
import pandas as pd
from tabulate import tabulate
import Cores
from datetime import datetime
import pytz

colunas = ["Placa", "Situação", "Modelo", "Ano", "Preço Aluguel", "Preço por Km rodado"]

def carregar_dados():
    return pd.read_csv("DB_Carros.txt", sep=",", names=colunas)

def salvar_dados(DB):
    DB.to_csv("DB_Carros.txt", sep=",", index=False, header=False)

def listar_carros(DB):
    os.system("cls")
    print(tabulate(DB, headers='keys', tablefmt='rounded_grid', showindex=False))
    input(f"{Cores.Amarelo}Pressione Enter para voltar ao menu.{Cores.Reset}")

def pesquisar_por_placa(DB):
    os.system("cls")
    placa = input("Digite a placa do carro: ").strip().upper()
    resultado = DB[DB["Placa"] == placa]
    if not resultado.empty:
        print(tabulate(resultado, headers='keys', tablefmt='rounded_grid', showindex=False))
    else:
        print(f"{Cores.Vermelho}ERRO: Carro não encontrado.{Cores.Reset}")
    input(f"{Cores.Amarelo}Pressione Enter para voltar ao menu.{Cores.Reset}")

def criar_registro(DB):
    os.system("cls")
    while True:
        placa = input("Digite a placa do carro: ").strip().upper()
        if placa == "":
            print("Placa não pode estar vazia.")
        elif placa in DB["Placa"].values:
            print(f"{Cores.Vermelho}ERRO: Já existe um carro com essa placa. Tente outra.{Cores.Reset}")
        elif len(placa) != 7:
            print(f"{Cores.Vermelho}ERRO: A placa deve ter 7 caracteres.{Cores.Reset}")
        else:
            break

    situacao = "DISPONÍVEL"

    while True:
        modelo = input("Digite o modelo do carro: ").strip().upper()
        if modelo == "":
            print(f"{Cores.Vermelho}ERRP: Modelo não pode estar vazio.{Cores.Reset}")
        else:
            break

    while True:
        ano = input("Digite o ano do carro: ").strip()
        try:
            ano = int(ano)
            if ano < 1900 or ano > 2100:
                raise ValueError
            break
        except ValueError:
            print(f"{Cores.Vermelho}ERRO: Ano inválido. Digite um número inteiro entre 1900 e 2100.{Cores.Reset}")

    while True:
        preco_aluguel = input("Digite o preço de aluguel: ").strip().replace(",", ".")
        try:
            preco_aluguel = float(preco_aluguel)
            if preco_aluguel < 0:
                raise ValueError
            break
        except ValueError:
            print(f"{Cores.Vermelho}ERRO: Preço inválido. Digite um número positivo.{Cores.Reset}")

    while True:
        preco_km = input("Digite o preço por km rodado: ").strip().replace(",", ".")
        try:
            preco_km = float(preco_km)
            if preco_km < 0:
                raise ValueError
            break
        except ValueError:
            print(f"{Cores}ERRO: Preço inválido. Digite um número positivo.{Cores.Reset}")

    novo_registro = pd.DataFrame([[placa, situacao, modelo, ano, preco_aluguel, preco_km]], columns=colunas)
    DB = pd.concat([DB, novo_registro], ignore_index=True)
    salvar_dados(DB)
    
    print(f"{Cores.Verde}Registro criado com sucesso!{Cores.Reset}")
    input(f"{Cores.Amarelo}Pressione Enter para voltar ao menu.{Cores.Reset}")
    salvar_dados(DB)
    return DB

def atualizar_registro(DB):
    os.system("cls")
    placa = input("Digite a placa do carro que deseja atualizar: ").strip().upper()
    if placa not in DB["Placa"].values:
        print(f"{Cores.Vermelho}ERRO: Carro não encontrado.{Cores.Reset}")
        input(f"{Cores.Amarelo}ERRO: Pressione Enter para voltar ao menu.{Cores.Reset}")
        return DB

    # Confirmação do carro a ser atualizado
    # Mostrar dados básicos para confirmação
    carro = DB.loc[DB["Placa"] == placa].iloc[0]
    print(f"Placa: {carro['Placa']} - Modelo: {carro['Modelo']}")
    confirm_placa = input("É este o carro que deseja atualizar? (S/N): ").strip().upper()
    if confirm_placa != "S":
        print("Atualização cancelada.")
        input(f"{Cores.Amarelo}Pressione Enter para voltar ao menu.{Cores.Reset}")
        return DB

    while True:
        modelo = input("Digite o novo modelo do carro: ").strip().upper()
        if modelo == "":
            print(f"{Cores.Vermelho}ERRO: Modelo não pode estar vazio.{Cores.Reset}")
        else:
            break

    while True:
        ano = input("Digite o novo ano do carro: ").strip()
        try:
            ano = int(ano)
            if ano < 1900 or ano > 2100:
                raise ValueError
            break
        except ValueError:
            print(f"{Cores.Vermelho}ERRO: Ano inválido. Digite um número inteiro entre 1900 e 2100.{Cores.Reset}")

    while True:
        preco_aluguel = input("Digite o novo preço de aluguel: ").strip().replace(",", ".")
        try:
            preco_aluguel = float(preco_aluguel)
            if preco_aluguel < 0:
                raise ValueError
            break
        except ValueError:
            print(f"{Cores.Vermelho}ERRO: Preço inválido. Digite um número positivo.{Cores.Reset}")

    while True:
        preco_km = input("Digite o novo preço por km rodado: ").strip().replace(",", ".")
        try:
            preco_km = float(preco_km)
            if preco_km < 0:
                raise ValueError
            break
        except ValueError:
            print(f"{Cores.Vermelho}ERRO: Preço inválido. Digite um número positivo.{Cores.Reset}")

    # Confirmarção final para atualização dos dados
    print(f"Dados a serem atualizados: \nModelo: {modelo}\nAno: {ano}\nPreço Aluguel: {preco_aluguel}\nPreço por Km rodado: {preco_km}")
    confirm = input("Confirma atualização do registro? (S/N): ").strip().upper()
    if confirm == "S":
        DB.loc[DB["Placa"] == placa, ["Modelo", "Ano", "Preço Aluguel", "Preço por Km rodado"]] = [modelo, ano, preco_aluguel, preco_km]
        salvar_dados(DB)
        print("Registro atualizado com sucesso!")
    else:
        print("Atualização cancelada.")

    input(f"{Cores.Amarelo}Pressione Enter para voltar ao menu.{Cores.Reset}")
    return DB

def deletar_registro(DB):
    os.system("cls")
    placa = input("Digite a placa do carro que deseja deletar: ").strip().upper()
    if placa not in DB["Placa"].values:
        print("Carro não encontrado.")
        input(f"{Cores.Amarelo}Pressione Enter para voltar ao menu.{Cores.Reset}")
        return DB

    # Confirmação do carro a ser deletado
    carro = DB.loc[DB["Placa"] == placa].iloc[0]
    print(f"Placa: {carro['Placa']} - Modelo: {carro['Modelo']}")
    confirm_placa = input("É este o carro que deseja deletar? (S/N): ").strip().upper()
    if confirm_placa != "S":
        print("Exclusão cancelada.")
        input(f"{Cores.Amarelo}Pressione Enter para voltar ao menu.{Cores.Reset}")
        return DB

    # Confirmarção final para exclusão dos dados
    print(f"Dados a serem deletados: \nPlaca: {carro['Placa']}\nModelo: {carro['Modelo']}")
    confirm = input(f"Confirma exclusão do carro com placa {placa}? (S/N): ").strip().upper()
    if confirm == "S":
        DB = DB[DB["Placa"] != placa]
        salvar_dados(DB)
        print("Registro deletado com sucesso!")
    else:
        print("Exclusão cancelada.")

    input(f"{Cores.Amarelo}Pressione Enter para voltar ao menu.{Cores.Reset}")
    return DB