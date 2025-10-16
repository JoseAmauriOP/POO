estoque_comida = {
    "arroz": 30,
    "feijão": 25,
    "macarrão": 20,
    "batata": 18,
    "carne": 12,
    "frango": 16,
    "queijo": 10,
    "pão": 40,
    "tomate": 22,
    "alface": 2
}

estoque_bebida = {
    "água mineral": 20,
    "refrigerante cola": 15,
    "suco de laranja": 10,
    "café": 24,
    "suco de uva": 8,
    "suco de Goiaba": 12,
    "chá": 18,
    "limonada": 9,
    "água de coco": 14,
    "espumante": 7
}

def mostrar_estoque(estoque_bebida,estoque_comida):

    print('Estoque de Comidas')
    for comida, quantidade in estoque_comida.items():
        print(f'Produto:{comida}, Quantidade:{quantidade}')

    print('\nEstoque de Bebidas')    
    for bebida, quant in estoque_bebida.items():
        print(f'Produto:{bebida}, Quantidade:{quant}')

def adicionar_produto(nome,quantidade, estoque_comida, estoque_bebida):
    opc = int(input('Em qual estoque você quer adicionar o produto?(1-comidas ou 2-bebidas):'))
    if opc == 1:
        estoque_comida[nome] = quantidade
        print('Operação feita com sucesso!.')

    elif opc == 2:
        estoque_bebida[nome] = quantidade
        print('Operação feita com sucesso!.')

    return estoque_bebida, estoque_comida

def remover_produto(nome,quantidade, estoque_bebida,estoque_comida):
    opc = int(input('Em qual estoque você quer remover o produto?(1-comidas ou 2-bebidas):'))
    if opc == 1:
        estoque_comida[nome] -= quantidade
    elif opc == 2:
        estoque_bebida[nome] -= quantidade
    return estoque_bebida, estoque_comida

def consultar_produto(nome, estoque_bebida, estoque_comida):
    if nome.lower() in estoque_comida.keys():
        print(f'O produto {nome} está com {estoque_comida[nome]} unidades')
    elif nome.lower() in estoque_bebida.keys():
        print(f'O produto {nome} está com {estoque_bebida[nome]} unidades')

def menu():
    global estoque_comida
    global estoque_bebida

    opc = input('Insira:\n1- Mostrar estoque\n' \
                '2- Adicionar Produtos\n' \
                '3- Remover Produtos\n' \
                '4- Consultar Produtos\n' \
                '5- Sair\n')
    while True:
        if opc == '1':
            mostrar_estoque(estoque_bebida, estoque_comida)

        elif opc == '2':
            nome = input('Digite o nome do produto:').lower()
            quantidade = int(input('Digite a quantidade:'))
            estoque_bebida, estoque_comida = adicionar_produto(nome, quantidade, estoque_comida, estoque_bebida)

        elif opc == '3':
            nome = input('Digite o nome do produto:').lower()
            quantidade = int(input('Digite a quantidade:'))
            estoque_bebida, estoque_comida = remover_produto(nome, quantidade, estoque_bebida, estoque_comida)
        
        elif opc == '4':
            consultar_produto('arroz', estoque_bebida, estoque_comida)
            
        elif opc == '5':
            print('Você saiu do Programa...Obrigado')
            break
        opc = input('Insira: 1- Mostrar estoque\n' \
                    '2- Adicionar Produtos\n' \
                    '3- Remover Produtos\n' \
                    '4- Consultar Produtos\n' \
                    '5- Sair\n')

def repor_automatico(estoque_bebida,estoque_comida):
    for prod,quant in estoque_bebida.items():
        if quant < 3:
            estoque_bebida[prod] += 5
    for produto, quantidade in estoque_comida.items():
        if quantidade < 3:
            estoque_comida[produto] += 5 
#repor_automatico(estoque_bebida,estoque_comida)

menu()


def salvar_relatorio(estoque_bebida, estoque_comida):
    with open('estoque.txt','a', encoding='utf-8') as arquivo:
        arquivo.write('Comidas:\n')
        for comida, unidades in estoque_comida.items():
            arquivo.write(f'{comida}:{unidades} unidades\n')

        arquivo.write('\nBebidas:\n')
        for bebida, quantidade in estoque_bebida.items():
            arquivo.write(f'{bebida}:{quantidade} unidades\n')
#salvar_relatorio(estoque_bebida,estoque_comida)
