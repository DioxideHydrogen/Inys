# -*- coding: utf8 -*-
import os
from datetime import datetime
from time import sleep
from pesquisas import Pesquise
from cotacoes import *
import database
import requests
import json
import ip
def interacao(frase):
    #re1 = re.search(r'Firefox', self.frase)
    #keyW = re1.group(0);
    comando = frase
    if 'abra o firefox' in comando:
        frase = 'Abrindo Firefox'
        a = Pesquise(frase)
        a.fala(frase)
        sleep(1)
        os.system('firefox')
    elif 'abra o google' in comando:
        frase =  'Abrindo Google.'
        a = Pesquise(frase)
        a.fala(frase)
        sleep(1)
        os.system('firefox https://www.google.com.br')
    elif 'tudo bem' in comando:
        frase = 'Estou sim e você?'
        a = Pesquise(frase)
        a.fala(frase)
        sleep(1)
    elif 'quando o mundo vai acabar' in comando:
        frase = 'Conforme o site Abril, por volta do ano 7500000000'
        a = Pesquise(frase)
        a.fala(frase)
        sleep(1)
    elif 'abra o facebook' in comando or 'abra o meu facebook' in comando:
        frase = 'Abrindo Facebook.'
        a = Pesquise(frase)
        a.fala(frase)
        sleep(1)
        os.system('firefox https://www.facebook.com')
    elif 'abra o whatsapp' in comando or 'abra o meu whatsapp' in comando:
        frase = 'Abrindo WhatsApp.'
        a = Pesquise(frase)
        a.fala(frase)
        sleep(1)
        os.system('firefox https://web.whatsapp.com')
    elif 'abra o github' in comando:
        frase = 'Abrindo GitHub.'
        a = Pesquise(frase)
        a.fala(frase)
        sleep(1)
        os.system('firefox https://www.github.com')
    elif 'abra o meu github' in comando and 'meu' in comando and 'repositório' in comando:
        frase =  'Abrindo seu GitHub.'
        a = Pesquise(frase)
        a.fala(frase)
        sleep(1)
        os.system('firefox https://www.github.com/ProfessorJamesBach/')
    elif 'abra o visual studio code' in comando:
        frase = 'Abrindo Visual Studio Code.'
        a = Pesquise(frase)
        a.fala(frase)
        sleep(1)
        os.system('code')
    elif 'Que horas sao' in comando or 'que horas sao' in comando:
        try:
            horas = datetime.now()
            hora = horas.hour
            min = horas.minute
            print str(hora)+':'+str(min)
            frase = 'Sao exatamente '+str(hora)+' horas e '+str(min)+' minutos.'
            a = Pesquise(frase)
            a.fala(frase)
        except Exception as err:
            print 'Erro: '+str(err)
    elif 'eu te amo' in comando:
        frase = 'Nossa relacao de IA para Humano ja e otima.'
        a = Pesquise(frase)
        a.fala(frase)
        sleep(1)
    elif 'pesquise' in comando or 'pesquisa' in comando:
        pesquisa = comando[15:]
        p = Pesquise(pesquisa)
        p.pesquise(pesquisa)
    elif 'toque' in comando or 'Toque' in comando:
        mu = comando[12:] #Alexa Toque --
        m = Pesquise(mu)
        m.tocar(mu)
    elif 'quem te criou' in comando or 'quem e seu criador' in comando:
        frase = 'Eu fui criada por Hugo Henrique'
        a = Pesquise(frase)
        a.fala(frase)
    elif 'qual o ip de' in comando or 'qual ip de' in comando:
        if 'qual o ip de' in comando:
            ip = comando[19:]
            print 'Pingando: {}'.format(ip)
            m = Pesquise(ip)
            m.ping(ip)
        elif 'qual ip de' in comando:
            ip = comando[17:]
            print 'Pingando: {}'.format(ip)
            m = Pesquise(ip)
            m.ping(ip)
    elif 'qual o preco do' in comando or 'quanto custa um' in comando or 'quanto custa o' in comando or 'qual preco do' in comando:
        try:
            coin = Cotacao(comando)
            coin.preco(comando)
        except Exception as err:
            f = 'Ocorreu algum erro.'
            a = Pesquise(f)
            a.fala(f)
            print 'Erro: '+ str(err)
    elif 'meu nome e' in comando or 'eu sou o' in comando or 'eu me chamo' in comando:
        try:
            if "meu nome e" in comando:
                horas = datetime.now()
                hora = horas.hour
                min = horas.minute
                seg = horas.second
                data = str(hora)+':'+str(min)+':'+str(seg)
                #alexa meu nome e hugo
                #01234567890123456
                nome = comando[17:]
                print 'Cadastrando usuário: {}'.format(nome)
                sql = 'INSERT INTO alexa_nomes(nome, data, hertz) VALUES (%s,%s,%s)' #.format(nome,data,'150Hz')
                sql_data = (0, nome, data, '150Hz')
                database.insert(sql, sql_data)
            elif "eu sou o" in comando:
                #alexa eu sou o hugo
                #012345678901234
                nome = comando[15:]
                print 'Cadastrando usuário: {}'.format(nome)
            elif "eu me chamo" in comando:
                #alexa eu me chamo hugo
                #012345678901234567
                nome = comando[18:]
                print 'Cadastrando usuário: {}'.format(nome)
            else:
                pass
        except Exception as err:
            f = 'Ocorreu algum erro.'
            a = Pesquise(f)
            a.fala(f)
            print 'Erro: ' + str(err)
    elif 'como esta o clima' in comando or 'qual a temperatura atual' in comando:
        tokenIP = '08e7b32026b7f15eb659455c1eaa09c6'
        tokenCLIMA = 'a6fe231cc95a95d6f6800c29573ba2ac'
        import ip
        import json
        meuIP = ip.meuIp()
        urlIP = 'http://api.ipstack.com/{}?access_key={}&format=1'.format(meuIP, tokenIP)
        #print '[+] URL IP: ' + urlIP
        try:
            request = requests.get(urlIP)
            request = request.json()
            cidade = request['city']
            estado = request['region_code']
        except Exception as err:
            print 'Erro: '+str(err)+'.'
        urlCLIMA = "http://apiadvisor.climatempo.com.br/api/v1/locale/city?name={}&state={}&token={}".format(cidade,estado,tokenCLIMA)
        #print '[+] URL CLIMA (CIDADE ID): ' + urlCLIMA
        try:
            cidadeID = requests.get(urlCLIMA)
            cidadeID = cidadeID.json()
            cidadeID = cidadeID[0]
            cidadeID = cidadeID['id']
            #print '[+] Cidade ID: '+str(cidadeID)
        except Exception as err:
            print 'Erro: '+str(err)+'!'
        urlCLIMA = "http://apiadvisor.climatempo.com.br/api/v1/weather/locale/{}/current?token={}".format(str(cidadeID), tokenCLIMA)
        print '[+] URL CLIMA (DADOS): '+ urlCLIMA
        try:
            restCLIMA = requests.get(urlCLIMA)
            restCLIMA = restCLIMA.json()
            restCLIMA2 = restCLIMA['data']
            frase = 'Para '+str(restCLIMA['name'])+' a temperatura atual e de '+str(restCLIMA2['temperature'])+' graus, sensacao de '+str(restCLIMA2['sensation'])+', previsao de '+str(restCLIMA2['condition'])
            a = Pesquise(frase)
            a.fala(frase)
        except Exception as err:
            print 'Erro: '+str(err)+'!!'
    elif 'gere um cpf' in comando or 'gerar cpf' in comando or 'gerar um cpf' in comando or 'gera um cpf' in comando or 'gera cpf' in comando:
        import json
        from alexa import remover_acentos
        tokenCPF = '995db8c466c13d70b0ff99f922655921'
        urlCPF = 'http://geradorapp.com/api/v1/cpf/generate?token={}'.format(tokenCPF)
        request = requests.get(urlCPF)
        resposta = request.json()
        data = resposta['data']
        if resposta['status'] == "0":
            print '[-] {}'.format(remover_acentos(data['message']))
        elif resposta['status'] == "1":
            print '[+] {}'.format(remover_acentos(data['message']))
            print '[+] Número: {}'.format(data['number'])
            print '[+] Número Formatado: {}'.format(data['number_formatted'])
        else:
            frase = 'Ocorreu algum erro.'
            print '[196] {}'.format(frase)
            a = Pesquise(frase)
            a.fala(frase)
    elif 'aonde fica o cep' in comando or 'onde fica o cep' in comando:
        from cep import buscaCEP
        buscaCEP(comando)
    elif 'localize um ip' in comando or 'localizacao do ip' in comando or 'onde fica o ip' in comando or 'aonde fica o ip' in comando or 'localize o ip' in comando:
        import ip
        tokenIP = '08e7b32026b7f15eb659455c1eaa09c6'
        ip2 = raw_input('Digite o IP: ')
        ip2 = str(ip2)
        print '[+] IP de Busca: \33[32m{}\33[0;0m'.format(ip2)
        ip.localizeIP(ip2,tokenIP)
    elif 'que dia e hoje' in comando or 'qual a data de hoje' in comando:
        from datetime import date
        data_atual = date.today()
        ano = data_atual.year
        mes = data_atual.month
        dia = data_atual.day
        frase = '{} do {} de {}'.format(str(dia),str(mes),str(ano))
    elif 'configure um despertador' in comando or 'me lembre de uma coisa' in comando or 'crie um alarme' in comando or 'me lembre de uma coisa' in comando or 'configure o despertador' in comando:
        nome_alarme = raw_input('Digite o nome do alarme: ')
        frase = 'Digite o dia do evento'
        data_alarme = raw_input('Digite o dia: ')
        hora_alarme = raw_input('Digite a hora: ')
        sql = 'INSERT INTO alexa_alarmes(nome, data, hora) VALUES (%s, %s, %s)'
        sql_data = (nome_alarme, data_alarme, hora_alarme)
        database.insert(sql, sql_data)
        frase = 'Alarme configurado'
        a = Pesquise(frase)
        a.fala(frase)
    elif 'ultimas noticias' in comando or 'noticias do dia' in comando or 'me fale as ultimas noticias' in comando:
        A = Pesquise(comando)
        A.noticias()
    elif 'abra o jogo da velha' in comando or 'jogar jogo da velha' in comando:
        import subprocess
        cmd = ['xterm']
        cmd.extend(['-e', 'cd .. && cd alexa_jogos && ./forca; exec $SHELL'])
    elif 'abra o alarme' in comando or 'abra o script do alarme' in comando or 'abrir alarme' in comando or 'abrir o alarme' in comando:
        import subprocess
        cmd = ['xterm']
        cmd.extend(['-e', 'python alarmes.py; exec $SHELL'])
        subprocess.Popen(cmd, stdout=subprocess.PIPE)
    elif 'mandar um e-mail' in comando or 'mande um e-mail' in comando or 'escrever um e-mail' in comando:
        import subprocess
        cmd = ['xterm']
        cmd.extend(['-e', 'python enviarEmail.py; exec $SHELL'])
        subprocess.Popen(cmd, stdout=subprocess.PIPE)
        cdm = ['xterm']
        cdm.extend(['-e', 'nano mensagem.html; exec $SHELL'])
        subprocess.Popen(cdm, stdout=subprocess.PIPE)
   # elif 'chame um taxi' in comando:
   #
    else:
        frase = 'Eu ainda nao fui programada para isso ... voce poderia me ensinar.'
        a = Pesquise(frase)
        a.fala(frase)
        os.system('python alexa.py')
