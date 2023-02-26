import cfa
def show_all():
    with open("save.txt", "r", encoding="UTF-8") as saved_info:
        for line in saved_info:
            print(line)
    cfa.main_menu()

def lf_everywhere():
    lf_str = input("Введите запрос: ")
    with open("save.txt", "r", encoding="UTF-8") as saved_info:
        for line in enumerate(saved_info):
            if line[0] == 0:
                continue
            if str(lf_str).lower() in str(line[1]).lower():
                print(line[1])
                cfa.found_result_action(line[0])
    print("Нет совпадений")

def lf_with_parameter(lf_index):
    lf_string = input("Введите искомое:")
    with open("save.txt", "r", encoding="UTF-8") as saved_info:
        for line in enumerate(saved_info):
            current_line = line[1].split()
            if line[0] == 0:
                continue
            if str(lf_string).lower() in current_line[lf_index].lower():
                print(line[1])
                cfa.found_result_action(line[0])
        lf_keep_searching = input("Нет совпадений. Повторить попытку? (y/n) ")
        while True:
            if lf_keep_searching == "y":
                lf_with_parameter(lf_index)
            elif lf_keep_searching == "n":
                cfa.main_menu()
            print("Ошибка ввода.")