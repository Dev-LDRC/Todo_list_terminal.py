import os
from pathlib import Path
import json

NOME_ARQUIVO = 'list.json'
ARQUIVO = os.path.join(Path(__file__).parent, NOME_ARQUIVO)


######### AÇÕES DO PROGRAMA ######################################################

# adicionar tarefas.

def add_tarefa():
    lista.append(n)
    lista_do_sistema.append(n)
    print('itém adicionado com SUCESSO!')
    ##########################################
    with open(ARQUIVO, 'w', encoding='utf8') as work2:
        json.dump(lista, work2, ensure_ascii=False)

# visualizar a lista de tarefas adicionadas.

def view_lista():
    print('Tarefas:')
    for x in lista: 
        print(f'\t- {x}')
    ##########################

# opção de desfazer ação (Ctrl+z).

def desfazer_acao():
    if len(lista) >= 1:
        lista_do_sistema.append(lista[len(lista) - 1])
        lista.pop()
        print('Tarefas:')
        for x in lista:
            print(f'\t- {x}')
        ##########################
        with open(ARQUIVO, 'w', encoding='utf8') as work:
            json.dump(lista, work, ensure_ascii=False)
    else:
        print('Sua lista já está vazia, não tem mais elemento para se desfazer.')

# opção de refazer ação (Ctrl+Shift+z).

def refazer_acao():
    if len(lista) < len(lista_do_sistema):
        lista.append(lista_do_sistema[len(lista_do_sistema) - 1])
        lista_do_sistema.pop()
        print('Tarefas:')
        for x in lista:
            print(f'\t- {x}')
        ##########################
        with open(ARQUIVO, 'w', encoding='utf8') as work:
            json.dump(lista, work, ensure_ascii=False)
    else:
        print('Você não "desfez" nenhuma tarefa para usar esse comando.')


######### ORGANIZAÇÃO DO PROGRAMA ############################################

lista_do_sistema = []
lista = []

try:
    with open(ARQUIVO, 'r') as work:
        lista = json.load(work)
except:
    with open(ARQUIVO, 'w') as work:
        json.dump(lista, work)

print('=-=- BEM VINDO AO EDITOR -=-=')
print('O você pode fazer?')
info = '---->  adicionar tarefas. (PADRÃO)\n| 000 |>  sair do programa.\n| 1 |>  visualizar a lista de tarefas adicionadas.\n| 2 |>  opção de desfazer ação (Ctrl+z).\n| 3 |>  opção de refazer ação (Ctrl+Shift+z).'
print(info)
print()

while True:
    print('Digite um dos Numeros acima para interagir com a ação mensionada OU acrecente um itém a sua lista.')
    print('Digite ( 0 ) para visualizar os comandos do programa.')
    n = input('-> ')
    if n.isdigit():
        if n == '0':
            print(info)
            print()
            continue
        elif n == '1':
            view_lista()
            print()
        elif n == '2':
            desfazer_acao()
            print()
        elif n == '3':
            refazer_acao()
            print()
        elif n == '000':
            print()
            break
        else:
            continue
    else:
        add_tarefa()
        print()