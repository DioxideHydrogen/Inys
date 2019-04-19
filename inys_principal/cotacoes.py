#!/usr/bin/python2.7
# -*- coding: utf8 -*-
import requests
import bs4 
from pesquisas import *
import todasMoedas
class Cotacao:
    def __init__(self, comando):
        self.comando = comando 
    def preco(self, comando):
        def precoReal(comando):
            cotacao = comando
            moedas = todasMoedas.moedas('moedas')
            tamanhoCripto = len(moedas)
            print 'Quantidade de moedas existentes: {}'.format(str(tamanhoCripto))
            # while i < tamanhoCripto:
            #     if moedas[i] in comando:
            #         pass 
            #     i += 1
            if cotacao in moedas:
                print '{}: Moeda Existente'.format(cotacao)
                sigla = cotacao
                print 'Função do {}'.format(sigla)
                if 'dolar dos estados unidos' in cotacao or 'dolar americano' in cotacao:
                    print '[+] Dólar dos Estados Unidos'
                    try:
                        url = ['https://dolarhoje.com']
                        request = requests.get(url[0])
                        request = request.content
                        soup = bs4.BeautifulSoup(request, 'html.parser')
                        cotacao = soup.find('input',{'id':'nacional'})
                        cotacao = cotacao.get('value').replace(',',' reais e ')
                        cotacao = 'O atual preco do {} e de: {} centavos.'.format(sigla, cotacao)
                        a = Pesquise(cotacao)
                        a.fala(cotacao)
                    except:
                        frase = 'Erro ao obter valor da moeda {}.'.format(sigla)
                        a = Pesquise(frase)
                        a.fala(frase)
                elif 'dolar australiano' in cotacao:
                    print '[+] Dólar Australiano'
                    try:
                        url = ['https://dolarhoje.com/dolar-australiano-hoje/']
                        request = requests.get(url[0])
                        request = request.content
                        soup = bs4.BeautifulSoup(request, 'html.parser')
                        cotacao = soup.find('input',{'id':'nacional'})
                        cotacao = cotacao.get('value').replace(',',' reais e ')
                        cotacao = 'O atual preco do {} e de: {} centavos.'.format(sigla, cotacao)
                        a = Pesquise(cotacao)
                        a.fala(cotacao)
                    except:
                        frase = 'Erro ao obter valor da moeda {}.'.format(sigla)
                        a = Pesquise(frase)
                        a.fala(frase)
                elif 'dolar canadense' in cotacao or 'dolar canadiano' in cotacao:
                    print '[+] Dólar Canadense'
                    try:
                        url = ['https://dolarhoje.com/dolar-canadense-hoje/']
                        request = requests.get(url[0])
                        request = request.content
                        soup = bs4.BeautifulSoup(request, 'html.parser')
                        cotacao = soup.find('input',{'id':'nacional'})
                        cotacao = cotacao.get('value').replace(',',' reais e ')
                        cotacao = 'O atual preco do {} e de: {} centavos.'.format(sigla, cotacao)
                        a = Pesquise(cotacao)
                        a.fala(cotacao)
                    except:
                        frase = 'Erro ao obter valor da moeda {}.'.format(sigla)
                        a = Pesquise(frase)
                        a.fala(frase)
            else:
                frase = 'Moeda nao foi reconhecida'
                a = Pesquise(frase)
                a.fala(frase)
        #Verificação se é uma criptomoeda ou uma moeda
        moedas = todasMoedas.criptomoedas('criptomoedas')
        tamanhoCripto = len(moedas)
    	print '[+] Quantidade de criptomoedas existentes: {}'.format(str(tamanhoCripto))
        url = []
        if 'ines qual o preco do' in comando or 'inys qual o preco do' in comando or 'inis qual o preco do' in comando: # Verificação 1
            if 'ines qual o preco do' in comando or 'inys qual o preco do' in comando or 'inis qual o preco do' in comando:
                cotacao = comando[21:]
            else:
                pass
            try:
                url.append(todasMoedas.links_criptomoedas(cotacao))
            except:
                print '[-] Nenhum site encontrado na minha lista verificando funções'
            if cotacao in moedas:
                print '[+] {}{}: Moeda Existente'.format(cotacao[:1].upper(),cotacao[1:])
                sigla = cotacao
                print '[+] Chamando função do {}'.format(sigla)
                if 'bitcoin' in comando and 'cash' in comando or 'bitcoin cash' in comando:
                    print '[+] Bitcoin Cash'
                    try:
                        if url:
                            pass
                        else:
                            url = ['https://dolarhoje.com/bitcoin-cash-hoje/']
                        request = requests.get(url[0])
                        request = request.content
                        soup = bs4.BeautifulSoup(request, 'html.parser')
                        cotacao = soup.find('input',{'id':'nacional'})
                        cotacao = cotacao.get('value').replace(',',' reais e ')
                        cotacao = 'O atual preco do {} e de: {} centavos.'.format(sigla, cotacao)
                        a = Pesquise(cotacao)
                        a.fala(cotacao)
                    except:
                        frase = 'Erro ao obter valor da moeda {}.'.format(sigla)
                        a = Pesquise(frase)
                        a.fala(frase)
                elif 'bitcoin' in cotacao and 'diamond' in cotacao or 'bitcoin diamond' in cotacao:
                    print '[+] Bitcoin Diamond'
                    try:
                        url = ['https://dolarhoje.com/bitcoin-diamond-hoje/']
                        request = requests.get(url[0])
                        request = request.content
                        soup = bs4.BeautifulSoup(request, 'html.parser')
                        cotacao = soup.find('input',{'id':'nacional'})
                        cotacao = cotacao.get('value').replace(',',' reais e ')
                        cotacao = 'O atual preco do {} e de: {} centavos.'.format(sigla, cotacao)
                        a = Pesquise(cotacao)
                        a.fala(cotacao)
                    except:
                        frase = 'Erro ao obter valor da moeda {}.'.format(sigla)
                        a = Pesquise(frase)
                        a.fala(frase)
                elif 'bitcoin' in cotacao and 'gold' in cotacao or 'bitcoin gold' in cotacao:
                    print '[+] Bitcoin Gold'
                    try:
                        url = ['https://dolarhoje.com/bitcoin-gold-hoje/']
                        request = requests.get(url[0])
                        request = request.content
                        soup = bs4.BeautifulSoup(request, 'html.parser')
                        cotacao = soup.find('input',{'id':'nacional'})
                        cotacao = cotacao.get('value').replace(',',' reais e ')
                        cotacao = 'O atual preco do {} e de: {} centavos.'.format(sigla, cotacao)
                        a = Pesquise(cotacao)
                        a.fala(cotacao)
                    except:
                        frase = 'Erro ao obter valor da moeda {}.'.format(sigla)
                        a = Pesquise(frase)
                        a.fala(frase)
                elif 'bitcoin' in cotacao or 'btc' in cotacao or 'BTC' in cotacao or 'Bitcoin' in cotacao:
                    print '[+] Bitcoin'
                    try:
                        if url:
                            pass
                        else:
                            url = ['https://dolarhoje.com/bitcoin-hoje/']
                        request = requests.get(url[0])
                        request = request.content
                        soup = bs4.BeautifulSoup(request, 'html.parser')
                        cotacao = soup.find('input',{'id':'nacional'})
                        cotacao = cotacao.get('value').replace(',',' reais e ')
                        cotacao = 'O atual preco do {} e de: {} centavos.'.format(sigla, cotacao)
                        a = Pesquise(cotacao)
                        a.fala(cotacao)
                    except:
                        frase = 'Erro ao obter valor da moeda {}.'.format(sigla)
                        a = Pesquise(frase)
                        a.fala(frase)
                elif 'dogecoin' in cotacao or 'doge' in cotacao or 'doge coin' in cotacao:
                    print '[+] Dogecoin'
                    try:
                        url = ['https://dolarhoje.com/dogecoin-hoje/']
                        request = requests.get(url[0])
                        request = request.content
                        soup = bs4.BeautifulSoup(request, 'html.parser')
                        cotacao = soup.find('input',{'id':'nacional'})
                        cotacao = cotacao.get('value').replace(',',' reais e ')
                        cotacao = 'O atual preco do {} e de: {} centavos.'.format(sigla, cotacao)
                        a = Pesquise(cotacao)
                        a.fala(cotacao)
                    except:
                        frase = 'Erro ao obter valor da moeda {}.'.format(sigla)
                        a = Pesquise(frase)
                        a.fala(frase)
                elif 'dash' in cotacao:
                    print '[+] Dash'
                    try:
                        url = ['https://dolarhoje.com/dash/']
                        request = requests.get(url[0])
                        request = request.content
                        soup = bs4.BeautifulSoup(request, 'html.parser')
                        cotacao = soup.find('input',{'id':'nacional'})
                        cotacao = cotacao.get('value').replace(',',' reais e ')
                        cotacao = 'O atual preco do {} e de: {} centavos.'.format(sigla, cotacao)
                        a = Pesquise(cotacao)
                        a.fala(cotacao)
                    except:
                        frase = 'Erro ao obter valor da moeda {}.'.format(sigla)
                        a = Pesquise(frase)
                        a.fala(frase)
                elif 'litecoin' in cotacao or 'lite coin' in cotacao:
                    print '[+] Litecoin'
                    try:
                        url = ['https://dolarhoje.com/litecoin/']
                        request = requests.get(url[0])
                        request = request.content
                        soup = bs4.BeautifulSoup(request, 'html.parser')
                        cotacao = soup.find('input',{'id':'nacional'})
                        cotacao = cotacao.get('value').replace(',',' reais e ')
                        cotacao = 'O atual preco do {} e de: {} centavos.'.format(sigla, cotacao)
                        a = Pesquise(cotacao)
                        a.fala(cotacao)
                    except:
                        frase = 'Erro ao obter valor da moeda {}.'.format(sigla)
                        a = Pesquise(frase)
                        a.fala(frase)
                elif 'ethereum' in cotacao:
                    print '[+] Ethereum'
                    try:
                        if url:
                            pass
                        else:
                            url = ['https://dolarhoje.com/ethereum/']
                        request = requests.get(url[0])
                        request = request.content
                        soup = bs4.BeautifulSoup(request, 'html.parser')
                        cotacao = soup.find('input',{'id':'nacional'})
                        cotacao = cotacao.get('value').replace(',',' reais e ')
                        cotacao = 'O atual preco do {} e de: {} centavos.'.format(sigla, cotacao)
                        a = Pesquise(cotacao)
                        a.fala(cotacao)
                    except:
                        frase = 'Erro ao obter valor da moeda {}.'.format(sigla)
                        a = Pesquise(frase)
                        a.fala(frase)
                elif 'cardano' in cotacao or 'carpano' in cotacao:
                    print '[+] Cardano'
                    try:
                        if url:
                            pass
                        else:
                            url = ['https://dolarhoje.com/cardano-hoje/']
                        request = requests.get(url[0])
                        request = request.content
                        soup = bs4.BeautifulSoup(request, 'html.parser')
                        cotacao = soup.find('input',{'id':'nacional'})
                        cotacao = cotacao.get('value').replace(',',' reais e ')
                        cotacao = 'O atual preco do {} e de: {} centavos.'.format(sigla, cotacao)
                        a = Pesquise(cotacao)
                        a.fala(cotacao)
                    except:
                        frase = 'Erro ao obter valor da moeda {}.'.format(sigla)
                        a = Pesquise(frase)
                        a.fala(frase)
                elif 'aeternity' in comando or 'eternity' in comando or 'eternity' in comando:
                    print '[+] Aeternity'
                    try:
                        if url:
                            pass
                        else:
                            url = ['https://dolarhoje.com/aeternity-hoje/']
                        request = requests.get(url[0])
                        request = request.content
                        soup = bs4.BeautifulSoup(request, 'html.parser')
                        cotacao = soup.find('input',{'id':'nacional'})
                        cotacao = cotacao.get('value').replace(',',' reais e ')
                        cotacao = 'O atual preco do {} e de: {} centavos.'.format(sigla, cotacao)
                        a = Pesquise(cotacao)
                        a.fala(cotacao)
                    except:
                        frase = 'Erro ao obter valor da moeda {}.'.format(sigla)
                        a = Pesquise(frase)
                        a.fala(frase)
                else:
                    print '[-] De acordo com meu dicionário {} não é uma criptomoeda.'.format(cotacao)
                    print '[-] Verificando se {} é uma moeda.'.format(cotacao)
                    precoReal(cotacao)                
        elif 'quanto custa um' in comando: # Verificação 2
            cotacao = cotacao[16:]

        elif 'qual custa o' in comando: # Verificação 3
            cotacao = cotacao[16:]

        else: # Falha
            frase = 'Comando nao reconhecido'
            a = Pesquise(frase)
            a.fala(frase)
