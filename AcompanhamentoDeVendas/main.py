import tkinter as tk
from tkinter import messagebox
from calculo import calcular_totais

janela = tk.Tk()
janela.title("Vendas da Loja")

# Títulos das colunas (produtos)
for j in range(3):  # 3 produtos
    label = tk.Label(janela, text=f"Produto {j+1}", font=("Arial", 10, "bold"))
    label.grid(row=0, column=j+1, padx=5, pady=5)

entradas = []

# Linhas com título lateral (semanas)
for i in range(2):  # 2 semanas
    label = tk.Label(janela, text=f"Semana {i+1}", font=("Arial", 10, "bold"))
    label.grid(row=i+1, column=0, padx=5, pady=5)
    
    linha = []
    for j in range(3):
        entrada = tk.Entry(janela, width=5)
        entrada.grid(row=i+1, column=j+1, padx=5, pady=5)
        linha.append(entrada)
    entradas.append(linha)

# Botão
botao = tk.Button(janela, text="Calcular Totais", command=lambda: exibir_resultados())
botao.grid(row=3, column=0, columnspan=4, pady=10)

# Função de cálculo
def exibir_resultados():
    try:
        matriz = []
        for linha in entradas:
            matriz.append([int(caixa.get()) for caixa in linha])
        semana_total, produto_total = calcular_totais(matriz)

        resultado = "Total por Semana:\n"
        for i, total in enumerate(semana_total, start=1):
            resultado += f"Semana {i}: {total}\n"

        resultado += "\nTotal por Produto:\n"
        for i, total in enumerate(produto_total, start=1):
            resultado += f"Produto {i}: {total}\n"

        messagebox.showinfo("Totais", resultado)
    except ValueError:
        messagebox.showerror("Erro", "Insira apenas números inteiros.")

janela.mainloop()
