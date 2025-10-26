from package.sistema import Sistema

def menu():
    sistema = Sistema()
    while True:
        print("""
========== MENU ==========
1. Cadastrar Usuário
2. Cadastrar Carro
3. Listar Carros
4. Alugar Carro
5. Devolver Carro
6. Sair
==========================
""")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome do usuário: ")
            email = input("Email do usuário: ")
            sistema.cadastrar_usuario(nome, email)

        elif opcao == "2":
            if not sistema.usuarios:
                print("\n Cadastre um usuário antes de cadastrar carros.")
                continue

            print("\nUsuários cadastrados:")
            for i, u in enumerate(sistema.usuarios, 1):
                print(f"{i}. {u.nome}")

            dono_idx = int(input("Escolha o dono do carro: "))
            dono = sistema.usuarios[dono_idx - 1]

            marca = input("Marca do carro: ")
            modelo = input("Modelo do carro: ")
            ano = int(input("Ano: "))
            preco = float(input("Preço por dia (R$): "))
            sistema.cadastrar_carro(marca, modelo, ano, preco, dono)

        elif opcao == "3":
            sistema.listar_carros()

        elif opcao == "4":
            sistema.listar_carros()
            if not sistema.carros:
                continue
            idx = input("Escolha o número do carro para alugar: ")
            if not idx.isdigit():
                print("\n❌ Entrada inválida.")
                continue
            dias = input("Por quantos dias deseja alugar o carro? ")
            if not dias.isdigit():
                print("\n❌ Entrada inválida.")
                continue
            sistema.alugar_carro(int(idx), int(dias))

        elif opcao == "5":
            sistema.listar_carros()
            indice = int(input("Escolha o número do carro para devolver: "))
            sistema.devolver_carro(indice)

        elif opcao == "6":
            print("\n Saindo do sistema... Até mais!")
            break
        else:
            print("\n Opção inválida, tente novamente!")

if __name__ == "__main__":
    menu()

