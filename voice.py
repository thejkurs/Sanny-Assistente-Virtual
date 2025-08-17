import os
import pygame
from gtts import gTTS
import logging
import pyttsx3
import tempfile
import speech_recognition as sr

logger = logging.getLogger(__name__)


def falar(texto):
    
    print(f"JARVIS (voz): {texto}")
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as fp:
            filename = fp.name

        tts = gTTS(text=texto, lang='pt', slow=False)
        tts.save(filename)

        pygame.mixer.music.load(filename)
        pygame.mixer.music.play()
        
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
        
        pygame.mixer.music.stop()
        pygame.mixer.music.unload()

        os.remove(filename)

        logger.debug(f"Falou: '{texto}'.")
        
    except Exception as e:
        logger.error(f"Erro ao tentar falar usando gTTS: {e}", exc_info=True)
        print(f"ERRO: Não consegui fazer o Jarvis falar com gTTS. {e}")

def ouvir_comando():
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Ajustando para ruído ambiente...")
        try:
            r.adjust_for_ambient_noise(source, duration=1) 
            print("Nível de ruído ambiente ajustado.")
        except Exception as e:
            logger.warning(f"Não foi possível ajustar para ruído ambiente: {e}")
        
        print("Ouvindo...")
        logger.info("Iniciando escuta de comando.")
        
        try:
            audio = r.listen(source, timeout=60, phrase_time_limit=60) 
            print("Reconhecendo...")
            logger.info("Áudio capturado. Tentando reconhecer.")
            
            comando = r.recognize_google(audio, language='pt-BR')
            print(f"Você disse: {comando}")
            logger.info(f"Comando reconhecido: '{comando}'.")
            return comando.lower()
        except sr.WaitTimeoutError:
            logger.warning("WaitTimeoutError: Nenhuma fala detectada dentro do tempo limite.")
            return ""
        except sr.UnknownValueError:
            logger.warning("UnknownValueError: Não foi possível entender o áudio.")
            return ""
        except sr.RequestError as e:
            logger.error(f"RequestError: Problema na requisição ao serviço Google Speech Recognition; {e}", exc_info=True)
            return ""
        except Exception as e:
            logger.critical(f"Erro inesperado em ouvir_comando: {e}", exc_info=True)
            return ""