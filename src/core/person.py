from time import localtime, strftime
from core.tools import checkPhoneNumber


class PrivacyError(Exception):
    def __str__(self) -> str:
        return "개인정보 수집 및 이용에 동의해주세요."


class ThirdPrivacyError(Exception):
    def __str__(self) -> str:
        return "개인정보 제3자 제공에 동의해주세요."


class PhoneNumberError(Exception):
    def __str__(self) -> str:
        return "전화번호가 올바르지 않습니다."


class Person:
    # name: str  # 성명 (Name)
    # phone: str  # 휴대전화번호 (Phone)
    # address: str  # 시군구(거주지) (Address)
    # __privacy: bool  # 개인정보 수집 동의 (Privacy Policy Agreement)
    # __third_privacy: bool  # 개인정보 제3자 제공 동의 (Privacy Policy Agreement)
    # covid: bool  # 확진 여부 (Covid-19 Confirmed)
    # __time  # 방문시간 (Time of Visit) YYYY-MM-DD/HH:MM:SS
    def __init__(self, name, phone, address, privacy, third_privacy, time: str = None) -> None:
        if privacy and third_privacy:
            if not checkPhoneNumber(phone):
                raise PhoneNumberError
            self.name = name
            self.phone = phone
            self.address = address
            self.__privacy = privacy
            self.__third_privacy = third_privacy
            if time == None:
                self.__time = strftime("%Y-%m-%d/%H:%M:%S", localtime())
            else:
                self.__time = time
        else:
            if not privacy:
                raise PrivacyError
            if not third_privacy:
                raise ThirdPrivacyError

    def person_info(self) -> list:
        return [self.__time, self.__privacy, self.__third_privacy, self.name, self.phone, self.address]

    def get_date(self) -> str:
        return self.__time.split("/")[0]

    def get_time(self) -> str:
        return self.__time.split("/")[1]

    def get_privacy(self) -> bool:
        return self.__privacy

    def get_third_privacy(self) -> bool:
        return self.__third_privacy
