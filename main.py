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
        for line in enumerate(saved_info):
            if line[0] == 0:
                continue
            if str(lf_str).lower() in str(line[1]).lower():
                print(line[1])
                found_result_action(line[0])
    print("Нет совпадений")


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
        print("Меню. Работа с данными: вывести все (v), добавить (a), найти и изменить (f), выйти (q).", end=" ")
        main_menu_ask = input().lower()
        if main_menu_ask == "f":
            find_menu()
        elif main_menu_ask == "q":
            quit()
        elif main_menu_ask == "v":
            show_all()
        else:
            print("Ошибка ввода команды.")


def edit_menu(edit_line_num):
    print("Выберите параметры редактирования: (a) - всё,", end=" ")
    edit_options = data_format()
    for i in range(len(edit_options)):
        print(edit_options[i], " (", i, ") ", sep="", end=" ")
    edit_what = input().lower()
    with open("save.txt", "r", encoding="UTF-8") as saved_info:
        data_save = saved_info.readlines()
    changed_line = ["" for i in range(len(edit_options))]
    for i in range(len(edit_options)):
        if edit_what in ["а", "a"] or int(edit_what) == i:
            print("Введите новое значение ", edit_options[i], ":", sep="")
            changed_line[i] = input().replace(" ", "_")
            if changed_line[i] == "" or changed_line[i] == None:
                changed_line[i] = "<None>"
    data_save[edit_line_num] = " ".join(changed_line) + "\n"
    with open("save.txt", "w", encoding="UTF-8") as saved_info:
        saved_info.writelines(data_save)
    main_menu()


def lf_with_parameter(lf_index):
    lf_string = input("Введите искомое:")
    with open("save.txt", "r", encoding="UTF-8") as saved_info:
        for line in enumerate(saved_info):
            current_line = line[1].split()
            if line[0] == 0:
                continue
            if str(lf_string).lower() in current_line[lf_index].lower():
                print(line[1])
                found_result_action(line[1])
        lf_keep_searching = input("Нет совпадений. Повторить попытку? (y/n) ")
        while True:
            if lf_keep_searching == "y":
                lf_with_parameter(lf_index)
            else:
                main_menu()


def found_result_action(line_number):
    while True:
        ask = input("Продолжить поиск(k), редактировать строку(e), удалить строку(d) или выйти в меню(q)?").lower()
        if ask == "k":
            break
        elif ask == "e":
            print("Вызов меню редактирования")
            edit_menu(line_number)
        elif ask == "q":
            main_menu()
        elif ask == "d":
            delete_line(line_number)
        print("Ошибка ввода продолжения работы с результатами поиска")


def delete_line(id_to_remove):
    with open("save.txt", "r", encoding="UTF-8") as saved_info:
        data_save = saved_info.readlines()
    del data_save[id_to_remove]
    with open("save.txt", "w", encoding="UTF-8") as saved_info:
        saved_info.writelines(data_save)
    print("Данные удалены.")
    main_menu()


main_menu()
