import datetime
import webbrowser
from voice import falar

def mostrar_hora():
    
    agora = datetime.datetime.now().strftime("%H:%M")
    falar(f"Agora são {agora}")

def abrir_google():

    webbrowser.open("https://google.com")
    falar("Abrindo Google")

def encerrar_sanny():
    
    falar("Encerrando o assistente. Até logo!")
    exit()