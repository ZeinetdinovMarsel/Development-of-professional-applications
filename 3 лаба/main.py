import os
import csv


def inputlist(filename):
    mylist = []
    with open(filename, newline='') as r_file:
        file_reader = csv.DictReader(r_file, delimiter=";")
        for row in file_reader:
            mylist.append(row)
    return mylist


def outputlist(filename, mylist):
    with open(filename, 'w', newline='') as w_file:
        writer = csv.DictWriter(w_file, ["num", "Date", "Cost", "Name"], delimiter=";")
        writer.writeheader()
        writer.writerows(mylist)
    print("Сохранение завершено")


def printlist(mylist):
    for x in mylist:
        print(x)


def printsortlist(mylist, data, reversed=0, integ=0):
    if integ:
        mylist.sort(key=lambda x: int(x[data]), reverse=reversed)
    else:
        mylist.sort(key=lambda x: x[data], reverse=reversed)
    printlist(mylist)
    return mylist


def printiflist(mylist, data, value):
    for x in mylist:
        if int(x[data]) > value:
            print(x)


if __name__ == '__main__':
    print("Количество файлов в директории:", len(os.listdir(path=".")))

    mylist = inputlist("input.csv")

    print("Сортировка по названию(по возрастанию):")
    mylist = printsortlist(mylist, "Name", 0)

    print("Сортировка по стоимости(по возрастанию):")
    mylist = printsortlist(mylist, "Cost", 0, 1)

    print("Вывод по условию(стоимость больше 44):")
    printiflist(mylist, "Cost", 44)

    print("Введите:\n1 - Если хотите сохранить в файл\n0 - Если не хотите сохранять в файл")
    check = int(input())
    if check == 1:
        outputlist("input.csv", mylist)
    else:
        exit()
