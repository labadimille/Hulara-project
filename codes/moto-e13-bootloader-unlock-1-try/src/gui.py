# src/gui.py
import tkinter as tk
from tkinter import messagebox
import main

def esegui_azione():
    comando = entry_comando.get()
    risultato = main.avvia_comando(comando)
    messagebox.showinfo("Hulara Output", risultato)

# Configurazione Finestra
root = tk.Tk()
root.title("Hulara Project GUI")
root.geometry("300x200")

label = tk.Label(root, text="Nome Script:")
label.pack(pady=10)

entry_comando = tk.Entry(root)
entry_comando.pack()

btn = tk.Button(root, text="Avvia", command=esegui_azione)
btn.pack(pady=20)

root.mainloop()
