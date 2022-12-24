import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(input_f, delimiter=",", new_line="\n") -> list[dict]:  # Заводим пустой словарь, необходимые списки и переменные
    dict_ = {}
    col_val = []
    list_val = []
    list_keys = []
    list_line = []
    list_final = []
    with open(input_f) as f:
        for line in f:
            list_line.append(line.rsplit())  # Добавляем в список строк разделенные строки из исходного файла
    for line_l in list_line:
        if line_l == list_line[0]:  # Проверяем наличие строки в списке строк
            list_keys = line_l[0].split(delimiter)  # При наличии строки отделяем ее запятой и формируем список ключей
        else:
            col_val.append(line_l)  # В случае отсутствия добавляем строки (значения) в отдельный список
    for value in col_val:
        list_val.append(value[0].split(delimiter))  # Добавляем разделенные значения в список значений
    for l in range(len(list_line) - 1):
        list_line_l = list_val[l]  # Формируем список порядковых номеров строк
        for key in range(len(list_keys)):
            dict_[list_keys[key]] = list_line_l[key]  # Формируем словарь для каждого порядкового номера строки
        list_final.append(dict_.copy())  # Добавляем словари в окончательный список
    return list_final


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
#