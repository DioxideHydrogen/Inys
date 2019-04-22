#!/usr/bin/python2.6
# -*- coding: utf8 -*-

#import speech
from wit import Wit
import speech_recognition as sr
import os
import interacoes
import unicodedata
from pesquisas import *
import subprocess

# Iniciar o Alarme da Alexa (Implica em uma janela a cada reinicialização da Alexa)
#
#cmd = ['xterm']
#cmd.extend(['-e', 'python alarmes.py; exec $SHELL' ])
#subprocess.Popen(cmd, stdout=subprocess.PIPE)

def remover_acentos(text):
    try:
        text = unicode(text, 'utf-8')
    except (TypeError, NameError): # unicode is a default on python 3
        pass
    text = unicodedata.normalize('NFD', text)
    text = text.encode('ascii', 'ignore')
    text = text.decode("utf-8")
    return str(text)

microfone = sr.Recognizer()#Habilita o microfone para ouvir o usuario
client = Wit("QLX725BK7TKR7ETZVDULHBWQ4SD5FT4J")
#speech.say("Alexa presente", speed=82, pitch=32, throat=145, mouth=145)

try:
    with sr.Microphone() as source:
        microfone.adjust_for_ambient_noise(source) #Chama a funcao de reducao de ruido disponivel na speech_recognition
        while True:
            print("Diga alguma coisa: ") #Avisa ao usuario que esta pronto para ouvir
            audio = microfone.listen(source) #Armazena a informacao de audio na variavel
            frase = microfone.recognize_google(audio,language='pt-BR') #Passa o audio para o reconhecedor de padroes do speech_recognition
            #frase = frase.encode('utf-8')
            #frase = str(frase)
            frase = remover_acentos(frase)
            frase = frase.lower()
            print("Você disse: " + frase) #Após alguns segundos, retorna a frase falada
            client.message(frase)
            interacoes.interacao(frase)
except KeyboardInterrupt:
    print('Inys está indo durmir') #Caso seja interrompida CTRL+C
except Exception as err:
    print("Não entendi") #Caso nao tenha reconhecido o padrao de fala, exibe esta mensagem
    print(str(err))
    os.system('python inys.py') # Auto execução da Alexa caso ela não entenda
