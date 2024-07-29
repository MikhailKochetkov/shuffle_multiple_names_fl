import os
import pandas as pd
import random

from settings import SKIP_ROWS, SHEET_NAME


def shuffle_lists(lists: list[list]) -> list:
    copy_lists = [lst.copy() for lst in lists]
    for i in range(len(copy_lists)):
        random.shuffle(copy_lists[i])
    while any(copy_lists[j][i] == copy_lists[k][i]
              for i in range(len(copy_lists[0]))
              for j in range(len(copy_lists))
              for k in range(j+1, len(copy_lists))):
        for i in range(len(copy_lists)):
            random.shuffle(copy_lists[i])
    return copy_lists


def repeat_element(lst: list, counts: list) -> list:
    result = []
    for i, element in enumerate(lst):
        result.extend([element] * counts[i])
    return result


def get_book_name():
    for filename in os.listdir(os.getcwd()):
        if filename.endswith('.xlsx') or filename.endswith('.xls'):
            return filename


def get_sheet_name():
    file = pd.ExcelFile(get_book_name())
    sheet_name = file.sheet_names
    return sheet_name[0]


def main():
    read_data = pd.read_excel(get_book_name(), skiprows=SKIP_ROWS, sheet_name=get_sheet_name())
    names_list = read_data.iloc[:, 0].tolist()
    counts_list = read_data.columns.tolist()[1:]
    df_dict = {}
    column_lists = []
    for element in counts_list:
        column_data = read_data[element].tolist()
        res = repeat_element(names_list, column_data)
        column_lists.append(res)
    shuffled_lists = shuffle_lists(column_lists)
    for i in range(len(shuffled_lists)):
        df_dict[i+1] = shuffled_lists[i]
    df = pd.DataFrame(df_dict)
    with pd.ExcelWriter(get_book_name(),
                        engine='openpyxl',
                        mode='a',
                        if_sheet_exists='replace') as writer:
        df.to_excel(writer, sheet_name=SHEET_NAME, index=False)


if __name__ == '__main__':
    main()
