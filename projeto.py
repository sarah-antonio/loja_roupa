# Listas para armazenar os dados
clientes = []
produtos = []

# Função para cadastrar cliente
def cadastrar_cliente():
    print("Cadastro de Cliente")
    nome = input("Nome do cliente: ")
    cpf = input("CPF do cliente: ")
    email = input("E-mail do cliente: ")
    
    cliente = {"nome": nome, "cpf": cpf, "email": email}
    clientes.append(cliente)
    print("Cliente cadastrado com sucesso!\n")

# Função para cadastrar produto
def cadastrar_produto():
    print("Cadastro de Produto")
    nome_produto = input("Nome do produto: ")
    categoria = input("Categoria do produto: ")
    preco = float(input("Preço do produto: R$ "))
    quantidade = int(input("Quantidade em estoque: "))
    
    produto = {"nome": nome_produto, "categoria": categoria, "preco": preco, "quantidade": quantidade}
    produtos.append(produto)
    print("Produto cadastrado com sucesso!\n")

# Função para exibir todos os clientes
def exibir_clientes():
    print("Lista de Clientes")
    if not clientes:
        print("Nenhum cliente cadastrado.")
    else:
        for cliente in clientes:
            print(f"Nome: {cliente['nome']}, CPF: {cliente['cpf']}, E-mail: {cliente['email']}")
    print()

# Função para exibir todos os produtos
def exibir_produtos():
    print("Lista de Produtos")
    if not produtos:
        print("Nenhum produto cadastrado.")
    else:
        for produto in produtos:
            print(f"Produto: {produto['nome']}, Categoria: {produto['categoria']}, Preço: R$ {produto['preco']}, Quantidade: {produto['quantidade']}")
    print()


