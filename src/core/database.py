from os.path import isfile, isdir
from pathlib import Path
from core.setting import get_path
from core.person import Person
import csv


def create_db():
    database_path = get_path("Database")
    file_path = get_path("Entry Log.csv")

    if not isdir(database_path):
        Path(database_path).mkdir(parents=True, exist_ok=True)

    if isfile(file_path):
        return

    with open(file_path, mode="w", newline='') as database_file:
        writer = csv.writer(database_file)
        writer.writerow(
            ["time", "privacy", "third_privacy", "name", "phone", "address"])


def append_db(one: Person):
    file_path = get_path("Entry Log.csv")
    with open(file_path, mode="a", newline='') as database_file:
        writer = csv.writer(database_file)
        writer.writerow(one.person_info())


def find_db(date: str = "", time: str = "", name: str = "", phone: str = ""):  # 작업해야함
    file_path = get_path("Entry Log.csv")
    with open(file_path, newline='') as database_file:
        reader = csv.reader(database_file)
        raw_DB = []
        for row in reader:
            raw_DB.append(row)
        DB = []
        for one in raw_DB[1:]:
            # DB 리턴을 딕셔너리 리스트로 할때
            # save_dict = {}
            # for no in range(len(one)):
            #     save_dict[raw_DB[0][no]] = oneㄸ[no]
            # DB.append(save_dict)

            # DB 리턴을 Person 클래스 리스트로 할때
            save_person = Person(
                time=one[0], privacy=one[1], third_privacy=one[2], name=one[3], phone=[4], address=one[5])
            DB.append(save_person)
        return DB
