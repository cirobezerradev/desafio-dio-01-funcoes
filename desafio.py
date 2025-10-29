
menu = """
[1] Cadastrar Usuário
[2] Listar Usuários Cadastrados
[3] Criar Conta
[4] Listar Contas
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
usuarios = []
contas = []


# FUNÇÃO SACAR COM TODOS ARGUMENTOS KEYWORDS ONLY
def sacar (*, valor: float) -> None:
        
        global saldo, extrato, limite, numero_saques

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            
            ver_extrato(saldo, extrato=extrato)
        
        else:
            print("Operação falhou! O valor informado é inválido.")
        


# FUNÇÃO DEPOSITAR COM TODOS OS ARGUMENTO POSITIONAL ONLY
def depositar(valor: float):
    global saldo, extrato

    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"

        ver_extrato(saldo, extrato=extrato)

    else:
        print("Operação falhou! O valor informado é inválido.")


# FUNÇÃO EXTRATO SALDO COM ARGUMENTO POSICIONAL E EXTRATO COMO ARGUMENTO NOMEADO
def ver_extrato(saldo: float, *, extrato: str) -> None:
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

# FUNÇÃO CRIAR USUÁRIO
def criar_usuario():
    
    global usuarios

    print("\n================ CRIAR USUÁRIO ================\n\n")
    nome = input("Digite o nome do usuário: ")
    data_nascimento = input("Digite a data de nascimento dd/mm/yyyy: ")
    cpf = input("Digite o CPF: ")
    endereco = input("Digite o endereço: ")

    if not(any(user.get("CPF") == cpf for user in usuarios)):
        usuarios.append({"Nome": nome, "Data de Nascimento": data_nascimento, "CPF": cpf, "Endereço": endereco})
    else:
        print("\nNão foi possível realizar o cadastro!\nEsse usuário já foi cadastrado anteriormente.")

# FUNÇÃO LISTAR USUÁRIOS CADASTRADOS
def listar_usuarios():
    print(8*"=", " USUÁRIOS CADASTRADOS ", 8*"=")

    if not usuarios:
        print("Nenhum usuário cadastrado")
        print(37 * "=")
        return
    
    for i, user in enumerate(usuarios, start=1):
        print(f"Usuário: {i}")
        for chave, valor in user.items():
            print(f"{chave}: {valor}")
        print(37 * "=")

# FUNÇÃO CRIAR CONTA
def criar_conta(agencia: str = "0001"):
     
    global contas, usuarios

    print("\n================ CRIAR CONTA ================\n\n")
    conta = str(len(contas) + 1)
    cpf = input("Digite um CPF de usuário cadastrado: ")

    if any(user.get("CPF") == cpf for user in usuarios):
        user = [user for user in usuarios if user.get("CPF") == cpf]
        contas.append(
            {
            "Agência": agencia,
            "Conta": conta,
            "Usuário": user[0]
            }
        )
        print(f"Conta número: {conta} de {user[0]['Nome']} - CPF: {user[0]['CPF']} cadastrada com sucesso!")
    else:
        print(f"Não foi possível criar a conta. Não existe usuário cadastrado com o CPF - {cpf} informado.")

# FUNÇÃO LISTAR CONTAS
def listar_contas():
    print(8*"=" + " Lista Contas Cadastradas " + 8*"=")

    if not contas:
        print("Nenhuma conta criada!")

    for conta in contas:
        for chave, valor in conta.items():
            if chave == "Usuário":
                print("Cliente:")
                for chave_user, valor_user in valor.items():
                    print(f"\t{chave_user}: {valor_user}")
                continue
            print(f"{chave}: {valor}")
        print(42*"-")

    print(42*"=")


while True:
    
    opcao = input(menu)

    if opcao == "1":
        criar_usuario()

    elif opcao == "2":
        listar_usuarios()

    elif opcao == "3":
        criar_conta()

    elif opcao == "4":
        listar_contas()

    elif opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        depositar(valor)   

    elif opcao == "s": 
        valor = float(input("Informe o valor do saque: "))
        sacar(valor=valor)        

    elif opcao == "e":
        ver_extrato(saldo, extrato=extrato)

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
  
