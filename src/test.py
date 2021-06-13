from genericpath import isfile
from core.database import append_db, create_db, find_db
from core.person import Person
from core.setting import get_path, set_defalut

file_path = get_path("Setting.ini")
if not isfile(file_path):
    set_defalut()

print(file_path)

if not isfile(get_path("Entry Log.csv")):
    create_db()

# one = Person("이지오", "010-3019-6324", "서울시 강남구", True, True)
# append_db(one)

DB = find_db()

print(DB)
for one in DB:
    print(one.person_info())
