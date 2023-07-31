# Напишите функцию, которая принимает
# на вход строку — абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов:
# путь, имя файла, расширение файла.


def gen_paht(file_path: str):
    a, b, c = '\\'.join(file_path.split('\\')[:-1]), \
        file_path.split('\\')[-1].split('.')[0], \
        file_path.split('\\')[-1].split('.')[1]
    return a, b, c

print(gen_paht(input("Введите путь: ")))