[![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)](https://www.python.org/)


# Описание
Распределение имен, заданных в трех колонках, в слечайном порядке

Условия:
* В каждой колонке каждое имя должно присутствовать заданное для данной колонки количество раз
* В одной строке одно имя может быть только в одной ячейке. Дублироваться имена в строке не должны
* В каждой колонке имена должны быть в случайном порядке

## Пример входных данных

| Список имен      | 1      | 2      | 3      |
|------------------|--------|--------|--------|
| Иван             | 2      | 1      | 1      |
| Петр             | 3      | 2      | 3      |
| Семен            | 4      | 1      | 2      |
| Мария            | 1      | 4      | 3      |
| Ольга            | 1      | 3      | 2      |

## Пример выходных данных

| 1     | 2      | 3      |
|-------|--------|--------|
| Иван  | Петр   | Ольга  |
| Семен | Петр   | Ольга  |
| Петр  | Ольга  | Мария  |
| Иван  | Мария  | Семен  |
| Семен | Мария  | Петр   |
| Семен | Иван   | Петр   |
| Петр  | Мария  | Иван   |
| Мария | Семен  | Петр   |
| Семен | Ольга  | Мария  |
| Петр  | Ольга  | Мария  |
| Ольга | Мария  | Семен  |

# Автор

**Михаил Кочетков** - https://github.com/MikhailKochetkov
