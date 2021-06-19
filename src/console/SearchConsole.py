from core.database import find_db, time_search_db, get_all_db
from core.person import print_person
from core.setting import get_search_time
from core.tools import menu_input, yes_or_no, clear


def type_input() -> str:
    while True:
        user_input = input("검색할 항목을 선택하세요. (이름/전화번호/날짜/모두)\n>> ")
        if user_input == "이름" or user_input.lower() == "name":
            return "name"
        elif user_input == "전화번호" or user_input.lower() == "phone":
            return "phone"
        elif user_input == "날짜" or user_input.lower() == "date":
            return "date"
        elif user_input == "모두" or user_input.lower() == "all":
            return "all"
        else:
            print("없는 항목입니다.\n")


def search_person():
    while True:
        clear()
        type = type_input()

        if type == "all":
            persons = get_all_db()
        else:
            print()
            value = input("검색할 내용을 입력하세요.\n>> ")

            persons = find_db(type, value)

        print_person(persons, index=True)

        if persons != []:
            select = menu_input(
                f"선택한 사람으로부터 {get_search_time()} 시간 동안 출입한 사람을 검색합니다", 0, len(persons)-1)

            time_persons = time_search_db(persons[select])
            print_person(time_persons)

        if yes_or_no("다시 검색하시겠습니까?"):
            continue
        else:
            return
