import random
import tkinter as tk
from tkinter import messagebox
import tkinter.ttk


# Função para gerar a senha
def generate_password():
    n = int(entry_length.get())
    include_lowercase = var_lowercase.get()
    include_uppercase = var_uppercase.get()
    include_special = var_special.get()
    include_numbers = var_numbers.get()

    # Listas de caracteres
    lowercase = 'abcdefghijklmnopqrstuvwxyz'
    uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    special = '!#$%()*,+-./:;=><?@[\\]^~_`´|{}'
    numbers = '1234567890'

    # Combina todas as listas de caracteres conforme seleção do usuário
    all_characters = ''
    if include_lowercase:
        all_characters += lowercase
    if include_uppercase:
        all_characters += uppercase
    if include_special:
        all_characters += special
    if include_numbers:
        all_characters += numbers

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
root.resizable(False, False)

# Configurações de layout
frame = tk.Frame(root, padx=10, pady=10)
frame.grid(padx=10, pady=5)

# Entrada para o número de caracteres
tk.Label(frame, text='Número de Caracteres').grid(row=2, column=1)
entry_length = tk.Entry(frame)
entry_length.grid(row=3, column=1)
entry_length.insert(0, '8')  # Valor padrão



# Opções para incluir tipos de caracteres
var_lowercase = tk.BooleanVar(value=True)
var_uppercase = tk.BooleanVar(value=True)
var_special = tk.BooleanVar(value=True)
var_numbers = tk.BooleanVar(value=True)
tk.Checkbutton(frame, text='Minúsculas', variable=var_lowercase).grid(row=2, column=0, sticky='w')
tk.Checkbutton(frame, text='Maiúsculas', variable=var_uppercase).grid(row=3, column=0, sticky='w')
tk.Checkbutton(frame, text='Especiais', variable=var_special).grid(row=4, column=0, sticky='w')
tk.Checkbutton(frame, text='Números', variable=var_numbers).grid(row=5, column=0, sticky='w')

# Botão para gerar a senha
tk.Button(frame, text='Gerar Senha', command=generate_password).grid(row=4, column=1, columnspan=2, padx=20)

# Senha gerada
tk.Label(frame).grid(row=7, column=0, columnspan=2)
entry_password = tk.Entry(frame, width=50)
entry_password.grid(row=7, column=0, columnspan=2)
tkinter.ttk.Separator(root, orient='vertical').grid(column=0, row=2, rowspan=3, sticky='ns')
# Inicia a aplicação
root.mainloop()
