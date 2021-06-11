def main_menu():
    while True:
        print("=========================================")
        print("                 *메인메뉴* ")
        print("     *1.전자출입명부 작성란입니다*")
        print("     *2.출입자를 검색합니다*")
        print("     *3.환경설정입니다*")
        print("     *4.프로그램 종료*")
        print("=========================================")
        print("*메뉴*를 선택하세요 :")

        try:
            select = int(input("메뉴를 선택하세요:"))
        except:
            print("정수를 입력해주세요.")
            continue

        if select == 1:
            None
        elif select == 2:
            None
        elif select == 3:
            None
        elif select == 4:
            if 'y' == input("\n정말 종료하시겠습니까?(Y/N) >>>").lower():
                break
        else:
            print("잘못 입력하셨습니다.")
