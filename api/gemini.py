import google.generativeai as genai
from config import API_KEY_GEMINI
from voice import falar

genai.configure(api_key=API_KEY_GEMINI)

MODELO_GEMINI = genai.GenerativeModel('gemini-1.5-flash')

def perguntar_gemini(pergunta):
    
    try:
        response = MODELO_GEMINI.generate_content(pergunta)
        return response.text.strip()
    except Exception as e:
        falar(f"Erro ao comunicar com o Gemini: {e}")
        return f"Erro ao comunicar com o Gemini: {e}"