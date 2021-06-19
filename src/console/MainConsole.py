from console.EntryLogConsole import input_person
from console.SearchConsole import search_person
from console.SettingConsole import setting_menu
from core.tools import menu_input, clear, yes_or_no


def main_menu():
    while True:
        clear()
        print("메인메뉴\n")

        print("1. 출입명부 작성")
        print("2. 출입자 검색")
        print("3. 환경설정")
        print("4. 프로그램 종료\n")

        select = menu_input("메뉴를 선택하세요", 1, 4)

        if select == 1:
            input_person()
        elif select == 2:
            search_person()
        elif select == 3:
            setting_menu()
        elif select == 4:
            print()
            if yes_or_no("정말 종료하시겠습니까?"):
                return
