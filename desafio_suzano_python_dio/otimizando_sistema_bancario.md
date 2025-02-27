# Otimizando um Sistema Bancário 🏦

##🚀 Desafio

Precisamos deixar nosso código mais modularizado, para isso vamos criar funções para as operações existentes: sacar, 
depositar e visualizar histórico. Além disso, para a versão 2 do nosso sistema precisamos criar duas novas funções: criar usuário (cliente do banco) e criar conta corrente (vincular com usuário)

- Separação em funções: Devemos criar funções para todas as operações do sistema. Para exercitar tudo o que aprendemos
- neste módulo, cada função vai ter uma regra na passagem de argumentos. O retorno e a
- forma como serão chamadas, pode ser definida por você da forma que achar melhor.
- Operação de depósito: A função depósito deve receber os argumentos apenas por posição (positional only). Sugestão de
- argumentos: saldo, valor, extrato. Sugestão de retorno: saldo e extrato.
- Operação de saque: A função saque deve receber os argumentos apenas por nome (keyword only). Sugestão de argumentos:
- saldo, valor, extrato, limite, numero_saques, limite_saques. Sugestão de retorno: saldo e extrato.
- Operação de extrato: A função extrato deve receber os argumentos por posição e nome (positional only e keyword only).
- Argumentos posicionais: saldo, argumentos nomeados: extrato.
- Novas funções: Precisamos crias duas novas funções: criar usuário e criar conta corrente. Fique a vontade para adicionar
- mais funções, exemplo: Listar contas.
- Criar usuário (cliente): O programa deve armazenar os usuários em uma lista, um usuário é composto por: nome, data de
- nascimento, CPF e endereço. O endereço é uma string com o formato: logradouro, numero, bairro, cidade/sigla, estado. Deve ser armazenado somente os números do CPF. Não podemos cadastrar dois usuários com o mesmo CPF.
- Criar conta corrente: O programa deve armazenar contas em uma lista, um conta é composta por: agência, número da conta
- e usuário. O número da conta é sequencial, iniciando em 1. O número da agência é fixo: "0001". O usuário poder ter mais
- de uma conta, mas uma conta pertence a somente um usuário.

## 📒 Objetivo Geral

Separar as funções existentes de saque, depósito e extrato em funções. Criar duas novas funções: cadastrar usuário
(cliente) e cadastrar conta bancária.

##🤖 Tecnologias Utilizadas

- Python como linguagem principal
- Tkinter para criar interfaces gráficas de usuário (GUIs)
- Ferramenta VsCode para codar

##🧐 Processo de Criação

Utilizei o Python como linguagem principal e a biblioteca do Tkinter para criar janelas, botões, caixas de texto, 
menus e outros componentes gráficos. E VScode como ferramenta pois é possivel encontrar tudo no mesmo ambiente.
