import tkinter as tk
from tkinter import messagebox

# Função para adicionar transação
def adicionar_transacao():
    tipo = tipo_var.get()
    valor = valor_var.get()

    if not valor.isdigit():
        messagebox.showerror("Erro", "Por favor, insira um valor numérico.")
        return

    valor = float(valor)
    if tipo == "Despesa":
        valor = -valor

    transacoes.append(valor)
    atualizar_saldo()
    lista_transacoes.insert(tk.END, f"{tipo}: R$ {abs(valor):.2f}")
    valor_var.set("")

# Função para atualizar o saldo
def atualizar_saldo():
    saldo = sum(transacoes)
    saldo_var.set(f"Saldo: R$ {saldo:.2f}")

# Configuração inicial do tkinter
root = tk.Tk()
root.title("Controle de Finanças")

# Variáveis
transacoes = []
saldo_var = tk.StringVar()
valor_var = tk.StringVar()

# Layout
frame_principal = tk.Frame(root)
frame_principal.pack(pady=20)

label_saldo = tk.Label(frame_principal, textvariable=saldo_var, font=("Arial", 16))
label_saldo.grid(row=0, column=0, columnspan=2)

tipo_var = tk.StringVar(value="Receita")
tk.Radiobutton(frame_principal, text="Receita", variable=tipo_var, value="Receita").grid(row=1, column=0)
tk.Radiobutton(frame_principal, text="Despesa", variable=tipo_var, value="Despesa").grid(row=1, column=1)

label_valor = tk.Label(frame_principal, text="Valor (R$):")
label_valor.grid(row=2, column=0)

entry_valor = tk.Entry(frame_principal, textvariable=valor_var)
entry_valor.grid(row=2, column=1)

btn_adicionar = tk.Button(frame_principal, text="Adicionar", command=adicionar_transacao)
btn_adicionar.grid(row=3, column=0, columnspan=2)

lista_transacoes = tk.Listbox(root, width=30)
lista_transacoes.pack(pady=10)

# Inicia o saldo com zero
atualizar_saldo()

# Inicia o loop do tkinter
root.mainloop()
