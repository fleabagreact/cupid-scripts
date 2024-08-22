import tkinter as tk
from tkinter import messagebox
import random

def clicou_sim():
    messagebox.showinfo("Aviso", "Tamo junto, galado!")

def mover_nao():
    x = random.randint(0, largura_janela - largura_nao)
    y = random.randint(0, altura_janela - altura_nao)
    botao_nao.place(x=x, y=y)

def clicou_nao(event):
    mover_nao()

def definir_cores_rosa():
    cor_fundo = "#FFB6C1"
    cor_botao = "#FF69B4"
    janela.configure(bg=cor_fundo)
    rotulo_mensagem.configure(bg=cor_fundo)
    botao_sim.configure(bg=cor_botao, activebackground=cor_botao, state=tk.NORMAL, cursor="hand2")
    botao_nao.configure(bg="#C71585", activebackground="#C71585", activeforeground="white")

janela = tk.Tk()
janela.title("Título Modificado")

largura_janela = 400
altura_janela = 400

janela.geometry(f"{largura_janela}x{altura_janela}")
cor_fundo_padrao = janela.cget("bg")

mensagem_texto = "Você veria o musical de Mean Girls com essa aluna de informática? Você veria?"

fonte_negrito = ("Calibri", 12, "bold")

rotulo_mensagem = tk.Label(janela, text=mensagem_texto, font=fonte_negrito, fg="white", bg=cor_fundo_padrao, wraplength=150, highlightthickness=0, pady=10)
rotulo_mensagem.pack(pady=10)

botao_sim = tk.Button(janela, text="Sim", command=clicou_sim, relief=tk.RAISED, bd=3, padx=10, pady=5, fg="white", bg="#FFB6C1", activebackground="#FFB6C1", activeforeground="white", cursor="hand2")
botao_nao = tk.Button(janela, text="Não", command=clicou_nao, cursor="hand2", relief=tk.RAISED, bd=3, padx=10, pady=5, fg="white", bg="#C71585", activebackground="#C71585", activeforeground="white")
botao_nao.bind("<Enter>", lambda event: mover_nao())

largura_nao = botao_nao.winfo_reqwidth()
altura_nao = botao_nao.winfo_reqheight()

botao_sim.pack(pady=20)
botao_nao.pack()

definir_cores_rosa()

janela.mainloop()