funcionario = []
salario = []

def adicionar():
    nome = input("Nome do funcionario: ")
    salario = float(input("Digite o salario: "))
    funcionario.append(nome)
    salario.append(salario)

def listar():
    for i in range(len(funcionario)):
        print(f"{funcionario[i]} - R$ {salario[i]:.2f}")

def buscar():
    nome_buscar = input("Digite o nome que quer buscar: ")
    for i in range(len(funcionario)):
        if funcionario[i].lower() == nome_buscar.lower():
            print(f"Encontrado: {funcionario[i]} - R$ {salario[i]:.2f}")
            return
    print("Funcionario não encontrado.")

def media():
    if len(salario) > 0:
        print("Media salarial:", sum(salario) / len(salario))
    else:
        print("Nenhum salario encontrado.")

while True: 
    print("\n1 - Adicionar")
    print("2 - Listar")
    print("3 - Buscar por um nome")
    print("4 - Media salarial")
    print("5 - Sair")

    opcao = input("Opção: ")

    if opcao == "1":
        adicionar()
    elif opcao == "2":
        listar()
    elif opcao == "3":
        buscar()
    elif opcao == "4":
        media()
    elif opcao == "5":
        print("Saindo...")
        break
    else:
        print("Opção invalida")
