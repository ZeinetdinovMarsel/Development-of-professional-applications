import time
import datetime
import random


class Convertor:
    def __init__(self):
        self.timestamp_seconds = 0
        self.real_second = 0

        self.timestamp_minutes = 0
        self.real_minute = 0

        self.timestamp_hours = 0
        self.real_hour = 0

        self.timestamp_days = 0
        self.real_day = 0

        self.real_month = 0
        self.real_year = 0

    def date_cnt(self):
        self.real_year = 1970
        period = 2
        while True:
            days_in_year = 365
            if period == 4:
                days_in_year = 366
                period = 0
            if self.real_day < days_in_year:
                break
            period += 1
            self.real_day -= days_in_year
            self.real_year += 1
        self.real_month = 0
        days_in_month = 0
        while self.real_day >= days_in_month:
            if self.real_month % 2 == 1 and self.real_month != 2 or self.real_month == 8:
                days_in_month += 31
            elif self.real_month % 2 == 0 and self.real_month != 2 and self.real_month != 8:
                days_in_month += 30
            elif self.real_month == 2:
                days_in_month += 28
            self.real_month += 1
        for i in range(1, self.real_month):
            if i % 2 == 1 and i != 2 or i == 8:
                self.real_day -= 31
            elif i % 2 == 0 and i != 2 and i != 8:
                self.real_day -= 30
            elif i == 2:
                self.real_day -= 28
        return self.fix_format(self.real_year) + "-" + self.fix_format(self.real_month) + "-" + self.fix_format(
            self.real_day)

    def update_timestamp(self, timestamp):
        self.timestamp_seconds = timestamp

    def time_cnt(self):
        self.real_second = round(self.timestamp_seconds % 60)

        self.timestamp_minutes = int(self.timestamp_seconds / 60)
        self.real_minute = int(self.timestamp_minutes % 60)

        self.timestamp_hours = int(self.timestamp_seconds / 3600)
        self.real_hour = int(self.timestamp_hours % 60)

        self.timestamp_days = int(self.timestamp_seconds / 3600 / 24)
        self.real_day = self.timestamp_days

        return self.fix_format(self.real_hour) + ":" + self.fix_format(self.real_minute) + ":" + self.fix_format(
            self.real_second)

    def print_date(self):
        real_time = self.time_cnt()
        real_date = self.date_cnt()
        print(real_date, real_time)

    @staticmethod
    def fix_format(temp_str):
        if len(str(temp_str)) < 2:
            return "0" + str(temp_str)
        return str(temp_str)


def minim(array):
    start_alg = time.time()
    minim_elem = min(array)
    end_alg = time.time()
    time_alg = (end_alg - start_alg) * 10 ** 3
    print("Работа алгоритма заняла:", time_alg, "мс (встроенная)")
    return minim_elem


def minim0(array):
    start_alg = time.time()
    minim_elem = array[0]
    len_arr = len(array)
    for i in range(0, len_arr):
        if array[i] < minim_elem:
            minim_elem = array[i]
    end_alg = time.time()
    time_alg = (end_alg - start_alg) * 10 ** 3
    print("Работа алгоритма заняла:", time_alg, "мс (обход по индексам)")
    return minim_elem


def minim1(array):
    start_alg = time.time()
    minim_elem = array[0]
    for i in array:
        if i < minim_elem:
            minim_elem = i
    end_alg = time.time()
    time_alg = (end_alg - start_alg) * 10 ** 3
    print("Работа алгоритма заняла:", time_alg, "мс (обход по элементам)")
    return minim_elem


def generate_new_arr():
    with open("out.txt", "w+") as out:
        for i in range(0, 10000000):
            out.write(str(random.randint(-100000000, 100000000)) + " ")


if __name__ == '__main__':
    a = Convertor()
    for j in range(1, 10):
        timestamp_seconds = time.time()
        a.update_timestamp(timestamp_seconds)
        a.print_date()
        # time.sleep(1)
    # generate_new_arr()
    with open("out.txt", "r") as out:
        arr = out.read().split()
    for i in range(0, 10000000):
        arr[i] = int(arr[i])

    print(minim(arr), minim0(arr), minim1(arr))

