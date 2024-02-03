#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random

"""
Напишите программу, которая будет генерировать матрицу из
случайных целых чисел. Пользователь может указать число
строк и столбцов, а такжедиапазон целых чисел.
Произведите обработку ошибок ввода пользователя.
"""


class Matrix:
    def __init__(self, crows, ccols, cmin_v, cmax_v):
        self.rows = crows
        self.cols = ccols
        self.min_v = cmin_v
        self.max_v = cmax_v

    def generate(self):
        mtr = [[random.randint(self.min_v, self.max_v)
                for _ in range(self.cols)] for _ in range(self.rows)]
        return mtr


if __name__ == "__main__":
    while True:
        try:
            rows = int(input("Количество строк: "))
            cols = int(input("Количество столбцов: "))
            min_v = int(input("Минимальное значение: "))
            max_v = int(input("Максимальное значение: "))
            if rows <= 0 or cols <= 0 or min_v > max_v:
                raise ValueError("Неверный диапазон")
        except ValueError:
            print("Ошибка. Введите целые числа.")
            continue

        matrix = Matrix(rows, cols, min_v, max_v)
        matrix_gen = matrix.generate()
        print("Полученная матрица:")
        for row in matrix_gen:
            print(row)
        break
