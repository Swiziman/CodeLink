import os
import tkinter as tk
from tkinter import messagebox
import subprocess
import webbrowser

server_process = None

def start_server():
    global server_process
    # Caminho para a virtual environment
    venv_path = os.path.join(os.getcwd(), 'venv', 'Scripts', 'activate')
    # Ative a virtual environment e inicie o servidor Django
    command = f'{venv_path} && python manage.py runserver'
    server_process = subprocess.Popen(command, shell=True)

def stop_server():
    global server_process
    # Pare o servidor Django se estiver sendo executado
    if server_process:
        server_process.terminate()
        server_process = None

def confirm_start():
    # Exiba uma mensagem de confirmação para iniciar o servidor
    if messagebox.askyesno("Iniciar Servidor", "Deseja iniciar o servidor CodeLink?"):
        start_server()

def confirm_stop():
    # Exiba uma mensagem de confirmação para parar o servidor
    if messagebox.askyesno("Parar Servidor", "Deseja parar o servidor CodeLink?"):
        stop_server()
        root.destroy() # Fecha o programa depois de parar o servidor

def open_server():
    # Abra o link no navegador padrão
    webbrowser.open("http://127.0.0.1:8000/")

# Crie a janela principal
root = tk.Tk()
root.title("CodeLink")

# Verifique se a imagem de fundo existe
background_image_path = "background_image.png"
if not os.path.exists(background_image_path):
    messagebox.showerror("Erro", f"Imagem de fundo não encontrada: {background_image_path}")
    root.destroy()  # Feche o programa se a imagem não for encontrada
else:
    # Carregue a imagem de fundo
    background_image = tk.PhotoImage(file=background_image_path)
    background_label = tk.Label(root, image=background_image)
    background_label.place(relwidth=1, relheight=1)

# Defina o tamanho da janela
root.geometry("600x400")

# Crie um frame para os botões
button_frame = tk.Frame(root, bg="white", bd=5)
button_frame.place(relx=0.5, rely=0.5, anchor="center")

# Adicione botões para iniciar e parar o servidor
button_bg = "#f0f0f0"  # Cor de fundo dos botões
button_fg = "#000000"  # Cor do texto dos botões

start_button = tk.Button(button_frame, text="Iniciar Servidor", command=confirm_start, width=20, height=2, bg=button_bg, fg=button_fg)
start_button.grid(row=0, column=0, padx=10, pady=10)

# Adicione botão para abrir o servidor no navegador
open_button = tk.Button(button_frame, text="Abrir Servidor", command=open_server, width=20, height=2, bg=button_bg, fg=button_fg)
open_button.grid(row=1, column=0, padx=10, pady=10)

stop_button = tk.Button(button_frame, text="Parar Servidor e Fechar", command=confirm_stop, width=20, height=2, bg=button_bg, fg=button_fg)
stop_button.grid(row=2, column=0, padx=10, pady=10)

# Execute a interface gráfica
root.mainloop()
