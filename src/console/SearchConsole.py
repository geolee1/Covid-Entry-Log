from core.database import find_db
from core.tools import yes_or_no


def type_input() -> str:
    while True:
        user_input = input("검색할 항목을 선택하세요. (이름/전화번호/날짜)\n>> ")
        if user_input == "이름" or user_input.lower() == "name":
            return "name"
        elif user_input == "전화번호" or user_input.lower() == "phone":
            return "phone"
        elif user_input == "날짜" or user_input.lower() == "date":
            return "date"
        else:
            print("없는 항목입니다.\n")


def search_person():
    while True:
        type = type_input()
        value = input("검색할 내용을 입력하세요.\n>> ")

        persons = find_db(type, value)

        if persons != []:
            print("no\t방문일\t방문시각\t이름\t전화번호\t주소")
            for index in range(len(persons)):
                print(
                    f"#{index}\t{persons.get_date()}\t{persons.get_time()}\t{persons.name}\t{persons.phone}\t{persons.address}")
        else:
            print("검색 결과가 없습니다.\n")

        if yes_or_no("다시 검색하시겠습니까? (Y/N)\n>> "):
            continue
        else:
            return
