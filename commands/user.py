import time
from voice import falar
from commands.apps import abrir_aplicativo_generico
from commands.spotify import abrir_spotify_playlist
from config import PREFERENCES

def iniciar_ambiente_trabalho():

    falar("Iniciando seu ambiente de trabalho.")

    abrir_aplicativo_generico("vscode")
    time.sleep(2)

    abrir_aplicativo_generico("discord")
    time.sleep(2)

    playlist_trabalho_nome = PREFERENCES.get("work_playlist_name", "playlist de trabalho")
    if playlist_trabalho_nome in PREFERENCES:
        abrir_spotify_playlist(playlist_trabalho_nome)
    else:
        falar(f"A playlist '{playlist_trabalho_nome}' não está configurada para o ambiente de trabalho. Verifique suas playlists do Spotify.")

    falar("Ambiente de trabalho iniciado com sucesso!")