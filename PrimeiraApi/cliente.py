#coding: utf-8

import requests
import json

menu = 'SELECIONE UMA OPÇÃO:\n\n 1. Listar arquivos\n 2. Exibir arquivo\n 3. Remover arquivo\n 4. Remover todos os arquivos\n 5. Criar arquivo\n 6. Atualizar arquivo\n\n Opção:'
prefix = 'http://127.0.0.1:8080/'

def listarArquivos():
    dados = json.loads(requests.get(prefix+'arquivos/json').text)
    print('Arquivos:')
    for i in dados['arquivos']:
        print(' '+i)

def exibirArquivos(nome):
    dados = requests.get(prefix+'arquivos/'+nome).text
    print('Conteudo do arquivo:')
    print (dados)

def removerArquivo(nome):
    dados = json.loads(requests.delete(prefix+'arquivos/'+nome).text)
    print (dados['Mensagem'])

def criarArquivo(nome, conteudo):
    dados = json.loads(requests.put(prefix+'arquivos/'+nome, data={'conteudo': conteudo}).text)
    print (dados['Mensagem'])

def removerTodos():
    dados = requests.delete(prefix+'arquivos/del').text
    print (dados)
while(True):
    print(menu)
    op = input()

    if op == '1':
        listarArquivos()
    elif op == '2':
        print('Forneça o nome do arquivo:')
        nome = input()
        exibirArquivos(nome)
    elif op == '3':
        print('Forneça o nome do arquivo:')
        nome = input()
        removerArquivo(nome)
    elif op == '4':
        removerTodos()
    elif op == '5':
        print('Forneça o nome do arquivo:')
        nome = input()
        print('Forneça o conteudo:')
        conteudo = input()
        criarArquivo(nome, conteudo)
    elif op == '6':
        print('Forneça o nome do arquivo:')
        nome = input()
        print('Forneça o conteudo:')
        conteudo = input()
        criarArquivo(nome, conteudo)
    else:
        print('Opção Invalida')