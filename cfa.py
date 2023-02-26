# cfa - call for action
import edit, find
def found_result_action(line_number):
    while True:
        ask = input("Продолжить поиск(k), редактировать строку(e), удалить строку(d) или выйти в меню(q)? ").lower()
        if ask == "k":
            break
        elif ask == "e":
            print("Вызов меню редактирования")
            edit.edit_menu(line_number)
        elif ask == "q":
            main_menu()
        elif ask == "d":
            edit.delete_line(line_number)
        print("Ошибка ввода")

def main_menu():
    while True:
        print("Меню. Работа с данными: вывести все (v), добавить (a), найти и изменить (f), выйти (q).", end=" ")
        main_menu_ask = input().lower()
        if main_menu_ask == "f":
            find_menu()
        elif main_menu_ask == "q":
            quit()
        elif main_menu_ask == "v":
            find.show_all()
        elif main_menu_ask in ["a", "а"]:
            edit.import_new_data()
        else:
            print("Ошибка ввода команды.")

def find_menu():
    print("Введите параметры поиска.")
    print("Искать везде (a), поиск по категории: ", end="")
    find_options = edit.data_format()
    for i in range(len(find_options)):
        print(find_options[i], " (", i, ") ", sep="", end=" ")
    while True:
        find_lf_index = input().lower()
        if find_lf_index == "a" or find_lf_index == "а":
            find.lf_everywhere()
            break
            # Искать везде
        if int(find_lf_index) > -1 and int(find_lf_index) <= len(find_options):
            print("Поиск по параметру:", find_options[int(find_lf_index)], end=".\n")
            find.lf_with_parameter(int(find_lf_index))
            break
        print("Ошибка ввода параметров поиска.")