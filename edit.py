import cfa
def data_format():
    with open("save.txt", "r", encoding="UTF-8") as saved_info:
        return saved_info.readlines()[0].split()
def import_new_data():
    print("Ввод новых данных.")
    new_line = ""
    for i in data_format():
        print("Введите ", i, ": ", sep="", end="")
        temp_data = str(input()).title().replace(" ", "_")
        if temp_data == "" or temp_data == None:
            temp_data = "<none>"
        new_line = new_line + temp_data + " "
    with open("save.txt", "a", encoding="UTF-8") as saved_info:
        saved_info.writelines(new_line[:-1])
        saved_info.write("\n")

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
            changed_line[i] = input().replace(" ", "_").title()
            if changed_line[i] == "" or changed_line[i] == None:
                changed_line[i] = "<None>"
    data_save[edit_line_num] = " ".join(changed_line) + "\n"
    with open("save.txt", "w", encoding="UTF-8") as saved_info:
        saved_info.writelines(data_save)
    cfa.main_menu()

def delete_line(id_to_remove):
    with open("save.txt", "r", encoding="UTF-8") as saved_info:
        data_save = saved_info.readlines()
    del data_save[id_to_remove]
    with open("save.txt", "w", encoding="UTF-8") as saved_info:
        saved_info.writelines(data_save)
    print("Данные удалены.")
    cfa.main_menu()