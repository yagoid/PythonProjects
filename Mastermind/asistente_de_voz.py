import pyttsx3
import re
import speech_recognition as sr


def indentify_name(text):
    name = None
    patterns = ["me llamo ([A-Za-z]+)", "mi nombre es ([A-Za-z]+)", "^([A-Za-z]+)$"]
    for pattern in patterns:
        try:
            name = re.findall(pattern, text)[0]
        except IndexError:
            pass
    return name


def main():
    engine = pyttsx3.init()
    engine.setProperty("rate", 120)
    engine.setProperty("voice", "spanish")

    engine.say("Hola, ¿como te llamas?")
    engine.runAndWait()

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Puedes hablar")
        audio = r.listen(source)
        text = r.recognize_google(audio, language="es-ES")
        name = indentify_name(text)
        if name:
            engine.say("Encantado de conocerte, {}".format(name))
        else:
            engine.say("Lo siento, pero no me has dicho tu puto nombre")
    engine.runAndWait()


if __name__ == '__main__':
        main()