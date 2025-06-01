import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
from calculo import calcular_totais

# Configurações globais
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("green")

# Janela principal
janela = ctk.CTk()
janela.title("Vendas da Loja")
janela.geometry("600x400")
janela.resizable(False, False)
janela.configure(fg_color="#add8e6")  # Azul claro

# Permitir apenas números
def somente_numeros(texto):
    return texto.isdigit() or texto == ""

vcmd = janela.register(somente_numeros)

# Título
titulo = ctk.CTkLabel(janela, text="Vendas Semanais", font=("Segoe UI", 18, "bold"), bg_color="transparent")
titulo.place(relx=0.5, y=20, anchor="n")

# Cabeçalhos
for j in range(3):
    label = ctk.CTkLabel(janela, text=f"Produto {j + 1}", font=("Segoe UI", 12, "bold"), bg_color="transparent")
    label.place(x=170 + j * 100, y=60)

entradas = []

# Entradas por semana
for i in range(2):
    semana_label = ctk.CTkLabel(janela, text=f"Semana {i + 1}", font=("Segoe UI", 12), bg_color="transparent")
    semana_label.place(x=70, y=100 + i * 60)

    linha = []
    for j in range(3):
        entrada = ctk.CTkEntry(
            janela, 
            width=80, 
            corner_radius=10, 
            fg_color="white",
            validate="key",
            validatecommand=(vcmd, "%P")
        )
        entrada.place(x=170 + j * 100, y=100 + i * 60)
        linha.append(entrada)
    entradas.append(linha)

# Função para calcular e mostrar totais
def exibir_resultados():
    try:
        matriz = []
        for linha in entradas:
            nova_linha = []
            for caixa in linha:
                valor = caixa.get().strip()
                if not valor.isdigit():
                    raise ValueError("Todos os campos devem conter números inteiros.")
                nova_linha.append(int(valor))
            matriz.append(nova_linha)

        semana_total, produto_total = calcular_totais(matriz)

        resultado_janela = ctk.CTkToplevel(janela)
        resultado_janela.title("Totais")
        resultado_janela.geometry("320x360")
        resultado_janela.resizable(False, False)
        resultado_janela.configure(fg_color="#add8e6")  # Azul claro

        ctk.CTkLabel(resultado_janela, text="Totais", font=("Segoe UI", 16, "bold"), bg_color="transparent").pack(pady=(15, 10))

        ctk.CTkLabel(resultado_janela, text="Total por Semana:", font=("Segoe UI", 12, "bold"), bg_color="transparent").pack(pady=(5, 0))
        for i, total in enumerate(semana_total, start=1):
            ctk.CTkLabel(resultado_janela, text=f"Semana {i}: {total}", font=("Segoe UI", 12),
                         fg_color="white", text_color="black", corner_radius=10, width=200, height=30).pack(pady=5)

        ctk.CTkLabel(resultado_janela, text="Total por Produto:", font=("Segoe UI", 12, "bold"), bg_color="transparent").pack(pady=(15, 0))
        for i, total in enumerate(produto_total, start=1):
            ctk.CTkLabel(resultado_janela, text=f"Produto {i}: {total}", font=("Segoe UI", 12),
                         fg_color="white", text_color="black", corner_radius=10, width=200, height=30).pack(pady=5)

    except ValueError as e:
        messagebox.showerror("Erro", str(e))

# Botão de cálculo
botao = ctk.CTkButton(
    janela,
    text="Calcular Totais",
    command=exibir_resultados,
    corner_radius=20,
    fg_color="#00cc99",
    hover_color="#00b386",
    text_color="white"
)
botao.place(relx=0.5, y=300, anchor="center")

janela.mainloop()
