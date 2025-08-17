import os
import pygame
from voice import falar
from config import MUSIC_FOLDER_PATH

try:
    pygame.mixer.init()
except Exception as e:
    print(f"Aviso: Não foi possível inicializar o mixer do Pygame. Funções de música local podem não funcionar. Erro: {e}")

def listar_musicas():
    
    musicas_path = os.path.join(os.path.dirname(__file__), "..", MUSIC_FOLDER_PATH) 
    if not os.path.exists(musicas_path):
        falar("A pasta de músicas não foi encontrada.")
        return []
    
    arquivos = [f for f in os.listdir(musicas_path) if f.lower().endswith(('.mp3', '.wav', '.ogg'))]
    if not arquivos:
        falar("Não encontrei nenhuma música na pasta.")
        return []
    
    falar("As músicas disponíveis são:")
    for i, musica in enumerate(arquivos):
        falar(f"{i+1}. {os.path.splitext(musica)[0]}")
    return arquivos

def tocar_musica(nome_musica):
    
    musicas_path = os.path.join(os.path.dirname(__file__), "..", MUSIC_FOLDER_PATH)
    caminho_completo_musica = os.path.join(musicas_path, nome_musica)
    
    if os.path.exists(caminho_completo_musica):
        try:
            pygame.mixer.music.load(caminho_completo_musica)
            pygame.mixer.music.play()
            falar(f"Tocando {os.path.splitext(nome_musica)[0]}")
            return True
        except pygame.error as e:
            falar(f"Não consegui tocar a música. Erro: {e}")
            return False
    else:
        falar(f"A música {os.path.splitext(nome_musica)[0]} não foi encontrada.")
        return False

def parar_musica():

    if pygame.mixer.music.get_busy():
        pygame.mixer.music.stop()
        falar("Música parada.")
    else:
        falar("Nenhuma música está tocando no momento.")