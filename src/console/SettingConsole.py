# 몇시간으로 설정할지 질문한다 정수 입력받기
# 아무것도 입력 안 할시 2시간으로 설정하기
# db파일 어디다 저장할지 물어본다
# 입력받는다
from time import sleep
from core.setting import change_database_path, change_search_time, get_search_time, get_path
from core.tools import clear, menu_input


def setting_menu():
    while True:
        clear()
        print("환경설정\n")

        print("1. 검색 범위 설정")
        print("2. DB 저장 위치 설정")
        print("3. 돌아가기\n")

        select = menu_input("메뉴를 선택하세요", 1, 3)

        if select == 1:
            set_search_range()
        elif select == 2:
            set_db_location()
        elif select == 3:
            return


def set_search_range():
    print(f"현재 설정된 시간 : {get_search_time()} 시간\n")
    set_hour = menu_input("검색할 시간을 설정하세요 (1~24, 취소하려면 0)", 0, 24)

    if set_hour == 0:
        print()
        print("취소되었습니다.")
        sleep(3)
        return

    change_search_time(set_hour)
    print()
    print("성공적으로 설정되었습니다. 잠시 뒤 메뉴로 돌아갑니다.")
    print(f"현재 설정된 시간 : {get_search_time()} 시간\n")
    sleep(5)
    return


def set_db_location():
    print(f"현재 설정된 경로 : {get_path('Database')}\n")
    new_path = input("바꿀 경로를 입력하세요 (폴더경로 입력, 취소하려면 0)\n>> ")

    if new_path == '0':
        print()
        print("취소되었습니다.")
        sleep(3)
        return

    if change_database_path(new_path):
        print()
        print("성공적으로 설정되었습니다. 잠시 뒤 메뉴로 돌아갑니다.")
        print(f"현재 설정된 경로 : {get_path('Database')}\n")
        sleep(5)
    return
