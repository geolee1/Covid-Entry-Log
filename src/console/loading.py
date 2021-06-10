from os.path import isfile
from core.database import create_db
from core.setting import get_path, set_defalut
from console.MainConsole import main_menu


def load():
    if not isfile(get_path("Setting.ini")):
        set_defalut()

    if not isfile(get_path("Entry Log.csv")):
        create_db()

    main_menu()
