import pyttsx3
engine = pyttsx3.init()
def listar_voces():
    voices = engine.getProperty('voices')
    for voice in voices:
        print(f"Voice: {voice.name}")
        print(f" - ID: {voice.id}")
        print(f" - Languages: {voice.languages}")
        print(f" - Gender: {voice.gender}")
        print(f" - Age: {voice.age}\n")

listar_voces()