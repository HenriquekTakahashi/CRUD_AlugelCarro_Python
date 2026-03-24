import os
from datetime import datetime
import pytz
import DB_Carros as carro
import func as FC

FC.fuso_brasil = pytz.timezone("America/Sao_Paulo")


print("\nCarros alugados:")
for carro in FC.alugados:
        print(f"{carro['id']}: {carro['modelo']} - {carro['ano']} | Cliente: {carro['cliente']} | Desde: {carro['data_aluguel']}")

try:
        carro_id = int(input("\nDigite o ID do carro que deseja devolver: "))
        for carro in FC.alugados:
            if carro["id"] == carro_id:
                data_devolucao = datetime.now(fuso_brasil)
                FC.gerar_recibo(carro, data_devolucao)
                carro["status"] = "disponível"
                carro["data_aluguel"] = None
                carro["cliente"] = None
                print("\n Carro devolvido com sucesso!")
            else:
                print("\n ID não encontrado entre os carros alugados.")
except ValueError:
        print("\n Entrada inválida.")

def menu():
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print("\n=== Sistema de Aluguel de Carros ===")
        print("1. Ver carros")
        print("2. Alugar carro")
        print("3. Devolver carro")
        print("4. Sair")

        escolha = input("Escolha uma opção: ")
        os.system("cls" if os.name == "nt" else "clear")
        
        if escolha == "1":
            FC.listar_carros_disponiveis()
        elif escolha == "2":
            FC.alugar_carro()
        elif escolha == "3":
            FC.devolver_carro()
        elif escolha == "4":
            print("Obrigado por usar nosso sistema!")
            break
        else:
            print("Opção inválida.")

        input("\nPressione Enter para continuar...")
        os.system("cls" if os.name == "nt" else "clear")
if __name__ == "__main__":
    menu()
