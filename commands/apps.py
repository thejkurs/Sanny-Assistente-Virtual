# commands/app_launcher.py

import subprocess
import os
from voice import falar
from config import APPLICATIONS_PATHS

def abrir_aplicativo_generico(comando_adicional):

    app_nome_limpo = comando_adicional.strip().lower()

    if app_nome_limpo in APPLICATIONS_PATHS:
        caminho_app = APPLICATIONS_PATHS[app_nome_limpo]
        try:
            falar(f"Abrindo {app_nome_limpo}.")
            subprocess.Popen([caminho_app])
            return True
        except FileNotFoundError:
            falar(f"Não consegui encontrar o arquivo do aplicativo {app_nome_limpo}. Verifique o caminho em 'config.py'.")
            return False
        except Exception as e:
            falar(f"Ocorreu um erro ao tentar abrir o {app_nome_limpo}: {e}")
            return False
    
    else:
        try:
            falar(f"Tentando abrir o aplicativo {app_nome_limpo}.")
            subprocess.Popen([app_nome_limpo])
            return True
        except FileNotFoundError:
            falar(f"Não consegui encontrar o aplicativo {app_nome_limpo}. Verifique se ele está instalado ou se o nome do comando está correto.")
            return False
        except Exception as e:
            falar(f"Ocorreu um erro ao tentar abrir o aplicativo {app_nome_limpo}: {e}")
            return False