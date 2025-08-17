from voice import falar, ouvir_comando
from api.gemini import perguntar_gemini
from commands.cmds import mostrar_hora, abrir_google, encerrar_sanny
from commands.apps import abrir_aplicativo_generico
from commands.spotify import abrir_spotify_app, abrir_spotify_playlist, listar_playlists_spotify
from commands.music import listar_musicas, tocar_musica, parar_musica
from commands.user import iniciar_ambiente_trabalho
from config import PLAYLISTS_SPOTIFY, APPLICATIONS_PATHS
import os
import pygame
import logging
import re
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

log_dir = os.path.join(os.path.dirname(__file__), "logs")
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

log_file_path = os.path.join(log_dir, "sanny.log")

logging.basicConfig(
    filename=log_file_path,
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

logger = logging.getLogger(__name__)
logger.info("sanny iniciado.")

COMANDOS = {
    
    r"que horas s(ao|ão)|me diga a hora|mostrar a hora": lambda: mostrar_hora(),
    r"abrir (google|navegador)": lambda: abrir_google(),
    r"encerrar|sair": lambda: encerrar_sanny(),
    r"abrir spotify": lambda: abrir_spotify_app(),
    r"listar playlists (spotify|do spotify)|quais playlists (spotify|do spotify)": lambda: listar_playlists_spotify(),
    r"listar m(ú|u)sicas|quais m(ú|u)sicas": lambda: listar_musicas(),
    r"parar m(ú|u)sica|pausar m(ú|u)sica": lambda: parar_musica(),
    r"iniciar ambiente de trabalho|acorda o papai chegou": lambda: iniciar_ambiente_trabalho(),
    
    r"abrir aplicativo (.+)": lambda app_name: abrir_aplicativo_generico(app_name),
    r"tocar m(ú|u)sica (.+)": lambda music_name: tocar_musica(music_name),
    r"tocar playlist spotify (.+)": lambda playlist_name: abrir_spotify_playlist(playlist_name)
}

last_gemini_response = ""
PALAVRAS_CHAVE_ASSISTENTE = ["sanny", "sunny", "sune", "sun", "sani", "sany", "saniy", "saniye", "saniyeh"]

def executar_comando(comando):
    
    global last_gemini_response
    comando_tratado = False
    
    comando = comando.lower()

    primeira_palavra = comando.split()[0] if comando.split() else ""
    if primeira_palavra:
        melhor_correspondencia, similaridade = process.extractOne(primeira_palavra, PALAVRAS_CHAVE_ASSISTENTE)

        if similaridade > 80:
            comando = comando.replace(primeira_palavra, "sanny", 1)

    for pattern, acao in COMANDOS.items():
        match = re.search(pattern, comando)
        if match:
            args = match.groups()
            acao(*args)
            comando_tratado = True
            break
    
    if comando_tratado:
        last_gemini_response = ""
        return

    if any(x in comando for x in ["me responda", "me responde", "responda", "responde", "sanny", "fale sobre"]):
        pergunta = comando
        for chave in ["me responda", "me responde", "responda", "responde", "sanny", "fale sobre"]:
            pergunta = pergunta.replace(chave, "", 1)
        pergunta = pergunta.strip()

        if pergunta:
            if any(palavra in pergunta for palavra in ["sobre isso", "o que mais", "continue", "e"]):
                pergunta = last_gemini_response + " " + pergunta
            
            if len(pergunta.split()) < 3 and len(pergunta) < 10 and not any(palavra in pergunta for palavra in ["sobre isso", "o que mais", "continue", "e"]):
                falar("Não entendi a sua pergunta completa. Você pode repetir a frase?")
                logger.warning(f"Pergunta muito curta para o Gemini: '{pergunta}'")
            else:
                resposta = perguntar_gemini(pergunta)
                falar(resposta)
                last_gemini_response = resposta
                logger.info(f"Pergunta ao Gemini: '{pergunta}'. Resposta: '{resposta[:50]}...'")
        else:
            falar("Por favor, faça uma pergunta depois do comando.")
            logger.warning("Comando Gemini invocado sem pergunta.")
        comando_tratado = True
    
    if not comando_tratado and any(x in comando for x in ["sanny", "me responda", "me responde", "responda", "responde"]):
        falar("Comando não reconhecido. Você pode tentar de novo ou me fazer uma pergunta.")
        logger.warning(f"Comando não reconhecido: '{comando}'.")
    
    if not any(x in comando for x in ["me responda", "me responde", "responda", "responde", "sanny", "fale sobre"]):
        last_gemini_response = ""
    

if __name__ == "__main__":
    falar("Olá, eu sou a Sanny, sua Assistente Virtual. Como posso ajudar?")
    logger.info("Mensagem de boas-vindas falada.")
    while True:
        comando = ouvir_comando()
        if comando:
            logger.info(f"Comando recebido: '{comando}'.")
            executar_comando(comando)
        else:
            logger.debug("Nenhum comando reconhecido ou áudio inválido (timeout/unknown value).")
            pass