# Lista onde todos os produtos serão armazenados
_lista_de_produtos = []


def cabecalho():
    # Mostra o cabeçalho do aplicativo.
    print('Bem-vindo à Lista de Compras Simples!')
    print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*')
    print()


def obter_id_atual():
    # Obtém o ID atual para o próximo produto automaticamente.
    if not _lista_de_produtos:
        return 0

    ultimo_id = max(produto['id'] for produto in _lista_de_produtos)

    return ultimo_id + 1


def limitar_tamanho_do_texto(texto, tamanho_maximo):
    # Limita o tamanho do texto e adiciona reticências (...) se necessário.
    if len(texto) <= tamanho_maximo:
        return texto
    else:
        return texto[:tamanho_maximo - 3] + '...'


def obter_valor_numerico(mensagem):
    # Obtém um valor numérico do usuário.
    while True:
        entrada_do_usuario = input(mensagem)
        try:
            valor = int(entrada_do_usuario)
            if valor < 0:
                raise ValueError
            return valor
        except ValueError:
            print('"' + entrada_do_usuario + '" é um número inválido, tente novamente.')


def adicionar_produto():
    # Adiciona um novo produto à lista.
    novo_produto = montar_produto()
    novo_produto['id'] = obter_id_atual()

    _lista_de_produtos.append(novo_produto)

    input("O produto '" + novo_produto['nome'] + "' foi adicionado com sucesso! Pressione ENTER para continuar...")


def remover_produto():
    # Remove um produto da lista pelo ID.
    id_do_produto_para_excluir = obter_valor_numerico("Qual é o ID do produto que você deseja excluir? >")
    for produto_atual in _lista_de_produtos:
        if produto_atual['id'] == id_do_produto_para_excluir:
            _lista_de_produtos.remove(produto_atual)
            input("Produto de ID '" + str(
                id_do_produto_para_excluir) + "' removido com sucesso! Pressione ENTER para continuar...")
            return

    input("Não foi possível encontrar o produto de ID '" + str(
        id_do_produto_para_excluir) + "'. Pressione ENTER para continuar...")


def listar_todos_os_produtos():
    # Lista todos os produtos na lista.
    if not _lista_de_produtos:
        print('Nenhum produto no banco de dados. Comece adicionando um produto!')
        return

    imprimir_tabela_de_resultados('PRODUTOS', _lista_de_produtos)


def pesquisar_todos_por_nome():
    # Pesquisa produtos pelo nome.
    if not _lista_de_produtos:
        input(
            "Nenhum produto na lista. Tente adicionar um novo produto primeiro. "
            "Pressione ENTER para tentar novamente..."
        )
        return

    nome_a_pesquisar = input("Qual é o nome ou parte nome do produto a pesquisar? >")

    produtos_encontrados = []
    for produto_atual in _lista_de_produtos:
        if nome_a_pesquisar.strip().lower() in produto_atual['nome'].strip().lower():
            produtos_encontrados.append(produto_atual)

    if not produtos_encontrados:
        input("Nenhum produto contendo '" + nome_a_pesquisar + "' foi encontrado. Pressione ENTER para continuar...")
        return

    imprimir_tabela_de_resultados('PRODUTOS FILTRADOS', produtos_encontrados)
    input(str(len(produtos_encontrados)) + ' produto(s) encontrado(s). Pressione ENTER para voltar ao menu...')


def imprimir_tabela_de_resultados(titulo, lista_de_produtos):
    # Imprime uma tabela formatada com os resultados.
    # Essa tabela está desenhada para aparecer na tela como uma tabela com bordas.
    print(titulo)
    print('|-------|-----------------|-------|------------|---------------------------|')
    print('|  ID   |      Nome       |  Qtd  |    Unidade |         Descrição         |')
    print('|-------|-----------------|-------|------------|---------------------------|')

    for produto in lista_de_produtos:
        _id = str(produto['id']).ljust(5)
        _nome = limitar_tamanho_do_texto(produto['nome'], 15).ljust(15)
        _quantidade = str(produto['quantidade']).ljust(5)
        _unidade = limitar_tamanho_do_texto(produto['unidade'], 10).ljust(10)
        _descricao = limitar_tamanho_do_texto(produto['descrição'], 25).ljust(25)

        print(f"| {_id} | {_nome} | {_quantidade} | {_unidade} | {_descricao} |")
        print('|-------|-----------------|-------|------------|---------------------------|')

    print()


def obter_opcao_de_unidade():
    # Obtém a unidade de medida do usuário.
    unidades = {
        '1': "Quilograma",
        '2': "Grama",
        '3': "Litro",
        '4': "Mililitro",
        '5': "Unidade",
        '6': "Metro",
        '7': "Centímetro"
    }

    while True:
        print("Escolha a unidade:")
        for chave, valor in unidades.items():
            print(f"{chave}. {valor}")

        valor = input("Selecione uma opção:")

        if valor not in ['1', '2', '3', '4', '5', '6', '7']:
            input("Unidade inválida! Pressione ENTER para tentar novamente...")
            continue

        return unidades[valor]


def montar_produto():
    # Monta um novo produto com base nas entradas do usuário.
    nome = input("Qual é o nome do produto? >")
    unidade = obter_opcao_de_unidade()
    quantidade = obter_valor_numerico("Qual é a quantidade do produto? >")
    descricao = input("Dê uma descrição para o produto: >")

    novo_produto = {
        "id": None,
        "nome": nome,
        "unidade": unidade,
        "quantidade": quantidade,
        "descrição": descricao
    }

    return novo_produto


def main():
    # Função principal que controla o fluxo do programa.
    while True:
        cabecalho()
        listar_todos_os_produtos()

        print('1. Adicionar produto à lista')
        print('2. Remover produtos')
        print('3. Pesquisar produtos')
        print('4. Sair')

        entrada_do_usuario = input("Selecione uma opção:")

        if entrada_do_usuario not in ['1', '2', '3', '4']:
            input("Opção inválida! Pressione ENTER para tentar novamente...")
            continue

        if entrada_do_usuario == '1':
            adicionar_produto()
        elif entrada_do_usuario == '2':
            remover_produto()
        elif entrada_do_usuario == '3':
            pesquisar_todos_por_nome()
        elif entrada_do_usuario == '4':
            print('Até mais!')
            break  # Sair do loop


main()
