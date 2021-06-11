# 몇시간으로 설정할지 질문한다 정수 입력받기
# 아무것도 입력 안 할시 2시간으로 설정하기
# db파일 어디다 저장할지 물어본다
# 입력받는다
from core.tools import int_input


def setting_menu():
    while True:
        print("=================================")
        print("환경설정")
        print("1. 검색 범위 설정")
        print("2. database 저장 위치")
        print("=================================")

        select = int_input("환경설정에서 설정할 것을 선택해주세요:")

        if select == 1:
            set_search_range()

        elif select == 2:
            set_db_location()


def set_search_range():
    try:
        int(input("검색할 시간을 설정하세요."))
    except:
        print("시간이 경과하여 2시간으로 설정합니다.")


def set_db_location():
    print("원하는 폴더를 정하세요.")
