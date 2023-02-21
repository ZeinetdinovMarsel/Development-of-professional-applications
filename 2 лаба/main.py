import numpy as np

def myinput():  # функция ввода числовых значений
    try:
        val = int(input())
    except ValueError:
        print("Некорректный ввод")
        exit()
    return val


def algorythm(calcarr):  # функция алгоритма
    calcarr = np.append(calcarr, np.array([np.mean(calcarr, axis=0)]), 0)
    calcarr = np.append(calcarr, np.split(np.array(np.mean(calcarr, axis=1)), len(calcarr)), 1)
    return calcarr


def handinput(a, b):  # функция ввода элементов массива
    tempcomarr = np.empty(shape=(a, b), dtype='int64')
    for i in range(a):
        try:
            print("Введите элементы " + str(i) + "-ой строки массива через пробел")
            temparr = str(input())
            tempcomarr[i] = np.array(list(map(int, temparr.split(' '))))
        except ValueError:
            print("Некорректный ввод")
            exit()
    return tempcomarr

def main():  # функция выполнения программы

    print("Введите:\n1-чтобы ввести данные самому\n0-чтобы ввести случайные данные")
    variant = myinput()

    print("Введите количество строк массива")
    a = myinput()
    print("Введите количество столбцов массива")
    b = myinput()

    if variant == 1:
        arr = handinput(a, b)
    elif variant == 0:
        arr = np.random.randint(0, 10, size=(a, b))  # заполнение массива случайными значениями от 0 до 10
    else:
        print("Некорректный ввод")
        exit()

    print("Исходный массив A[" + str(a) + "][" + str(b) + "]=\n" + str(arr))
    calcarr = np.copy(arr)
    calcarr = algorythm(calcarr)
    print("Обработанный массив B[" + str(a + 1) + "][" + str(b + 1) + "]=\n" + str(calcarr))
    f = open("output.txt", "w+")  # открывание(при отсутствии создание) файла для записи
    try:
        f.write("Исходный массив A[" + str(a) + "][" + str(b) + "]=\n" + str(arr) + '\n')  # запись результатов
        f.write("Обработанный массив B[" + str(a + 1) + "][" + str(b + 1) + "]=\n" + str(calcarr) + '\n')
    finally:  # нужен для срабатывания f.close() при любом типе исключений
        f.close()

if __name__ == '__main__':
    main()
