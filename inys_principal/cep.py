#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
import requests
from acentos import remover_acentos
import json
from pesquisas import *
token = '995db8c466c13d70b0ff99f922655921'
url = 'http://geradorapp.com/api/v1/cep/search/{}?token={}'

"""

      {
          "status": "0",
          "data": {
              "number": "Cep informado na busca",
              "message": "Nenhuma informação encontrada para o CEP"
          }
      }


      {
          "status": "1",
          "data": {
              "state": "SP",
              "state_name": "São Paulo",
              "city": "Cidade",
              "district": "Bairro",
              "abbreviated_district": "Bairro abreviado",
              "address": "Nome do logradouro (Rua/Avenida)",
              "abbreviated_address": "Nome do logradouro abreviado",
              "address_name": "Nome do local",
              "city_code": "Código IBGE da cidade",
              "number": "Cep informado na busca",
              "number_formatted": "Cep informado na busca formatado",
              "message": "Mensagem"
          }
      }
"""

def buscaCEP(comando):
    global url
    if 'alexa aonde fica o cep' in comando:
        comando = comando[23:]
        print '[+] CEP: {}'.format(comando)
        cep = comando.replace('-','')
        print '[+] CEP FORMATADO: {}'.format(cep)
        url = url.format(cep,token)
        request = requests.get(url)
        resposta = request.json()
        data = resposta['data']
        if resposta['status'] == "0":
            print '[-] {}'.format(remover_acentos(data['message']))
        elif resposta['status'] == "1":
            print '[+] {}'.format(remover_acentos('CEP ENCONTRADO'))
            frase = 'No estado de {} na cidade de {}'.format(remover_acentos(data['state_name']), remover_acentos(data['city']))
            a = Pesquise(frase)
            a.fala(frase)
        else:
            frase = 'Ocorreu algum erro.'
            print '[60] {}'.format(frase)
            a = Pesquise(frase)
            a.fala(frase) 
    elif 'alexa onde fica o cep' in comando:
        comando = comando[23:]
        print '[+] CEP: {}'.format(comando)
        cep = comando.replace('-','')
        print '[+] CEP FORMATADO: {}'.format(cep)
        url = url.format(cep,token)
        request = requests.get(url)
        resposta = request.json()
        data = resposta['data']
        if resposta['status'] == "0":
            print '[-] {}'.format(remover_acentos(data['message']))
        elif resposta['status'] == "1":
            print '[+] {}'.format(remover_acentos('CEP ENCONTRADO'))
            frase = 'No estado de {} na cidade de {}'.format(remover_acentos(data['state_name']), remover_acentos(data['city']))
            a = Pesquise(frase)
            a.fala(frase)
        else:
            frase = 'Ocorreu algum erro.'
            print '[81] {}'.format(frase)
            a = Pesquise(frase)
            a.fala(frase)
    elif 'alexia aonde fica o cep' in comando:
        comando = comando[24:]
        print '[+] CEP: {}'.format(comando)
        cep = comando.replace('-','')
        print '[+] CEP FORMATADO: {}'.format(cep)
        url = url.format(cep,token)
        request = requests.get(url)
        resposta = request.json()
        data = resposta['data']
        if resposta['status'] == "0":
            print '[-] {}'.format(remover_acentos(data['message']))
        elif resposta['status'] == "1":
            print '[+] {}'.format(remover_acentos('CEP ENCONTRADO'))
            frase = 'No estado de {} na cidade de {}'.format(remover_acentos(data['state_name']), remover_acentos(data['city']))
            a = Pesquise(frase)
            a.fala(frase)
        else:
            frase = 'Ocorreu algum erro.'
            print '[102] {}'.format(frase)
            a = Pesquise(frase)
            a.fala(frase)
    elif 'alexia onde fica o cep' in comando:
        comando = comando[23:]
        print '[+] CEP: {}'.format(comando)
        cep = comando.replace('-','')
        print '[+] CEP FORMATADO: {}'.format(cep)
        url = url.format(cep,token)
        request = requests.get(url)
        resposta = request.json()
        data = resposta['data']
        if resposta['status'] == "0":
            print '[-] {}'.format(remover_acentos(data['message']))
        elif resposta['status'] == "1":
            print '[+] {}'.format(remover_acentos('CEP ENCONTRADO'))
            frase = 'No estado de {} na cidade de {}'.format(remover_acentos(data['state_name']), remover_acentos(data['city']))
            a = Pesquise(frase)
            a.fala(frase)
        else:
            frase = 'Ocorreu algum erro.'
            print '[123] {}'.format(frase)
            a = Pesquise(frase)
            a.fala(frase)
    else:
        frase = 'Comando para busca de CEP nao foi reconhecido'
        a = Pesquise(frase)
        a.fala(frase)