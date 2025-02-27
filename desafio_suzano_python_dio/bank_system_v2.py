import tkinter as tk
from tkinter import messagebox

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
usuarios = []
contas = []
AGENCIA = "0001"

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        messagebox.showinfo("Sucesso", f"Depósito de R$ {valor:.2f} realizado!")
    else:
        messagebox.showerror("Erro", "O valor informado é inválido.")
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        messagebox.showerror("Erro", "Você não tem saldo suficiente.")
    elif excedeu_limite:
        messagebox.showerror("Erro", "O valor do saque excede o limite.")
    elif excedeu_saques:
        messagebox.showerror("Erro", "Número máximo de saques excedido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        messagebox.showinfo("Sucesso", f"Saque de R$ {valor:.2f} realizado!")
    else:
        messagebox.showerror("Erro", "O valor informado é inválido.")
    return saldo, extrato, numero_saques

def exibir_extrato(saldo, /, *, extrato):
    extrato_texto = extrato if extrato else "Não foram realizadas movimentações."
    extrato_texto += f"\nSaldo: R$ {saldo:.2f}"
    messagebox.showinfo("Extrato", extrato_texto)

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_usuario():
    cpf = entry_cpf.get()
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        messagebox.showerror("Erro", "Já existe usuário com esse CPF!")
        return

    nome = entry_nome.get()
    data_nascimento = entry_data_nascimento.get()
    endereco = entry_endereco.get()

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    messagebox.showinfo("Sucesso", "Usuário criado com sucesso!")

def criar_conta():
    cpf = entry_cpf_conta.get()
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        numero_conta = len(contas) + 1
        contas.append({"agencia": AGENCIA, "numero_conta": numero_conta, "usuario": usuario})
        messagebox.showinfo("Sucesso", "Conta criada com sucesso!")
    else:
        messagebox.showerror("Erro", "Usuário não encontrado!")

def listar_contas():
    if not contas:
        messagebox.showinfo("Contas", "Nenhuma conta cadastrada.")
    else:
        lista = "".join([f"Agência: {conta['agencia']}\nConta: {conta['numero_conta']}\nTitular: {conta['usuario']['nome']}\n---\n" for conta in contas])
        messagebox.showinfo("Contas", lista)

def abrir_tela_principal():
    global saldo, extrato, numero_saques
    tela_principal = tk.Toplevel(root)
    tela_principal.title("Sistema Bancário - Operações")

    frame_principal = tk.Frame(tela_principal)
    frame_principal.pack(padx=20, pady=20)

    tk.Label(frame_principal, text="Informe o valor:").pack()
    global entry_valor
    entry_valor = tk.Entry(frame_principal)
    entry_valor.pack()

    tk.Button(frame_principal, text="Depositar", command=lambda: atualizar_saldo_depositar()).pack(fill='x')
    tk.Button(frame_principal, text="Sacar", command=lambda: atualizar_saldo_sacar()).pack(fill='x')
    tk.Button(frame_principal, text="Exibir Extrato", command=lambda: exibir_extrato(saldo, extrato=extrato)).pack(fill='x')
    tk.Button(frame_principal, text="Listar Contas", command=listar_contas).pack(fill='x')
    tk.Button(frame_principal, text="Sair", command=tela_principal.destroy).pack(fill='x')

def atualizar_saldo_depositar():
    global saldo, extrato
    valor = float(entry_valor.get())
    saldo, extrato = depositar(saldo, valor, extrato)

def atualizar_saldo_sacar():
    global saldo, extrato, numero_saques
    valor = float(entry_valor.get())
    saldo, extrato, numero_saques = sacar(saldo=saldo, valor=valor, extrato=extrato, limite=limite, numero_saques=numero_saques, limite_saques=LIMITE_SAQUES)

root = tk.Tk()
root.title("Sistema Bancário - Cadastro")

frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

label_nome = tk.Label(frame, text="Nome Completo:")
label_nome.pack()
entry_nome = tk.Entry(frame)
entry_nome.pack()

label_data_nascimento = tk.Label(frame, text="Data de Nascimento:")
label_data_nascimento.pack()
entry_data_nascimento = tk.Entry(frame)
entry_data_nascimento.pack()

label_cpf = tk.Label(frame, text="CPF:")
label_cpf.pack()
entry_cpf = tk.Entry(frame)
entry_cpf.pack()

label_endereco = tk.Label(frame, text="Endereço:")
label_endereco.pack()
entry_endereco = tk.Entry(frame)
entry_endereco.pack()

btn_novo_usuario = tk.Button(frame, text="Novo Usuário", command=criar_usuario)
btn_novo_usuario.pack(fill='x')

label_cpf_conta = tk.Label(frame, text="CPF para criar conta:")
label_cpf_conta.pack()
entry_cpf_conta = tk.Entry(frame)
entry_cpf_conta.pack()

btn_nova_conta = tk.Button(frame, text="Nova Conta", command=criar_conta)
btn_nova_conta.pack(fill='x')

btn_proxima_tela = tk.Button(frame, text="Ir para Operações", command=abrir_tela_principal)
btn_proxima_tela.pack(fill='x')

root.mainloop()
