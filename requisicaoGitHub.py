#coding: utf-8
import urllib2
import json
import sys


def cash(url):
	nomeArquivo = url.replace("/", ",");
	try:
		f = open("Cache/"+nomeArquivo+".txt", "r")	
	except IOError:
		s = urllib2.urlopen(url).read()
		f = open("Cache/"+nomeArquivo+".txt", "w")
		f.write(s)

urlUser = 'https://api.github.com/users/{0}'

usuario = raw_input("Forneça o nome do usuário: ");
cash(urlUser.format(usuario))
f = open("Cache/"+urlUser.format(usuario).replace("/",",")+".txt", "r")	
s = f.read()
dados = json.loads(s)

print 'Usuario:', dados['login']
print 'Nome: ',dados['name']


cash(dados['followers_url'])
f = open("Cache/"+dados['followers_url'].replace("/", ",")+".txt", "r")	
seguidores = f.read()
dadosSeguidores = json.loads(seguidores)

for i in dadosSeguidores:
	cash(urlUser.format(i['login']))
	f = open("Cache/"+urlUser.format(i['login']).replace("/", ",")+".txt", "r")	
	seg = f.read()
	dadosSeguidor = json.loads(seg)
	print ''
	print '   ' + (' 'if dadosSeguidor['name'] == None else dadosSeguidor['name'])
	cash(urlUser.format(i['login'])+"/repos")
	f = open("Cache/"+(urlUser.format(i['login'])+"/repos.txt").replace("/", ","), "r")	
	repositorio = f.read()
	dadosRepositorio = json.loads(repositorio)
	for r in dadosRepositorio:
		print '      '+r['name']

raw_input("ola");


	
	
