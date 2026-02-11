produtos = []
vendas = []

print('      === SISTEMA DE VENDAS ===     ')
print('Seja Bem-Vindo, adicione seus produtos na sacola!')

def cadastro_produto():
  print('\n--- Cadastro de Produto ---')
  nome_produto = input('\nDigite o nome do produto: ')
  preco_produto = float(input('Preço do produto (R$): '))

  produto = {'nome':(nome_produto), 'preco': (preco_produto)}
 
  produtos.append(produto) 
  print('Produto cadastrado com sucesso!')


def listar_produtos():
  if len (produtos) == 0:
    print('Nenhum produto cadastrado.')

  else:
    print('\n--- Lista de Produtos ---')
    for indice, produto in enumerate(produtos):
      print(f'\n{indice + 1} - {produto["nome"]} | R$ {produto["preco"]:.2f}')
      

def registrar_venda():
  if len (produtos) == 0:
    print('Não há produtos cadastrados para venda.')
    return

  else:
    print('\n--- Registrar Venda ---')
    print('Selecione o produto:')
    for (indice), produto in enumerate(produtos):
      print(f'{indice + 1} - {produto["nome"]} | R$ {produto["preco"]:.2f}')
    

    while True:
      escolha = input('\nDigite o número do produto: ')

      if not escolha.isdigit():
        print('Digite um número válido.')
        continue

      escolha = int(escolha)

      if escolha < 1 or escolha > len(produtos):
        print('Produto inexistente. Tente novamente.')
        continue

      produto_vendido = produtos.pop(escolha - 1)
      vendas.append(produto_vendido)

      print(f'Venda registrada com sucesso: {produto_vendido["nome"]}')
      return

def mostrar_total_vendas():
  if len(vendas) == 0:
    print('Nenhuma venda realizada')
    return

  total = 0

  for venda in vendas:
    total += venda ['preco']

  print(f'Valor total: R$ {total:.2f}')

def quantidade_vendas():
  if len(vendas) == 0:
    print('Nenhuma venda registrada.')
    return

  quantidade = len(vendas)
  print(f'Quantidade de vendas: {quantidade}')

def relatorio_vendas():
  print('\n--- Relatório de Vendas ---')
  if len(vendas) == 0:
    print('Nenhuma venda registrada.')
    return

  total_vendas = 0

  for indice, venda in enumerate(vendas):
    print(f'{indice + 1} - {venda["nome"]} | R$ {venda["preco"]:.2f}')
    total_vendas = total_vendas + venda['preco']
  print(f'Valor total: R${total_vendas:.2f}')
  


  
while True:
    print('\n=== MENU PRINCIPAL ===')
    print('1 - Cadastrar produto') 
    print('2 - Listar produtos')
    print('3 - Registrar venda')
    print('4 - Mostrar total de vendas')
    print('5 - Relatório de Vendas')
    print('6 - Sair')

    opcao = input('\nEscolha uma opção: ') 

    if opcao == '1':
      cadastro_produto()

    elif opcao == '2':
      listar_produtos()

    elif opcao == '3':
      registrar_venda()

    elif opcao == '4':
      mostrar_total_vendas()
      quantidade_vendas()

    elif opcao == '5':
      relatorio_vendas()

    elif opcao == '6':
      print('Sistema encerrado!')
      break

    else:
      print('Opção inválida')