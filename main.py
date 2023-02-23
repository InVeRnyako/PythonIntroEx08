# Запуск поиска по заданному параметру
def find_with_parameters(lf_str):
    with open("save.txt", "r", encoding="UTF-8") as saved_info:
        for line in saved_info:
            if str(lf_str).lower() in str(line).lower():
                print(line)

# Запрос параметров поиска
def ask_for_parameters():
    print("Введите искомые данные или оставьте пустым для вывода всех данных.")
    lf_str = str(input("Поиск: "))
    return lf_str

# Заполнение данных
def import_new_data():
    print("Введите новые данные в формате: Имя Фамилия Телефон")
    with open("save.txt", "a", encoding="UTF-8") as saved_info:
        saved_info.writelines(input())
        saved_info.write("\n")
    print("Данные внесены.")

import_new_data()
# find_with_parameters(ask_for_parameters())