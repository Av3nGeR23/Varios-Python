import tkinter as tk
from tkinter import messagebox
from cryptography.fernet import Fernet


#Este código crea una aplicación gráfica en Python usando la biblioteca tkinter 
#que permite encriptar y desencriptar texto utilizando el algoritmo de cifrado simétrico AES 
#a través de la librería cryptography.


def encrypt_text():
    plaintext = plaintext_var.get().encode()
    key = Fernet.generate_key()
    cipher_suite = Fernet(key)
    ciphertext = cipher_suite.encrypt(plaintext)
    ciphertext_var.set(ciphertext.decode())
    key_var.set(key.decode())

def decrypt_text():
    ciphertext = ciphertext_var.get().encode()
    user_key = user_key_entry.get().encode()
    try:
        cipher_suite = Fernet(user_key)
        plaintext = cipher_suite.decrypt(ciphertext)
        plaintext_var.set(plaintext.decode())
    except Exception as e:
        messagebox.showerror("Error", "Error al desencriptar el texto: {}".format(str(e)))

def clear_text():
    plaintext_var.set("")

def clear_ciphertext():
    ciphertext_var.set("")
    key_var.set("")

root = tk.Tk()
root.title("Encriptador y Desencriptador AES")

# Estilo
bg_color = "#f9f9f9"
text_color = "#333333"
button_color = "#3498db"
button_hover_color = "#2980b9"
entry_bg_color = "#ecf0f1"
entry_fg_color = "#2c3e50"
font_style = ("Helvetica", 12)

root.configure(bg=bg_color)

plaintext_var = tk.StringVar()
ciphertext_var = tk.StringVar()
key_var = tk.StringVar()

plaintext_label = tk.Label(root, text="Texto a encriptar:", bg=bg_color, fg=text_color, font=font_style)
plaintext_entry = tk.Entry(root, textvariable=plaintext_var, bg=entry_bg_color, fg=entry_fg_color, font=font_style)
ciphertext_label = tk.Label(root, text="Texto encriptado:", bg=bg_color, fg=text_color, font=font_style)
ciphertext_entry = tk.Entry(root, textvariable=ciphertext_var, bg=entry_bg_color, fg=entry_fg_color, font=font_style)
key_label = tk.Label(root, text="Clave generada:", bg=bg_color, fg=text_color, font=font_style)
key_entry = tk.Entry(root, textvariable=key_var, state='readonly', bg=entry_bg_color, fg=entry_fg_color, font=font_style)
user_key_label = tk.Label(root, text="Clave de desencriptación:", bg=bg_color, fg=text_color, font=font_style)
user_key_entry = tk.Entry(root, bg=entry_bg_color, fg=entry_fg_color, font=font_style)
encrypt_button = tk.Button(root, text="Encriptar", bg=button_color, fg="#ffffff", font=font_style, 
                           command=encrypt_text, activebackground=button_hover_color)
decrypt_button = tk.Button(root, text="Desencriptar", bg=button_color, fg="#ffffff", font=font_style, 
                           command=decrypt_text, activebackground=button_hover_color)
clear_button = tk.Button(root, text="Borrar Texto", bg=button_color, fg="#ffffff", font=font_style, 
                         command=clear_text, activebackground=button_hover_color)
clear_ciphertext_button = tk.Button(root, text="Limpiar Cifrado", bg=button_color, fg="#ffffff", font=font_style, 
                                    command=clear_ciphertext, activebackground=button_hover_color)

plaintext_label.grid(row=0, column=0, sticky='e', padx=5, pady=5)
plaintext_entry.grid(row=0, column=1, columnspan=2, sticky='we', padx=5, pady=5)
ciphertext_label.grid(row=1, column=0, sticky='e', padx=5, pady=5)
ciphertext_entry.grid(row=1, column=1, columnspan=2, sticky='we', padx=5, pady=5)
key_label.grid(row=2, column=0, sticky='e', padx=5, pady=5)
key_entry.grid(row=2, column=1, columnspan=2, sticky='we', padx=5, pady=5)
user_key_label.grid(row=3, column=0, sticky='e', padx=5, pady=5)
user_key_entry.grid(row=3, column=1, columnspan=2, sticky='we', padx=5, pady=5)
encrypt_button.grid(row=4, column=1, padx=5, pady=5)
decrypt_button.grid(row=4, column=2, padx=5, pady=5)
clear_button.grid(row=5, column=1, padx=5, pady=5)
clear_ciphertext_button.grid(row=5, column=2, padx=5, pady=5)

root.mainloop()
