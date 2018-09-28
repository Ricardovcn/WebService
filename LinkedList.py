
import requests

urlInit = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
num = 12345


def requisita(url):
    return requests.get(url)


r = requisita(urlInit+str(num));

while(True):
    try:
        if('Divide by two' in r.text):
            num = num/2		
        else:
            num = int(r.text.split()[-1])
        print (r.text)
        r = requisita(urlInit+str(num))
    except ValueError:
        print("O desafio foi vencido.")
        break


	

