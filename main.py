#Importando os módulos
import speedtest
from tkinter import *
from PIL import Image, ImageTk


#Implementando as cores
cor0 = "#000000" #Preto
cor1 = "#feffff" #Branco
cor2 = "#3fb5a3" #Verde
cor3 = "#fc76dd" #Vermelha
cor4 = "#403d3d"
cor5 = "#4a88e8" #Azul
cor6 = "#1c1c1c" #Cinza escuro
cor7 = "#0000cd" #Azul médio


#Criando a aba
aba = Tk()
aba.title("SpeedNet")
aba.geometry("640x360")
aba.configure(background=cor6)
aba.resizable(height=False, width=False)


#Dividindo a tela em 2 frames
frame_logo = Frame(aba, width=640, height=120, bg=cor6)
frame_logo.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)

frame_corpo = Frame(aba, width=640, height=240, bg=cor6)
frame_corpo.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)


#Fazendo as personalizações do Frame Logo
imagem = Image.open("speed_logo.png")
imagem = imagem.resize((65,65))
imagem =  ImageTk.PhotoImage(imagem)

l_logo_imagem = Label(frame_logo, height=120, image=imagem, padx=10, anchor=NE, font=("Ivy 20 bold"), background=cor6, fg=cor1)
l_logo_imagem.place(x=70, y=10)

l_logo_nome = Label(frame_logo, text='| Internet Speed Tester', padx=10, font=("Ivy 28 bold"), bg=cor6, fg=cor7)
l_logo_nome.place(x=130, y=18)

l_linha = Label(frame_logo, width=640, height=0, anchor=NW, font=("Arial 1"), bg=cor7)
l_linha.place(x=0, y=85)


#Função de teste
def main():
    speed = speedtest.Speedtest()
    download = f"{'{:.1f}'.format(speed.download()/1024/1024)}"
    upload = f"{'{:.1f}'.format(speed.upload()/1024/1024)}"

    l_down['text'] = download
    l_up['text'] = upload

    bottao_iniciar['text'] = 'Try again'


#Fazendo a configuração do frame corpo
#Download
l_down = Label(frame_corpo, text='', anchor=NW, font=("Arial 32 bold"), bg=cor6, fg=cor7)
l_down.place(x=105, y=68)
l_down_mbps = Label(frame_corpo, text='Mbps download', anchor=NW, font=("Ivy 12"), bg=cor6, fg=cor7)
l_down_mbps.place(x=90, y=117)

imagem_down = Image.open("down.png")
imagem_down = ImageTk.PhotoImage(imagem_down)

l_down_imagem = Label(frame_corpo, width=88, image=imagem_down, padx=10, anchor=NE, bg=cor6)
l_down_imagem.place(x=213, y=53)


#Upload
l_up = Label(frame_corpo, text='', anchor=NW, font=("Arial 32 bold"), bg=cor6, fg=cor7)
l_up.place(x=438, y=68)
l_up_mbps = Label(frame_corpo, text='Mbps download', anchor=NW, font=("Ivy 12"), bg=cor6, fg=cor7)
l_up_mbps.place(x=428, y=117)

imagem_up = Image.open("up.png")
imagem_up = ImageTk.PhotoImage(imagem_up)

l_up_imagem = Label(frame_corpo, width=88, image=imagem_up, padx=10, anchor=NE, bg=cor6)
l_up_imagem.place(x=340, y=53)


#Botão Iniciar
bottao_iniciar = Button(frame_corpo, command=main, text='Start test', font=("Ivy 12 bold"), relief=RAISED, overrelief=RIDGE, bg=cor7, fg=cor6)
bottao_iniciar.place(x=270, y=200)


aba.mainloop()
