# 출입 명부 작성
# 개인정보 수집 동의, 이름, 전화번호, 주소 입력받기
from time import sleep
from core.person import Person
from core.database import append_db
from os.path import dirname, abspath
from core.tools import clear, yes_or_no

PRIVACY_DIR_PATH = dirname(
    abspath(dirname(abspath(dirname(__file__))))) + "\Privacy Policy"


def get_privacy_text(type: str) -> str:
    privacy_text = ""
    with open(PRIVACY_DIR_PATH + f"\{type}.txt", mode="r", encoding="utf-8") as file:
        for oneline in file.readlines():
            privacy_text += oneline
    return privacy_text


def input_person():
    while True:
        clear()
        if not yes_or_no("어서오십시오. 입력하시겠습니까?"):
            return

        clear()
        print(get_privacy_text("개인정보 수집 이용 동의"))
        privacy = yes_or_no("개인정보 수집 및 이용에 동의하십니까?",
                            no_false="반드시 동의하셔야 합니다.\n")

        clear()
        print(get_privacy_text("개인정보 제3자 제공 동의"))
        third_privacy = yes_or_no("개인정보 제3자 제공에 동의하십니까?",
                                  no_false="반드시 동의하셔야 합니다.\n")

        clear()
        while True:
            name = input("이름\n>> ")
            print()
            phone = input("전화번호\n>> ")
            print()
            address = input("주소\n>> ")
            print()
            if yes_or_no(f"{name}, {phone}, {address} 맞습니까?"):
                try:
                    new_person = Person(name, phone, address,
                                        privacy, third_privacy)
                except:
                    print()
                    print("입력된 정보가 올바르지 않습니다. 다시 입력하세요.\n")
                    continue

                append_db(new_person)
                print()
                print("성공적으로 입력되었습니다. 잠시 뒤에 자동으로 넘어갑니다.\n")
                print(
                    f"{new_person.get_date()}, {new_person.get_time()}, {new_person.name}, {new_person.phone}, {new_person.address}")
                sleep(5)
                break
            else:
                print()
                continue
