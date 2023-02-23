def data_format():
    with open("save.txt", "r", encoding="UTF-8") as saved_info:
        return saved_info.readlines()[0].split()


def show_all():
    with open("save.txt", "r", encoding="UTF-8") as saved_info:
        for line in saved_info:
            print(line)
    main_menu()

def import_new_data():
    print("Ввод новых данных.")
    new_line = ""
    for i in data_format():
        print("Введите ", i, ": ", sep="", end="")
        temp_data = str(input())
        if temp_data == "" or temp_data == None:
            temp_data = "<none>"
        temp_data.replace(" ", "_")
        new_line = new_line + temp_data + " "
    with open("save.txt", "a", encoding="UTF-8") as saved_info:
        saved_info.writelines(new_line[:-1])
        saved_info.write("\n")

def lf_everywhere():
    lf_str = input("Введите запрос: ")
    with open("save.txt", "r", encoding="UTF-8") as saved_info:
        for line in saved_info:
            if str(lf_str).lower() in str(line).lower():
                print(line)
def find_menu():
    print("Введите параметры поиска.")
    print("Искать везде (a), поиск по категории: ", end="")
    find_options = data_format()
    for i in range(len(find_options)):
        print(find_options[i], " (", i, ") ", sep="", end=" ")
    while True:
        find_lf_index = input().lower()
        if find_lf_index == "a" or find_lf_index == "а":
            lf_everywhere()
            break
            # Искать везде
        if int(find_lf_index) > -1 and int(find_lf_index) <= len(find_options):
            print("Поиск по параметру:", find_options[int(find_lf_index)], end=".\n")
            lf_with_parameter(int(find_lf_index))
            break
        print("Ошибка ввода параметров поиска.")


def main_menu():
    while True:
        print("Меню. Работа с данными: вывести все (v), добавить (a), найти (f), выйти (q).", end=" ")
        main_menu_ask = input().lower()
        if main_menu_ask == "f" or main_menu_ask == "а":
            find_menu()
        elif main_menu_ask == "q":
            quit()
        elif main_menu_ask == "v":
            show_all()
        else:
            print("Ошибка ввода команды.")


def lf_with_parameter(lf_index):
    lf_string = input("Введите искомое:")
    skip_first = True
    with open("save.txt", "r", encoding="UTF-8") as saved_info:
        for line in saved_info:
            current_line = line.split()
            if skip_first:
                skip_first = False
                continue
            if str(lf_string).lower() in current_line[lf_index].lower():
                print(line)
                while True:
                    ask = input("Продолжить поиск(k), редактировать строку(e) или выйти в меню(q)?").lower()
                    if ask == "k":
                        break
                    elif ask == "e":
                        print("Вызов меню редактирования")
                        quit()
                        # edit_menu(line_num)
                    elif ask == "q":
                        main_menu()
                    print("Ошибка ввода продолжения работы с результатами поиска")
        lf_keep_searching = input("Нет совпадений. Повторить попытку? (y/n) ")
        while True:
            if lf_keep_searching == "y":
                lf_with_parameter(lf_index)
            else:
                main_menu()




main_menu()
