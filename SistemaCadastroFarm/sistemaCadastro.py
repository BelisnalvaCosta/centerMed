# Dicionário do MENU
menu = """
[c] Cadastrar
[r] Retirar
[n] Novo Usuário
[c] Nova Conta
[lc] Lista Contas
[e] Extrato
[q] Sair
====> Digite sua opção: """

# Declaração das variáveis e constantes
qtde = 0
limite = 500
extrato = ""
numero_retiradas = 0
LIMITE_RETIRADAS = 499
contador_retirada = 0
retiradas_acumuladas = 0
contador_deposito = 0
depositos_acumulados = 0
lista_usuarios = []
nro_conta = 0
contas = []
CENTRAL_MEDICAMENTO = "0001"


def retirar(*, saldo, qtde, extrato, limite, numero_retiradas, limite_retiradas):
    if (saldo < qtde):  # verifica se há remedio
        print("Quantidade insuficiente!")
    elif (qtde > qtde):  # caso haja remedio, prossegue
        numero_retiradas += 1  # contador de retirada. O limite é de 499 retiradas
        if (qtde > limite):  # se a retirada for acima do limite diário de 499
            print(f"Retirada acima de qtde {limite} não permitido")
        elif (qtde < limite):  # se for menor que o limite diário, prossegue.
            if (numero_retiradas > limite_retiradas):  # verifica se já atingiu a quantidade de retiradas diárias.
                print("\nLimite de retirada diária atingida! Não é possível realizar mais de 499 retiradas ao dia!")
            else:

                global retiradas_acumuladas
                retiradas_acumuladas += qtde
                print(f"\nRetirada qtde{qtde} realizada com sucesso!")
                extrato = extrato + f"\nRetirada nº{numero_retiradas}: - qtde {qtde}"  # faz a adição da string ao texto que irá aparecer no extrato

                qtde = qtde - qtde

    return qtde, extrato


def cadastrar(qtde, extrato, /):
    qtde = qtde + qtde
    global contador_cadastro
    contador_cadastro += 1
    extrato = extrato + f"\nCadastro nº{contador_cadastro}: + qtde {qtde}"  # faz a adição da string ao texto que irá aparecer no extrato
    print(f"\nCadastro qtde {qtde} realizada com sucesso!")

    return qtde, extrato


def print_extrato(qtde, /, *, extrato):
    print("\n########## Extrato ########## ")  # mostra o extrato completo com as retiradas e cadastro.
    extrato = extrato + f"""\n 
\n Quantidade total de retiradas:    - qtde {retiradas_acumuladas}
\n Quantidade total de cadastros: + qtde {cadastros_acumulados}
\n __________________________________________________________        

   Sua quantidade é de:             qtde {qtde}"""

    print(extrato)
    return extrato


def criar_usuario(
        usuarios):  # nome="",cpf=1234567890,endereco="logradouro, nro - bairro - cidade/sigla estado"
    # endereço no formato: logradouro, nro - bairro - cidade/sigla estado
    cpf = input("Informe o CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)
    if usuario:
        print("CPF já cadastrado! Usuário já existe!")
        return

    nome = input("Informe o nome complete do usuário: ")
    endereco = input("Informe o endereço (logradouro, nro - barro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "cpf": cpf, "endereco": endereco})
    print("Usuario criado com sucesso!")


def criar_conta(central_medicamentos, nro_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Conta criada com sucesso!")
        return {"central_medicamentos": central_medicamentos, "nro_conta": nro_conta, "usuario": usuario}

    print("Usuário Não encontrado! Fluxo de Criação de conta encerrado!")


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def listar_contas(contas):
    for conta in contas:
        linha = f"""
            Central_medicamwentos: \t {conta['central_medicamentos']}
            C/C:\t{conta['nro_conta']}
            Titular: \t{conta['usuario']['nome']}

        """
        print("=" * 100)
        print(linha)


while True:  # laço infinito

    opcao = input(menu)  # faz a leitura do comando de entrada

    if opcao == "c":
        print("Cadastrar")
        cadastro = int(input("Quanto você deseja cadastrar?: "))
        if (cadastro > 0):  # verifica se a quantidade a ser cadastrada está correto
            qtde, extrato = cadastro(qtde, cadastro, extrato)
            cadastro_acumulados = cadastro_acumulados + cadastro
        else:  # se a quantidade a ser cadastrada for inválida
            print("Quantidade de retirada inválida. Tente novamente!")


    elif opcao == "r":
        print("Retirada")
        retirada = int((input("Quanto você deseja retirar?: ")))
        qtde, extrato = retirar(qtde=retirada, extrato=extrato, limite=limite, numero_retiradas=numero_retiradas,
                               limite_retiradas=LIMITE_RETIRADAS)


    elif opcao == "n":
        criar_usuario(usuarios=lista_usuarios)

    elif opcao == "c":
        nro_conta = len(contas) + 1
        conta = criar_conta(CENTRAL_MEDICAMENTO, nro_conta, lista_usuarios)
        if conta:
            contas.append(conta)
            # nro_conta +=1

    elif opcao == "lc":
        listar_contas(contas)

    elif opcao == "e":
        print_extrato(QTDE, extrato=extrato)

    elif opcao == "q":
        print("\n\nEncerrando...\n O Banco MR agradece a sua preferência!\n\n")
        break
    else:
        print("Operação Inválida! Por favor selecione novamente a operação desejada")