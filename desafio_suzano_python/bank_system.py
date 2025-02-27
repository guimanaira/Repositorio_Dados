import tkinter as tk
from tkinter import messagebox

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

def depositar():
    global saldo, extrato
    try:
        valor = float(entry_valor.get())
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            messagebox.showinfo("Sucesso", f"Depósito de R$ {valor:.2f} realizado!")
        else:
            messagebox.showerror("Erro", "O valor informado é inválido.")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, informe um valor numérico.")
    entry_valor.delete(0, tk.END)

def sacar():
    global saldo, extrato, numero_saques
    try:
        valor = float(entry_valor.get())
        if valor > saldo:
            messagebox.showerror("Erro", "Você não tem saldo suficiente.")
        elif valor > limite:
            messagebox.showerror("Erro", "O valor do saque excede o limite.")
        elif numero_saques >= LIMITE_SAQUES:
            messagebox.showerror("Erro", "Número máximo de saques excedido.")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            messagebox.showinfo("Sucesso", f"Saque de R$ {valor:.2f} realizado!")
        else:
            messagebox.showerror("Erro", "O valor informado é inválido.")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, informe um valor numérico.")
    entry_valor.delete(0, tk.END)

def exibir_extrato():
    global saldo, extrato
    extrato_texto = extrato if extrato else "Não foram realizadas movimentações."
    extrato_texto += f"\nSaldo: R$ {saldo:.2f}"
    messagebox.showinfo("Extrato", extrato_texto)

def sair():
    root.destroy()

# Interface Tkinter
root = tk.Tk()
root.title("Sistema Bancário")

frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

label_valor = tk.Label(frame, text="Informe o valor:")
label_valor.pack()

entry_valor = tk.Entry(frame)
entry_valor.pack()

btn_depositar = tk.Button(frame, text="Depositar", command=depositar)
btn_depositar.pack(fill='x')

btn_sacar = tk.Button(frame, text="Sacar", command=sacar)
btn_sacar.pack(fill='x')

btn_extrato = tk.Button(frame, text="Exibir Extrato", command=exibir_extrato)
btn_extrato.pack(fill='x')

btn_sair = tk.Button(frame, text="Sair", command=sair)
btn_sair.pack(fill='x')

root.mainloop()
