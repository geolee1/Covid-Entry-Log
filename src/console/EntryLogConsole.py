# 출입 명부 작성
# 개인정보 수집 동의, 이름, 전화번호, 주소 입력받기
from core.person import Person
from core.database import append_db


def input_person():
    while True:
        print("[개인정보 수집 이용 안내문]")
        answer_is = "n"
        while (answer_is != "y"):
            answer_is = input("개인정보 수집 및 이용에 동의하십니까? (y/n) ")

            if (input == "y"):
                privacy = True
                break
            else:
                print("반드시 동의해야합니다")
                continue

        print("[개인정보 제3자 제공 안내문]\n")
        answer_is = "n"
        while (answer_is != "y"):
            answer_is = input("개인정보 제3자 제공에 동의하십니까? (Y/N) ")

            if input == "y":
                third_privacy = True
                break
            else:
                print("반드시 동의해야합니다")

        # one_person = dict()
        answer_is = "n"
        while (answer_is != "y"):
            name = input("이름: ")
            phone = input("전화번호: ")
            address = input("주소: ")
            # one_person["name"] = input("이름: ")
            # one_person["phone"] = input("전화번호: ")
            # one_person["address"] = input("주소: ")
            # one_person = input(f"{one_person.get('name')}, {one_person.get('phone')}, {one_person.get('address')} 맞습니까? ("Y/N")")
            answer_is = input(f"{name}, {phone}, {address} 맞습니까? (Y/N)")
            if (answer_is != "y"):
                new_person = Person(name, phone, address,
                                    privacy, third_privacy)
                append_db(new_person)
                print("정상적으로 입력되었습니다.")
                # {------------------}
                break

            else:
                print("개인정보를 수정하십시오")
                continue
