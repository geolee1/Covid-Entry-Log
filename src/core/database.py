from os.path import isfile, isdir
from pathlib import Path
from core.setting import get_path
from core.person import Person
from core.tools import get_phone_onlynum
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


def find_db(type: str, value):  # 작업해야함
    persons = get_all_db()

    value = value.strip().replace(' ', '')
    find = []
    if type == "name":
        for person in persons:
            if value == person.name:
                find.append(person)
    elif type == "phone":
        for person in persons:
            if get_phone_onlynum(value) == get_phone_onlynum(person.phone):
                find.append(person)
    elif type == "date":
        for person in persons:
            if value == person.get_date():
                find.append(person)
    else:
        raise TypeError

    return find


def get_all_db() -> list:
    file_path = get_path("Entry Log.csv")
    with open(file_path, newline='') as database_file:
        reader = csv.reader(database_file)
        raw_DB = []
        for row in reader:
            raw_DB.append(row)
        DB = []
        for one in raw_DB[1:]:
            saved_person = Person(
                time=one[0], privacy=one[1], third_privacy=one[2], name=one[3], phone=one[4], address=one[5])
            DB.append(saved_person)
        return DB
