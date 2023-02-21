from random import randint

list1 = []  # список для сохранения последовательности чётных чисел
list2 = []  # список для сохранения последовательности после обработки


def mylen(templist):  # собственная функция длины списка
    count = 0
    for _ in templist:
        count += 1
    return count


def mysplit(array):  # собственная функция для разделения строки на элементы списка по пробелам
    templist = []
    sizearray = mylen(array)
    tempstr = ""
    i = 0
    while i < sizearray:
        while array[i] != ' ' and array[i] != '\0':
            tempstr += array[i]
            i += 1
            if i == sizearray:
                break
        templist.append(int(tempstr))
        tempstr = ""
        i += 1
    return templist


def myinput():  # собственная функция ввода числовых значений
    try:
        val = int(input())
    except ValueError:
        print("Некорректный ввод")
        exit()
    return val


def myhandinput():  # собсвтенная функция ввода элементов массива
    print("Введите элементы массива через пробел")
    try:
        arr = str(input())
        templist = mysplit(arr)
    except ValueError:
        print("Некорректный ввод")
        exit()
    return templist


def mymin(templist):  # собственная функция минимума
    minim = templist[0]
    for j in range(mylen(list1)):
        if list1[j] < minim:
            minim = list1[j]
    return minim


def myalgorythm():  # собственная функция алгоритма
    if mylen(list1) != 0:
        minim = mymin(list1)
        list1.remove(minim)
        for j in range(mylen(list1)):
            list2.append(list1[j])
        list1.clear()
    return 0


def mymain():  # функция выполнения программы с собственными функциями
    mainlist = []

    print("Введите:\n1-чтобы ввести данные самому\n0-чтобы ввести случайные данные")
    variant = myinput()

    print("Введите размер массива")
    a = myinput()

    if variant == 1:
        mainlist = myhandinput()
    elif variant == 0:
        for i in range(a):
            mainlist.append(randint(0, 9))
    else:
        print("Некорректный ввод")
        exit()

    print("A[" + str(a) + "] =", mainlist)

    for i in range(a + 1):
        if i == a or mainlist[i] % 2 == 1:
            myalgorythm()
            if i < a:
                list2.append(mainlist[i])
        else:
            list1.append(mainlist[i])

    print("A[" + str(mylen(list2)) + "] =", list2)


def algorythm():  # функция алгоритма со встроенными функциями языка
    if len(list1) != 0:
        minim = min(list1)
        list1.remove(minim)
        for j in range(len(list1)):
            list2.append(list1[j])
        list1.clear()
    return 0


def handinput():  # функция ввода элементов массива со встроенными функциями языка
    print("Введите элементы массива через пробел")
    try:
        arr = str(input())
        templist = list(map(int, arr.split(' ')))
    except ValueError:
        print("Некорректный ввод")
        exit()
    return templist


def defaultmymain():  # функция выполнения программы со встроенными функциями
    mainlist = []

    print("Введите:\n1-чтобы ввести данные самому\n0-чтобы ввести случайные данные")
    variant = myinput()

    print("Введите размер массива")
    a = myinput()

    if variant == 1:
        mainlist = handinput()
    elif variant == 0:
        for i in range(a):
            mainlist.append(randint(0, 9))
    else:
        print("Некорректный ввод")
        exit()

    print("A[" + str(a) + "] =", mainlist)

    for i in range(a + 1):
        if i == a or mainlist[i] % 2 == 1:
            algorythm()
            if i < a:
                list2.append(mainlist[i])
        else:
            list1.append(mainlist[i])

    print("A[" + str(len(list2)) + "] =", list2)


if __name__ == '__main__':
    print(
        "Введите:\n1-для выполнения программы со встроенными функциями\n0-для выполнения программы с созданными "
        "функциями")
    choose = myinput()
    if choose == 1:  # проверка ввода выбора функции выполнения программы
        defaultmymain()
    else:
        mymain()
