#coding: utf-8
import os
import json
from xml.dom import minidom
import shutil


from flask import Flask
from flask import request
app = Flask(__name__)

@app.route('/arquivos/json', methods=['GET'])
def api():
     l = os.listdir('/home/aluno/Desktop/arquivos')
     dic = {'arquivos' : l}
     return json.dumps(dic)


@app.route('/arquivos/xml', methods=['GET'])
def apixml():
    l = os.listdir('/home/aluno/Desktop/arquivos')

    doc = minidom.Document()

    #cria raiz e adicionar no documento
    raiz = doc.createElement('raiz')
    doc.appendChild(doc.createElement('raiz'))

    for i in l:
        item = doc.createElement('arquivo')
        item.setAttribute('name', i)
        raiz.appendChild(item)
    f = open('bla.txt','w')
    f.write(raiz.toprettyxml())
    return raiz.toprettyxml()

@app.route('/arquivos/<arquivo>', methods=['GET'])
def arquivos_get(arquivo):
    try:
        arq = open('./arquivos/'+arquivo, 'r')
        content = arq.read()
        arq.close()
        return content
    except:
        return json.dumps({'Mensagem':'Arquivo não existe'})

@app.route('/arquivos/<arquivo>', methods=['DELETE'])
def arquivos_delete(arquivo):
    try:
        os.remove('./arquivos/'+arquivo)
        return json.dumps({'Mensagem': 'Arquivo '+arquivo+' deletado'})
    except:
        return json.dumps({'Mensagem':'Arquivo não existe'})

@app.route('/arquivos/del', methods=['DELETE'])
def arquivos_del():
    shutil.rmtree('./arquivos/')
    return json.dumps({'Mensagem': 'Arquivos deletado'})


@app.route('/arquivos/<arquivo>', methods=['PUT'])
def arquivos_put(arquivo):
    try:

        try : os.mkdir('arquivos')
        except: pass
        arq = open('./arquivos/'+arquivo, 'w')
        content = request.form['conteudo']
        arq.write(content)
        arq.close()
        return json.dumps({'Mensagem':'Arquivo criado com sucesso'})
    except Exception as e:
        print(e)
        return json.dumps({'Mensagem':'Arquivo não existe'})

if __name__ == '__main__':
    app.run(debug=True, port=8080)
