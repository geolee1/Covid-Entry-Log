from configparser import ConfigParser
from os import getenv
from os.path import isfile, isdir
from pathlib import Path
from shutil import move


def get_search_time() -> int:
    setting = ConfigParser()
    setting.read(get_path("Setting.ini"))
    return int(setting["Find"].get("search_time"))


def get_path(name: str = None) -> str:
    if name == "Setting.ini":
        return getenv("APPDATA") + f"\\Entry Logger\\Setting\\Setting.ini"

    elif name == "Setting":
        return getenv("APPDATA") + "\\Entry Logger\\Setting"

    elif name == "Entry Log.csv":
        setting = ConfigParser()
        setting.read(get_path("Setting.ini"))
        return setting["Database"].get("path") + "\\Entry Log.csv"

    elif name == "Database":
        setting = ConfigParser()
        setting.read(get_path("Setting.ini"))
        return setting["Database"].get("path")

    else:
        return getenv("APPDATA") + "\\Entry Logger"


def set_defalut():
    if not isdir(get_path("Setting")):
        Path(get_path("Setting")).mkdir(parents=True, exist_ok=True)

    database_path = get_path() + "\\Database"
    search_time = 2

    setting = ConfigParser()
    setting["Database"] = {"path": database_path}
    setting["Find"] = {"search_time": search_time}

    with open(get_path("Setting.ini"), mode="w") as setting_file:
        setting.write(setting_file)


def change_database_path(new_path: str):
    setting_path = get_path("Setting.ini")

    try:
        if not isdir(new_path):
            Path(new_path).mkdir(parents=True, exist_ok=True)

        setting = ConfigParser()
        setting.read(setting_path)

        old_path = setting["Database"].get("path")
        setting["Database"]["path"] = new_path
        with open(setting_path, mode="w") as setting_file:
            setting.write(setting_file)

        if isfile(old_path + "\\Entry Log.csv"):
            move(old_path + "\\Entry Log.csv", new_path + "\\Entry Log.csv")

        return True

    except:
        print("주소가 잘못되었습니다\n")
        return False


def change_search_time(new_hour: int):
    setting_path = get_path("Setting.ini")

    setting = ConfigParser()
    setting.read(setting_path)

    setting["Find"]["search_time"] = str(new_hour)

    with open(setting_path, mode="w") as setting_file:
        setting.write(setting_file)
