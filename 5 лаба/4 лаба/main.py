class TemplateRow:
    def __init__(self, num):
        self.num = num

    def get_num(self):
        return self.num

    def set_num(self, val):
        self.num = val


class Row(TemplateRow):
    def __init__(self, temp_arr):
        super().__init__(int(temp_arr[0]))
        (self.date, self.cost, self.name) = temp_arr[1], int(temp_arr[2]), temp_arr[3]

    def __str__(self):
        return str(self.num) + ' ' + self.date + ' ' + str(self.cost) + ' ' + self.name

    def __repr__(self):
        return 'NUM: ' + str(self.num) + ' DATE: ' + self.date + ' COST: ' + str(self.cost) + ' NAME: ' + self.name

    def __setattr__(self, __name, __value):
        self.__dict__[__name] = __value

    def __getitem__(self, __name):
        return self.__dict__[__name]


class MyTable:
    def __init__(self, file_path=None):
        self.index = 0
        if file_path is not None:
            self.table = self.parse(file_path)
        else:
            self.table = []

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.table):
            self.index = 0
            raise StopIteration
        else:
            iter_row = self.table[self.index]
            self.index += 1
            return iter_row

    def __getitem__(self, id_row):
        return self.table[id_row]

    def add_row(self, row):
        if len(self.table) == 0:
            self.table.append(Row([0] + row))
        else:
            self.table.append(Row([len(self.table) + 1] + row))

    def delete_row(self, row_num):
        self.table.remove(self.table[row_num])

    def sort_table(self, name, is_reversed):
        temp_list = MyTable()
        temp_list.table = sorted(self.table, key=lambda f: f[name], reverse=is_reversed)
        return temp_list

    def if_list(self, data, op, value):
        temp_list = MyTable()
        for elem in self.table:
            if op == '>':
                if int(elem[data]) > value:
                    temp_list.table.append(elem)
            elif op == '<':
                if int(elem[data]) < value:
                    temp_list.table.append(elem)
            elif op == '==':
                if int(elem[data]) == value:
                    temp_list.table.append(elem)
            elif op == '!=':
                if int(elem[data]) != value:
                    temp_list.table.append(elem)
            elif op == '>=':
                if int(elem[data]) >= value:
                    temp_list.table.append(elem)
            elif op == '<=':
                if int(elem[data]) <= value:
                    temp_list.table.append(elem)
        return temp_list

    def generator(self):
        self.index = 0
        while self.index < len(self.table):
            yield table[self.index]
            self.index += 1
        else:
            self.index = 0

    @staticmethod
    def parse(file_path):
        temp_table = []
        with open(file_path, 'r') as file:
            for line in file:
                temp_row = Row(line.replace('\n', '').split(';'))
                temp_table.append(temp_row)
        return temp_table

    @staticmethod
    def save(file_path):
        with open(file_path, 'w') as file:
            for row in table:
                file.write(';'.join([str(row.num), row.date, str(row.cost), row.name]))
                file.write('\n')


if __name__ == '__main__':
    table = MyTable('input.csv')

    print("Вывод по элементам:")
    for x in table:
        print(x)

    print("Вывод по генератору:")
    for x in table.generator():
        print(x)

    print("Вывод по индексу:")
    print(table[2])

    print("Изменение значения свойства:")
    table.table[2].cost=3
    print(table[2])

    print("Сортировка по названию(по возрастанию):")
    table = table.sort_table('name', 0)
    for x in table:
        print(x)

    print("Сортировка по стоимости(по возрастанию):")
    table = table.sort_table('cost', 0)
    for x in table:
        print(x)

    print("По условию(стоимость больше 44):")
    table = table.if_list('cost', '>', 44)
    for x in table:
        print(x)

    table.sort_table('num', 0)
    print("Введите:\n1 - Если хотите сохранить в файл\n0 - Если не хотите сохранять в файл")
    check = int(input())
    if check == 1:
        print("Введите путь к файлу")
        table.save(input())
    else:
        exit()
