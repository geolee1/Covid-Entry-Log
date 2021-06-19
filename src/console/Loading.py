from os.path import isfile
from core.database import create_db
from core.setting import get_path, set_defalut
from console.MainConsole import main_menu
from core.tools import yes_or_no


def load():
    try:
        if not isfile(get_path("Setting.ini")):
            set_defalut()

        if not isfile(get_path("Entry Log.csv")):
            create_db()
    except:
        if yes_or_no("프로그램의 오류가 발생했습니다. 프로그램을 초기화하시겠습니까?"):
            set_defalut()
            create_db()
        else:
            return

    main_menu()
