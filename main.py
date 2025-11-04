from package.controllers.sistema import Sistema

def prompt(msg):
    return input(msg + " > ").strip()

def menu():
    sistema = Sistema()
    while True:
        print("""
========== MENU ==========
1. Registrar usuário
2. Login
3. Cadastrar Carro (requer login)
4. Listar Carros
5. Alugar Carro
6. Devolver Carro
7. Logout
8. Sair
==========================
""")
        opcao = input("Escolha uma opção: ").strip()
        if opcao == "1":
            nome = prompt("Nome")
            email = prompt("Email")
            senha = prompt("Senha")
            try:
                sistema.cadastrar_usuario(nome, email, senha)
                print("Usuário registrado com sucesso. Faça login.")
            except Exception as e:
                print("Erro ao registrar:", e)
        elif opcao == "2":
            email = prompt("Email")
            senha = prompt("Senha")
            if sistema.autenticar(email, senha):
                print("Login realizado com sucesso.")
            else:
                print("Email ou senha inválidos.")
        elif opcao == "3":
            if not sistema.current_user:
                print("Você precisa estar logado para cadastrar um carro.")
                continue
            marca = prompt("Marca")
            modelo = prompt("Modelo")
            ano = prompt("Ano")
            preco = prompt("Preço por dia")
            try:
                sistema.cadastrar_carro(marca, modelo, ano, preco)
                print("Carro cadastrado com sucesso.")
            except Exception as e:
                print("Erro ao cadastrar carro:", e)
        elif opcao == "4":
            carros = sistema.listar_carros()
            if not carros:
                print("Nenhum carro cadastrado.")
            else:
                for i, c in enumerate(carros, 1):
                    status = "Disponível" if c.disponivel else f"Alugado ({c.dias_alugado} dias)"
                    print(f"{i}. {c.marca} {c.modelo} ({c.ano}) - {c.preco_dia} | {status} | dono: {c.dono}")
        elif opcao == "5":
            carros = sistema.listar_carros()
            if not carros:
                print("Nenhum carro disponível.")
                continue
            for i, c in enumerate(carros, 1):
                print(f"{i}. {c.marca} {c.modelo} - {'Disponível' if c.disponivel else 'Indisponível'}")
            try:
                idx = int(input("Escolha o número do carro para alugar: "))
                dias = int(input("Por quantos dias? "))
                valor = sistema.alugar_carro(idx, dias)
                print(f"Carro alugado. Valor total: {valor}")
            except Exception as e:
                print("Erro:", e)
        elif opcao == "6":
            carros = sistema.listar_carros()
            if not carros:
                print("Nenhum carro cadastrado.")
                continue
            for i, c in enumerate(carros, 1):
                print(f"{i}. {c.marca} {c.modelo} - {'Disponível' if c.disponivel else 'Alugado'}")
            try:
                idx = int(input("Escolha o número do carro para devolver: "))
                sistema.devolver_carro(idx)
                print("Carro devolvido com sucesso.")
            except Exception as e:
                print("Erro:", e)
        elif opcao == "7":
            sistema.logout()
            print("Logout realizado.")
        elif opcao == "8":
            print("Saindo...")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu()
