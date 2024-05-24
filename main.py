from tkinter import *
from tkinter import ttk  # necessário para combobox: selecionar opção
from tkinter import messagebox

janela = Tk()
    
def voltar_inicio():
    frame = Frame(janela, background="#4B3621")
    frame.place(relx=0.30, rely=0.27, anchor='center', relwidth=0.5, relheight=0.30)

    info_frame = LabelFrame(frame, bg="#4B3621")
    info_frame.grid(row=1, column=0)

    titulo_label = Label(info_frame, text="BEM VINDO AO TESTE DE IMC!", font=("Georgia"), bg="#4B3621", fg="white")
    titulo_label.grid(row=0, column=0, columnspan=3, pady=16)

    nome_label = Label(info_frame, text="Primeiro nome:", font=("Georgia"), bg="#4B3621", fg="white")
    nome_label.grid(row=1, column=0)
    nome_entry = Entry(info_frame)
    nome_entry.grid(row=2, column=0, padx=16, pady=8)

    idade_label = Label(info_frame, text="Idade:", font=("Georgia"), bg="#4B3621", fg="white")
    idade_label.grid(row=1, column=1)
    idade_spinbox = Spinbox(info_frame, from_=1, to=110)
    idade_spinbox.grid(row=2, column=1, padx=16, pady=8)

    peso_label = Label(info_frame, text="Peso (em kg):", font=("Georgia"), bg="#4B3621", fg="white")
    peso_label.grid(row=1, column=2)
    peso_entry = Entry(info_frame)
    peso_entry.grid(row=2, column=2, padx=16, pady=8)

    altura_label = Label(info_frame, text="Altura (em m):", font=("Georgia"), bg="#4B3621", fg="white")
    altura_label.grid(row=3, column=0)
    altura_entry = Entry(info_frame)
    altura_entry.grid(row=4, column=0, padx=16, pady=8)

    genero_title = Label(info_frame, text="Gênero:", font=("Georgia"), bg="#4B3621", fg="white")
    genero_title.grid(row=3, column=1)
    genero_combobox = ttk.Combobox(info_frame, values=["Masculino", "Feminino"])
    genero_combobox.grid(row=4, column=1, padx=16, pady=8)

    enviar = Button(info_frame, text="Enviar", command=entrada_dados)
    enviar.grid(row=4, column=2)

    
def imc(peso_salvo, altura_salvo, idade_salvo, genero_salvo):
    imc_calculo = float(peso_salvo) / float(altura_salvo) ** 2
    if genero_salvo == "Masculino" and idade_salvo >= 21:
        if imc_calculo < 20.7:
            return "abaixo do peso!"
        elif 20.7 <= imc_calculo < 26.4:
            return "com peso normal!"
        elif 26.4 <= imc_calculo < 27.8:
            return "marginalmente acima do peso!"
        elif 27.8 <= imc_calculo < 31.1:
            return "acima do peso ideal!"
        elif imc_calculo >= 31.1:
            return "obeso!"

    if genero_salvo == "Masculino" and idade_salvo < 21:
        if imc_calculo < 19.1:
            return "abaixo do peso!"
        elif 19.1 <= imc_calculo < 25.8:
            return "com peso normal!"
        elif 25.8 <= imc_calculo < 27.3:
            return "marginalmente acima do peso!"
        elif 27.3 <= imc_calculo < 32.3:
            return "acima do peso ideal!"
        elif imc_calculo >= 32.3:
            return "obeso!"

    if genero_salvo == "Feminino" and idade_salvo >= 21:
        if imc_calculo < 19.1:
            return "abaixo do peso!"
        elif 19.1 <= imc_calculo < 25.8:
            return "com peso normal!"
        elif 25.8 <= imc_calculo < 27.8:
            return "marginalmente acima do peso!"
        elif 27.8 <= imc_calculo < 32.3:
            return "acima do peso ideal!"
        elif imc_calculo >= 32.3:
            return "obesa!"

    if genero_salvo == "Feminino" and idade_salvo < 21:
        if imc_calculo < 20.7:
            return "abaixo do peso!"
        elif 20.7 <= imc_calculo < 26.4:
            return "com peso normal!"
        elif 26.4 <= imc_calculo < 27.3:
            return "marginalmente acima do peso!"
        elif 27.3 <= imc_calculo < 31.1:
            return "acima do peso ideal!"
        elif imc_calculo >= 31.1:
            return "obesa!"

