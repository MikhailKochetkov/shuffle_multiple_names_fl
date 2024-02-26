import pandas as pd
import random

from settings import SKIP_ROWS


def shuffle_lists(lists: list[list]) -> list:
    copy_lists = [lst.copy() for lst in lists]
    for i in range(len(copy_lists)):
        random.shuffle(copy_lists[i])
    while any(copy_lists[0][i] == copy_lists[1][i] or
              copy_lists[0][i] == copy_lists[2][i] or
              copy_lists[1][i] == copy_lists[2][i]
              for i in range(len(copy_lists[0]))):
        for i in range(len(copy_lists)):
            random.shuffle(copy_lists[i])
    return copy_lists


def repeat_element(lst: list, counts: list) -> list:
    result = []
    for i, element in enumerate(lst):
        result.extend([element] * counts[i])
    return result


def main():
    read_data = pd.read_excel('Book1.xlsx', skiprows=SKIP_ROWS)
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
    with pd.ExcelWriter('Book1.xlsx',
                        engine='openpyxl',
                        mode='a',
                        if_sheet_exists='replace') as writer:
        df.to_excel(writer, sheet_name='Sheet2', index=False)


if __name__ == '__main__':
    main()
