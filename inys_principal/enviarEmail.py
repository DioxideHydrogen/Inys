import urllib
from bs4 import BeautifulSoup
from pesquisas import Pesquise
import tkinter as tk
from tkinter import ttk

LARGE_FONT= ("Verdana", 12)
NORM_FONT = ("Helvetica", 10)
SMALL_FONT = ("Helvetica", 8)

def popupmsg(msg):
    popup = tk.Tk()
    popup.wm_title("Email")
    label = ttk.Label(popup, text=msg, font=NORM_FONT)
    label.pack(side="top", fill="x", pady=10)
    B1 = ttk.Button(popup, text="Okay", command = popup.destroy)
    B1.pack()
    popup.mainloop()

def main():
    sender = raw_input("Remetente > ")
    to = raw_input("Para > ")
    subject = raw_input("Assunto > ")
    message_text = raw_input("Arquivo > ")
    arquivo = open(message_text)
    message_text = arquivo.read()
    parametros = urllib.urlencode({'emailMain': sender,'email': to,'assunto': subject ,'mensagem': message_text})
    html = urllib.urlopen('http://autoup.esy.es/layer0/mail_send.php',parametros)
    return html
if __name__ == '__main__':
    soup = main()
    soup = BeautifulSoup(soup, 'html.parser')
    confirma = str(soup.find('p'))
    confirma = confirma[3:35]
    if confirma == 'O e-mail foi enviado com sucesso':
        msg = 'O e-mail foi enviado com sucesso.'
        popupmsg(msg)
    else:
        msg = 'Erro ao enviar email'
        popupmsg(msg)



    