def entrada_dados():
    nome_salvo = nome_entry.get()
    idade_salvo = idade_spinbox.get()
    peso_salvo = peso_entry.get()
    altura_salvo = altura_entry.get()
    genero_salvo = genero_combobox.get()

    if not idade_salvo.isdigit():
        messagebox.showwarning(title="Idade", message="Coloque apenas números em idade!")
        return
    elif not peso_salvo.replace(".", "", 1).isdigit() or peso_salvo.isalpha():
        messagebox.showwarning(title="Peso", message="Coloque apenas números em peso!")
        return
    elif not altura_salvo.replace(".", "", 1).isdigit() or altura_salvo.isalpha():
        messagebox.showwarning(title="Altura", message="Coloque apenas números em altura!")
        return
    elif genero_salvo not in ["Masculino", "Feminino"]:
        messagebox.showwarning(title="Gênero", message="Escolha uma das duas opções de gênero!")
        return

    idade_salvo = int(idade_salvo)
    peso_salvo = float(peso_salvo)
    altura_salvo = float(altura_salvo)

    imc_calculo = float(peso_salvo) / float(altura_salvo) ** 2
    resultado_imc = imc(peso_salvo, altura_salvo, idade_salvo, genero_salvo)

    print(nome_salvo, idade_salvo, peso_salvo, altura_salvo, genero_salvo, "\n", "-" * 25)
    frame_resultado = Frame(janela, background="#4B3621")
    frame_resultado.place(relx=0.30, rely=0.27, anchor='center', relwidth=0.5, relheight=0.30)

    info_frame_resultado = LabelFrame(frame_resultado, bg="#4B3621")
    info_frame_resultado.grid(row=1, column=0)

    titulo_label_resultado = Label(info_frame_resultado, text=("{}\n\nSeu IMC é {:.2f} e você está {}".format(nome_salvo, imc_calculo, resultado_imc)), font=("Georgia"), bg="#4B3621", fg="white")
    titulo_label_resultado.grid(row=0, column=0, columnspan=3, pady=60, padx=88)
    
    voltar = Button(info_frame_resultado, text="Voltar", command=voltar_inicio)
    voltar.place(relx=0.78, rely=0.8, relwidth=0.2, relheight=0.17)

image_name = PhotoImage(file="C:\\Users\\Júlia\\Desktop\\Nova pasta\\bmi.png")
img_bg = Label(janela, image=image_name)
img_bg.place(relwidth=1, relheight=1)

frame = Frame(janela, background="#4B3621")
frame.place(relx=0.30, rely=0.27, anchor='center', relwidth=0.5, relheight=0.30)

info_frame = LabelFrame(frame, bg="#4B3621")
info_frame.grid(row=1, column=0)

titulo_label = Label(info_frame, text="BEM VINDO AO TESTE DE IMC!", font=("Georgia"), bg="#4B3621", fg="white")
titulo_label.grid(row=0, column=0, columnspan=3, pady=16)

nome_label = Label(info_frame, text="Primeiro nome:", font=("Georgia"), bg="#4B3621", fg="white")
nome_label.grid(row=1, column=0)
nome_entry = Entry(info_frame)
nome_entry.grid(row=2, column=0, padx=16, pady=8)

idade_label = Label(info_frame, text="Idade:", font=("Georgia"), bg="#4B3621", fg="white")
idade_label.grid(row=1, column=1)
idade_spinbox = Spinbox(info_frame, from_=1, to=110)
idade_spinbox.grid(row=2, column=1, padx=16, pady=8)

peso_label = Label(info_frame, text="Peso (em kg):", font=("Georgia"), bg="#4B3621", fg="white")
peso_label.grid(row=1, column=2)
peso_entry = Entry(info_frame)
peso_entry.grid(row=2, column=2, padx=16, pady=8)

altura_label = Label(info_frame, text="Altura (em m):", font=("Georgia"), bg="#4B3621", fg="white")
altura_label.grid(row=3, column=0)
altura_entry = Entry(info_frame)
altura_entry.grid(row=4, column=0, padx=16, pady=8)

genero_title = Label(info_frame, text="Gênero:", font=("Georgia"), bg="#4B3621", fg="white")
genero_title.grid(row=3, column=1)
genero_combobox = ttk.Combobox(info_frame, values=["Masculino", "Feminino"])
genero_combobox.grid(row=4, column=1, padx=16, pady=8)

enviar = Button(info_frame, text="Enviar", command=entrada_dados, width=8, height=1)
enviar.grid(row=4, column=2)

janela.title("Teste de IMC")
janela.geometry("1000x650")
janela.resizable(0, 0)
janela.iconphoto(0, PhotoImage(file="C:\\Users\\Júlia\\Desktop\\Nova pasta\\bmi1.png"))

janela.mainloop()
