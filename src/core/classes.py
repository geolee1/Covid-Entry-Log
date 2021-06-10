from time import localtime
from core.tools import checkPhoneNumber, get_setting_dir
import csv


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
    # privacy: bool  # 개인정보 수집 동의 (Privacy Policy Agreement)
    # third_privacy: bool  # 개인정보 제3자 제공 동의 (Privacy Policy Agreement)
    # covid: bool  # 확진 여부 (Covid-19 Confirmed)
    # __time  # 방문시간 (Time of Visit)
    def __init__(self):
        None

    def add_person(self, name, phone, address, privacy, third_privacy) -> None:
        if privacy and third_privacy:
            if not checkPhoneNumber(phone):
                raise PhoneNumberError
            self.name = name
            self.phone = phone
            self.address = address
            self.privacy = privacy
            self.third_privacy = third_privacy
            self.__date = localtime()
            self.__time = localtime()
        else:
            if not privacy:
                raise PrivacyError
            if not third_privacy:
                raise ThirdPrivacyError

    def saveDB(self) -> None:
        setting_dir = get_setting_dir('Setting.ini')
        setting_file = open(setting_dir)

    def getDate(self) -> str:
        return self.__date

    def getTime(self) -> str:
        return self.__time
