import webbrowser
import subprocess
from voice import falar
from config import PLAYLISTS_SPOTIFY

def abrir_spotify_app():

    falar("Abrindo o Spotify.")
    try:
        subprocess.Popen(["start", "spotify:"], shell=True)
        return True
    except Exception as e:
        falar(f"Não consegui abrir o Spotify. Erro: {e}")
        print(f"Erro ao tentar abrir Spotify via URI: {e}")
        return False

def abrir_spotify_playlist(nome_playlist):

    url_playlist = PLAYLISTS_SPOTIFY.get(nome_playlist.lower())
    
    if url_playlist:
        falar(f"Abrindo o Spotify e tocando a playlist {nome_playlist}.")
        webbrowser.open(url_playlist)
        return True
    else:
        falar(f"Não encontrei a playlist {nome_playlist} na sua lista. Por favor, verifique as playlists cadastradas.")
        return False

def listar_playlists_spotify():

    if not PLAYLISTS_SPOTIFY:
        falar("Nenhuma playlist do Spotify cadastrada.")
        return

    falar("As playlists do Spotify cadastradas são:")
    for nome in PLAYLISTS_SPOTIFY.keys():
        falar(nome)