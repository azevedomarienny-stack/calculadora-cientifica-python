import customtkinter as ctk
import math


# CONFIGURAÇÃO


ctk.set_appearance_mode("light")

janela = ctk.CTk()
janela.geometry("430x760")
janela.title("Calculadora Científica")


# VISOR


expressao = ""

visor = ctk.CTkTextbox(
    janela,
    height=100,
    font=("Consolas", 32, "bold"),
    corner_radius=20,
    fg_color="#fff0f6",
    text_color="#ff1493"
)

visor.pack(
    fill="x",
    padx=15,
    pady=15
)

# FUNÇÕES


def atualizar_visor(texto):

    visor.delete("1.0", "end")
    visor.insert("end", texto)

def clicar(valor):

    global expressao

    expressao += valor

    atualizar_visor(expressao)

def limpar():

    global expressao

    expressao = ""

    atualizar_visor(expressao)

def apagar():

    global expressao

    expressao = expressao[:-1]

    atualizar_visor(expressao)

def calcular():

    global expressao

    try:

        conta = expressao

        conta = conta.replace("π", str(math.pi))
        conta = conta.replace("^", "**")
        conta = conta.replace("√", "math.sqrt")
        conta = conta.replace("sin", "math.sin")
        conta = conta.replace("cos", "math.cos")
        conta = conta.replace("tan", "math.tan")
        conta = conta.replace("log", "math.log10")

        resultado = str(eval(conta))

        expressao = resultado

        atualizar_visor(resultado)

    except:

        atualizar_visor("ERRO")

        expressao = ""


# BOTÕES

botoes = [

    ["(", ")", "[", "]"],
    ["{", "}", "⌫", "C"],

    ["sin", "cos", "tan", "/"],
    ["log", "√", "^", "*"],

    ["7", "8", "9", "-"],
    ["4", "5", "6", "+"],
    ["1", "2", "3", "="],

    ["π", "0", ".", ""]

]


# GRID


frame_principal = ctk.CTkFrame(
    janela,
    fg_color="transparent"
)

frame_principal.pack(
    expand=True,
    fill="both",
    padx=10,
    pady=10
)

for i in range(8):
    frame_principal.rowconfigure(i, weight=1)

for j in range(4):
    frame_principal.columnconfigure(j, weight=1)


# CRIAR BOTÕES


for linha, conteudo in enumerate(botoes):

    for coluna, texto in enumerate(conteudo):

        if texto == "":
            continue

        if texto == "=":
            comando = calcular

        elif texto == "C":
            comando = limpar

        elif texto == "⌫":
            comando = apagar

        else:
            comando = lambda x=texto: clicar(x)

        botao = ctk.CTkButton(

            frame_principal,

            text=texto,

            command=comando,

            font=("Arial", 22, "bold"),

            corner_radius=25,

            fg_color="#ff69b4",

            hover_color="#ff1493",

            height=70
        )

        botao.grid(
            row=linha,
            column=coluna,
            padx=6,
            pady=6,
            sticky="nsew"
        )

# LOOP


janela.mainloop()