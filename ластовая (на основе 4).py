"""Лукьянов Никита практика 4 вариант 15"""


def main():
    while True:
        print("\n___МЕНЮ___")
        print("\nЗадать диапазон - 1")
        print("Выйти - 2")
        n = input()
        while n != '2' and n != '1':
            print("Нужно ввести числа 1 или 2")
            n = input()
        if n == '2':
            break
        if n == '1':
            diap = input("введите диапазон\n")
            if diap == "exit":
                break
            start_stop = new_diap(diap)

            if isinstance(start_stop, tuple):
                for number in range(start_stop[0], start_stop[1]):
                    list_of_numbers = lagr(number)
                    print("Согласно теореме Лагранжа число", number,
                          "состоит из следующих чисел, являющихся квадратами:",
                          list_of_numbers)
            else:
                print("Ошибка ввода данных")


def lagr(n):
    """
    Функция lagr() перебирает абсолютно все возможные значения
    и находит те, которые удовлетворяют теореме Лагранжа
    """
    for a in range(n, -1, -1):
        for b in range(n, -1, -1):
            for c in range(n, -1, -1):
                for d in range(n, -1, -1):
                    if a ** 2 + b ** 2 + c ** 2 + d ** 2 == n:
                        t = [a ** 2, b ** 2, c ** 2, d ** 2]
                        s = [x for x in t if x != 0]
                        return s


def new_diap(diap):
    """
    Функция принимает один аргумент: diap
    :param diap: введёный пользователем отрезок
    :return: Если в диапазоне не числа, возвращается StrError.
    Если числа в нашем отрезке кончились,
    возвращается ArgCountError. Если отрезок существует, возвращается отрезок
    """
    if all(i.isdigit() for i in diap.split(' ')):
        if len(diap.split(' ')) == 1:
            diap = (0, int(diap))
        elif len(diap.split(' ')) == 2:
            diap = tuple(map(int, diap.split(' ')))
        else:
            return "ArgCountError"
        return diap
    else:
        return "StrError"


if __name__ == '__main__':
    main()
