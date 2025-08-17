import pyttsx3

def listar_e_testar_vozes():
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    print("Vozes disponíveis no seu sistema:")
    for i, voice in enumerate(voices):
        print(f"--- Voz {i} ---")
        print(f"  ID: {voice.id}")
        print(f"  Nome: {voice.name}")
        print(f"  Idiomas: {voice.languages}")
        print(f"  Gênero: {'Masculino' if voice.gender == 'male' else 'Feminino' if voice.gender == 'female' else 'Desconhecido'}")
        engine.setProperty('voice', voice.id)
        engine.say(f"Olá, eu sou {voice.name}. Esta é uma amostra da minha voz.")
        engine.runAndWait()
    engine.stop()

listar_e_testar_vozes()