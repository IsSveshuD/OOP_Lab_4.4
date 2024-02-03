#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Напишите программу, которая запрашивает ввод двух значений.
Если хотя бы одно из них не является числом, то должна
выполняться конкатенация, т. е. соединение, строк.
В остальных случаях введенные числа суммируются.
"""


def main():
    a1 = input("Первое значение: ")
    a2 = input("Второе значение: ")
    try:
        num1 = float(a1)
        num2 = float(a2)

        result = num1 + num2
        print("Результат:", result)

    except ValueError:
        result = a1 + a2
        print("Результат:", result)


if __name__ == "__main__":
    main()