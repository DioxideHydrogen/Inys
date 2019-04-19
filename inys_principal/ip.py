#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
import requests
import bs4
import json
from pesquisas import *
'''
Token = 08e7b32026b7f15eb659455c1eaa09c6

cores = {
		'vermelho': '33[31m',
		'verde': '33[32m',
		'azul': '33[34m',
		'ciano': '33[36m',
		'magenta': '33[35m',
		'amarelo': '33[33m',
		'preto': '33[30m',
		'branco': '33[37m',
		'original': '33[0;0m',
		'reverso': '33[2m',
	}
'''

urlIPmain = 'http://meuip.com/'
urlIPdata = 'http://api.ipstack.com/{}?access_key={}&format=1'
def meuIp():
    global urlIPmain
    request = requests.get(urlIPmain)
    request = request.text
    soup = bs4.BeautifulSoup(request, 'html.parser')
    ip = soup.find('font',{'color':'#FF0000'}).get_text()
    ip = ip.encode('utf8')
    print '[+] IP: ' + ip
    return ip
def localizeIP(ip,token):
    from acentos import remover_acentos
    global urlIPdata
    try:
        url = urlIPdata.format(ip, token)
        request = requests.get(url)
        request = request.json()
        #print request
        print '\33[32m[+]\33[0;0m País: {}'.format(remover_acentos(request['country_name'].encode('utf-8')))
        print '\33[32m[+]\33[0;0m Estado: {}'.format(remover_acentos(request['region_name'].encode('utf-8')))
        print '\33[32m[+]\33[0;0m Cidade: {}'.format(remover_acentos(request['city'].encode('utf-8')))
        print '\33[32m[+]\33[0;0m CEP: {}'.format(remover_acentos(request['zip'].encode('utf-8')))
        print '\33[32m[+]\33[0;0m Latitude: {}'.format(str(request['latitude']))
        print '\33[32m[+]\33[0;0m Longitude: {}'.format(str(request['longitude']))
        print '\33[33m[=]\33[0;0m IP: {}'.format(remover_acentos(request['ip'].encode('utf-8')))
        frase = '{}, {}, {}'.format(remover_acentos(request['country_name'].encode('utf-8')),remover_acentos(request['region_name'].encode('utf-8')),remover_acentos(request['city'].encode('utf-8')))
        a = Pesquise(frase)
        a.fala(frase)
    except Exception as err:
        print '[-] Error: {}'.format(str(err))