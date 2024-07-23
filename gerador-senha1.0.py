import random
import tkinter as tk
from tkinter import messagebox

# Função para gerar a senha
def generate_password():
    n = int(entry_length.get())
    include_lowercase = var_lowercase.get()
    include_uppercase = var_uppercase.get()
    include_special = var_special.get()

    # Listas de caracteres
    lowercase = 'abcdefghijklmnopqrstuvwxyz'
    uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    special = '!#$%()*,+-./:;=><?@[\\]^~_`´|{}'

    # Combina todas as listas de caracteres conforme seleção do usuário
    all_characters = ''
    if include_lowercase:
        all_characters += lowercase
    if include_uppercase:
        all_characters += uppercase
    if include_special:
        all_characters += special

    # Verifica se pelo menos um tipo de caractere foi selecionado
    if not all_characters:
        messagebox.showerror('Erro', 'Você deve selecionar pelo menos um tipo de caractere.')
    else:
        # Gera a senha
        password = ''.join(random.choice(all_characters) for _ in range(n))
        entry_password.delete(0, tk.END)
        entry_password.insert(0, password)

# Configura a janela principal
root = tk.Tk()
root.title('Gerador de Senha')

# Configurações de layout
frame = tk.Frame(root, padx=10, pady=10)
frame.pack(padx=10, pady=10)

# Entrada para o número de caracteres
tk.Label(frame, text='Quantos caracteres estarão na senha?').grid(row=0, column=0, columnspan=2)
entry_length = tk.Entry(frame)
entry_length.grid(row=1, column=0, columnspan=2)
entry_length.insert(0, '12')  # Valor padrão

# Opções para incluir tipos de caracteres
var_lowercase = tk.BooleanVar(value=True)
var_uppercase = tk.BooleanVar(value=True)
var_special = tk.BooleanVar(value=True)

tk.Checkbutton(frame, text='Incluir letras minúsculas', variable=var_lowercase).grid(row=2, column=0, sticky='w')
tk.Checkbutton(frame, text='Incluir letras maiúsculas', variable=var_uppercase).grid(row=3, column=0, sticky='w')
tk.Checkbutton(frame, text='Incluir caracteres especiais', variable=var_special).grid(row=4, column=0, sticky='w')

# Botão para gerar a senha
tk.Button(frame, text='Gerar Senha', command=generate_password).grid(row=5, column=0, columnspan=2)

# Senha gerada
tk.Label(frame).grid(row=6, column=0, columnspan=2)
entry_password = tk.Entry(frame, width=50)
entry_password.grid(row=7, column=0, columnspan=2)

# Inicia a aplicação
root.mainloop()
