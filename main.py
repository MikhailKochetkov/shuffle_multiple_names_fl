import pandas as pd
import random


def repeat_element(lst: list, counts: list) -> list:
    result = []
    for i, element in enumerate(lst):
        result.extend([element] * counts[i])
    return result


def main():
    read_data = pd.read_excel('Book1.xlsx', skiprows=2)
    names_list = read_data.iloc[:, 0].tolist()
    counts_list = read_data.columns.tolist()[1:]
    df_dict = {}
    for element in counts_list:
        column_data = read_data[element].tolist()
        res = repeat_element(names_list, column_data)
        random.shuffle(res)
        df_dict[element] = res
    df = pd.DataFrame(df_dict)
    with pd.ExcelWriter('Book1.xlsx', engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
        df.to_excel(writer, sheet_name='Sheet2', index=False)


if __name__ == '__main__':
    main()
