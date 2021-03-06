import platform
import os


class PhoneNumberError(Exception):
    def __str__(self) -> str:
        return "전화번호가 올바르지 않습니다."


def check_phone_number(phone: str) -> bool:  # 전화번호 형식 확인 함수
    prefixs = [
        '010',  # 이동전화
        '011',  # 이동전화
        '016',  # 이동전화
        '017',  # 이동전화
        '018',  # 이동전화
        '019',  # 이동전화
        '02',  # 서울특별시 지역번호
        '031',  # 경기도 지역번호
        '032',  # 인천광역시 지역번호
        '033',  # 강원도 지역번호
        '041',  # 충청남도 지역번호
        '042',  # 대전광역시 지역번호
        '043',  # 충청북도 지역번호
        '044',  # 세종특별자치시 지역번호
        '051',  # 부산광역시 지역번호
        '052',  # 울산광역시 지역번호
        '053',  # 대구광역시 지역번호
        '054',  # 경상북도 지역번호
        '055',  # 경상남도 지역번호
        '061',  # 전라남도 지역번호
        '062',  # 광주광역시 지역번호
        '063',  # 전라북도 지역번호
        '064',  # 제주특별자치시도 지역번호
        '070'  # 인터넷 전화
    ]
    phone = get_phone_onlynum(phone)

    if len(phone) <= 6 or len(phone) > 11:  # 전화번호 길이가 맞는지 확인
        # print("전화번호길이아님")  # 테스트코드
        return False

    if len(phone) > 8:  # 000-0000-0000 형태의 전화번호 일때
        for one_prefix in prefixs:
            if one_prefix in phone[:3]:
                if one_prefix == '02':
                    if len(phone) > 10:  # 서울특별시 전화번호일때 길이가 더 긴 것 제외
                        return False
                    phone = phone[2:]
                else:
                    phone = phone[3:]
                break
    # print(f"현재전화번호 {phone}")  # 테스트코드

    if phone[0] == '0' or phone[0] == '1':  # 국번호는 2부터 9까지의 숫자로 시작
        # print("국번호 틀림")  # 테스트코드
        return False

    return True


def get_phone_onlynum(phone: str) -> str:
    result = phone.replace('-', '').replace(' ', '')  # 숫자로만 이루어진 형태로 변환
    try:  # 입력된 정보가 정수인지 확인
        int(result)
        return result
    except:
        # print("정수아님")  # 테스트코드
        raise PhoneNumberError


def num_input(string: str) -> int:
    while True:
        user_input = input(f"{string}\n>> ")
        try:
            return int(user_input)
        except:
            print("숫자를 입력해 주세요.\n")
            continue


def menu_input(string: str, start_num: int, end_num: int) -> int:
    while True:
        result = num_input(string)
        if result < start_num:
            print("숫자가 너무 작습니다.\n")
        elif result > end_num:
            print("숫자가 너무 큽니다.\n")
        else:
            return result


def yes_or_no(string: str = "Y/N \n>> ", no_false: str = None) -> bool:
    while True:
        user_input = input(f"{string} (Y/N)\n>> ")
        if user_input.lower() == "y" or user_input.lower() == "yes":
            return True
        elif user_input.lower() == "n" or user_input.lower() == "no":
            if no_false is not None:
                print(no_false)
                continue
            return False
        else:
            print("잘못 입력하셨습니다.\n")
            continue


def clear():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")
