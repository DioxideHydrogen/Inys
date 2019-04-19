# -*- coding: utf8 -*-
import imp
import googlesearch
import os
import requests
import json
from gtts import gTTS
from playsound import playsound
import time
import paises
class Pesquise:
    def __init__(self, pesquisa):
        self.pesquisa = pesquisa
    def pesquise(self, pesquisa):
            pesquisa = self.pesquisa
            Rpesq = 'Aqui estao alguns resultados de {}'.format(pesquisa)
            Rpesq = str(Rpesq)
            audioN = 'falam.mp3'
            audio1 = gTTS(Rpesq,'pt')
            audio1.save(audioN)
            playsound(audioN)
            dic = []
            for resultado in googlesearch.search('"{}" google'.format(pesquisa), stop=1):
                print resultado
                dic.append(resultado)
            audioN = 'falam.mp3'
            audio1 = gTTS('Abrindo o primeiro link','pt')
            audio1.save(audioN)
            playsound(audioN)
            os.system("firefox {}".format(dic[0]))
    def tocar(self, musica):
        musica = self.pesquisa
        Rpesq = 'Pedindo para o YouTube tocar {}'.format(musica)
        Rpesq = Rpesq.encode('utf-8')
        Rpesq = str(Rpesq)
        audioN = 'falam.mp3'
        audio1 = gTTS(Rpesq,'pt')
        audio1.save(audioN)
        playsound(audioN)
        dic = []
        for resultado in googlesearch.search('"{}" youtube'.format(musica), stop=1):
            print resultado
            dic.append(resultado)
        os.system("firefox {}".format(dic[0]))
    def fala(self, fala):
        Rpesq = self.pesquisa
        Rpesq = str(Rpesq)
        audioN = 'falam.mp3'
        audio1 = gTTS(Rpesq,'pt')
        audio1.save(audioN)
        playsound(audioN) 
        time.sleep(2)
    def ping(self, ip):
        import socket
        Rpesq = 'Obtendo endereco ip de: '+ip
        Rpesq = str(Rpesq)
        audioN = 'falam.mp3'
        audio1 = gTTS(Rpesq,'pt')
        audio1.save(audioN)
        playsound(audioN)
        try:
            ip = socket.gethostbyname(ip)
            Rpesq = 'Sucesso, o endereco ip e: '+ip
            Rpesq = str(Rpesq)
            audioN = 'falam.mp3'
            audio1 = gTTS(Rpesq,'pt')
            audio1.save(audioN)
            playsound(audioN)
        except:
            Rpesq = 'Endereco invalido ou fora do ar'
            Rpesq = str(Rpesq)
            audioN = 'falam.mp3'
            audio1 = gTTS(Rpesq,'pt')
            audio1.save(audioN)
            playsound(audioN)
    def noticias(self):
        import requests
        import bs4
        from acentos import remover_acentos
        from gtts import gTTS
        from playsound import playsound
        url = 'https://noticias.uol.com.br/'
        request = requests.get(url)
        request = request.text
        soup = bs4.BeautifulSoup(request, 'html.parser')
        #titulo = soup.find_all('span',{'class':'thumb-kicker'}) # <span class="thumb-kicker">  Renúncia bilionária </span> 
        url = soup.find_all('a',{'data-audience-click':'{"reference":"abrir-chamada","component":"highlights-headline","mediaName":"Home"}'})
        conteudo = soup.find_all('h3',{'class':'thumb-title'}) # <h3 class="thumb-title">Governo congela gastos com o SUS, mas abre mão de bilhões à saúde privada  </h3>
        tamanhoConteudo = len(conteudo)
        tamanhoUrl = len(url)
        xis = ''
        for x in range(0,10):
            print 'Conteudo: ' + remover_acentos(conteudo[x].get_text())
            xis += remover_acentos(conteudo[x].get_text())+', '
            print 'Url: ' + str(url[x]['href'])
        Rpesq = xis.replace('R$','')
        Rpesq = str(Rpesq)
        audioN = 'falam.mp3'
        audio1 = gTTS(Rpesq,'pt')
        audio1.save(audioN)
        playsound(audioN) 
        time.sleep(2)