import customtkinter
from tkinter import messagebox


def apertar(numero):
    """
    Recebe o botao apertado e o escreve na tela.
    :param numero: int
    """
    cont = 0
    global cliques
    if numero == '.' and cliques == '':
        numero = ''
    if numero == '.' and '.' in cliques:
        if '+' in cliques or '-' in cliques or '*' in cliques or '/' in cliques:
            cliques = cliques + str(numero)
            reverso = cliques[::-1]
            for k, i in enumerate(reverso):
                if i in '+-*/':
                    for y in range(0, k):
                        if '.' in reverso[y]:
                            cont += 1
                            if cont == 2:
                                cliques = cliques[:-1]
                    break
    else:
        cliques = cliques + str(numero)
    tecla_aparecer.set(cliques)


def igual():
    """
    Resolve a conta matematica apos apertar o botao igual, e mostra na tela o resultado.
    """
    global cliques
    try:
        valor = str(eval(cliques))
        if '.' in valor and valor[-2] == '.' and valor[-1] == '0':
            valor = str(round(float(valor)))
            tecla_aparecer.set(valor)
        else:
            if '.' in valor:
                valor = str(round(float(valor), 6))
                tecla_aparecer.set(valor)
            else:
                tecla_aparecer.set(valor)
        cliques = valor
    except ZeroDivisionError:
        messagebox.showerror(message="Não é possível dividir por zero")


def limpar():
    """
    Limpa toda a tela da calculadora.
    """
    global cliques
    cliques = ""
    tecla_aparecer.set("")


def apagar_ultimo():
    """
    Apaga o ultimo caracter da tela da calculadora.
    """
    global cliques
    cliques = cliques[:-1]
    tecla_aparecer.set(cliques)


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")
janela = customtkinter.CTk()
janela.wm_attributes('-toolwindow', 'true')
janela.geometry("233x280")
janela.title("Calculadora")
cliques = ""
tecla_aparecer = customtkinter.StringVar()

tela = customtkinter.CTkLabel(janela, textvariable=tecla_aparecer, font=("Arial", 30), height=50, width=230,
                              justify='right')
tela.pack(pady=4)

botoes = customtkinter.CTkFrame(janela, height=233, width=275)
botoes.pack()

botao_limpar = customtkinter.CTkButton(botoes, text="C", height=40, width=172, command=lambda: limpar(),
                                       fg_color="#566573")
botao_limpar.place(x=1, y=0)

botao1 = customtkinter.CTkButton(botoes, text="1", height=40, width=55, command=lambda: apertar(1),
                                 fg_color="#566573")
botao1.place(x=1, y=45)

botao2 = customtkinter.CTkButton(botoes, text="2", height=40, width=55, command=lambda: apertar(2),
                                 fg_color="#566573")
botao2.place(x=60, y=45)

botao3 = customtkinter.CTkButton(botoes, text="3", height=40, width=55, command=lambda: apertar(3),
                                 fg_color="#566573")
botao3.place(x=119, y=45)

botao4 = customtkinter.CTkButton(botoes, text="4", height=40, width=55, command=lambda: apertar(4),
                                 fg_color="#566573")
botao4.place(x=1, y=90)

botao5 = customtkinter.CTkButton(botoes, text="5", height=40, width=55, command=lambda: apertar(5),
                                 fg_color="#566573")
botao5.place(x=60, y=90)

botao6 = customtkinter.CTkButton(botoes, text="6", height=40, width=55, command=lambda: apertar(6),
                                 fg_color="#566573")
botao6.place(x=119, y=90)

botao7 = customtkinter.CTkButton(botoes, text="7", height=40, width=55, command=lambda: apertar(7),
                                 fg_color="#566573")
botao7.place(x=1, y=135)

botao8 = customtkinter.CTkButton(botoes, text="8", height=40, width=55, command=lambda: apertar(8),
                                 fg_color="#566573")
botao8.place(x=60, y=135)

botao9 = customtkinter.CTkButton(botoes, text="9", height=40, width=55, command=lambda: apertar(9),
                                 fg_color="#566573")
botao9.place(x=119, y=135)

botao0 = customtkinter.CTkButton(botoes, text="0", height=40, width=55, command=lambda: apertar(0),
                                 fg_color="#566573")
botao0.place(x=60, y=180)

botao_dividir = customtkinter.CTkButton(botoes, text="/", height=40, width=55, command=lambda: apertar('/'),
                                        fg_color="#566573")
botao_dividir.place(x=178, y=0)

botao_multiplicar = customtkinter.CTkButton(botoes, text="*", height=40, width=55, command=lambda: apertar('*'),
                                            fg_color="#566573")
botao_multiplicar.place(x=178, y=45)

botao_subtracao = customtkinter.CTkButton(botoes, text="-", height=40, width=55, command=lambda: apertar('-'),
                                          fg_color="#566573")
botao_subtracao.place(x=178, y=90)

botao_adicao = customtkinter.CTkButton(botoes, text="+", height=40, width=55, command=lambda: apertar('+'),
                                       fg_color="#566573")
botao_adicao.place(x=178, y=135)

botao_igual = customtkinter.CTkButton(botoes, text="=", height=40, width=55, command=lambda: igual(),
                                      fg_color="#566573")
botao_igual.place(x=178, y=180)

botao_ponto = customtkinter.CTkButton(botoes, text=".", height=40, width=55, command=lambda: apertar('.'),
                                      fg_color="#566573")
botao_ponto.place(x=119, y=180)

botao_apagar_ultimo = customtkinter.CTkButton(botoes, text="apagar", height=40, width=55,
                                              command=lambda: apagar_ultimo(), fg_color="#566573")
botao_apagar_ultimo.place(x=1, y=180)

janela.mainloop()

