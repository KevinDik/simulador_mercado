from typing import List, Dict
from time import sleep

from models.produto import Produto
from utils.helper import formata_strin

produtos:  List[Produto] = []
carrinho:  List[Dict[Produto, int]] = []


def main():
    menu()


def escreve_linha(tamanho=42):
    print('=' * tamanho)


def menu():
    escreve_linha()
    print('=============== Bem  vindo ===============')
    print('=============== Geek Shop ================')
    escreve_linha()

    print('Selecione uma opção abaixo: ')
    print('1 - Cadastrar produto')
    print('2 - listar produto')
    print('3 - Comprar produto')
    print('4 - visualizar carrinho')
    print('5 - fechar pedido')
    print('6 - sair do sistema')

    opcao = int(input())
    if opcao == 1:
        cadastrar_produto()
    elif opcao == 2:
        listar_produto()
    elif opcao == 3:
        comprar_produto()
    elif opcao == 4:
        visualizar_carrinho()
    elif opcao == 5:
        fechar_pedido()
    elif opcao == 6:
        print('Volte sempre')
        sleep(2)
        exit(0)
    else:
        print('Opção inválida')
        sleep(1)
        menu()


def cadastrar_produto():
    print('Cadastro de produto')
    escreve_linha()

    nome = input('Informe o nome do produto: ')
    preco = float(input('Informe o preço do produto: '))

    produto = Produto(nome, preco)
    produtos.append(produto)
    print(f'O produto {produto.nome} foi cadastrado com sucesso')
    sleep(2)
    menu()


def listar_produto():
    if len(produtos) > 0:
        print('Listagem de produtos')
        escreve_linha()
        for produto in produtos:
            print(produto)
            escreve_linha(30)
            sleep(1)
    else:
        print('Ainda não existe produtos cadastrados.')
    sleep(2)
    menu()


def comprar_produto():
    pass


def visualizar_carrinho():
    pass


def fechar_pedido():
    if len(carrinho) > 0:
        valor_total = 0
        print('Produtos do carrinho')
        for item in carrinho:
            for dados in item.items():
                print(dados[0])
                print(f'Quantidade: {dados[1]}')
                valor_total += dados[0].preco + dados[1]
                escreve_linha(20)
                sleep(2)
        print(f'Sua fatura é {formata_strin(valor_total)}')
        print('volte sempre!')
        carrinho.clear()
        sleep(5)
    else:
        print('Ainda não existe produtos no carrinho')
        sleep(2)
        menu()


def pega_produto_por_codigo(codigo):
    p = None
    for produto in produtos:
        if Produto.codigo == codigo:
            p = codigo
    return p


if __name__ == '__main__':
    main()
