# -*- coding: utf-8 -*-

import random
import os

# Заменить .txt на БД

def opening_dictionary():
    """ Открывает файл-словарь Dictionary.txt и передает из него случайно
    перемешанные данные в переменную dictionary.

    dictionary = [[str, str], ..., [str, str]]
        dictionary[*][0] - английское слово
        dictionary[*][1] - его перевод
    """

    dictionary = []

    with open('Dictionary.txt', 'r') as file:
        while True:
            line = file.readline()
            if line == '':
                break
            dictionary.append(line.rstrip().split(' - '))

    # Перемешивает словарь
    random.shuffle(dictionary)

    return dictionary


def run(dictionary):
    """ Последовательно проходит по перемешанному словарю указанное количество
    слов, прося ввести правильный вариант перевода."""

    number = int(input('Введите количество слов для повторения:\n'))

    for ind, value in enumerate(dictionary[: number]):
        os.system('cls')
        print(value[1], '\t', ind + 1, '/', number, '/', len(dictionary))
        answer = input('Введите перевод\n')

        if answer == value[0]:
            print('Верно!\n')
            input('Нажмите Enter, чтобы продолжить.')

        else:
            while answer != value[0]:
                if answer == '':
                    print('Правильный ответ -', value[0], '\n')
                    answer = input('Введите правильный отвер:\n')

                elif answer != value[0]:
                    print('Не Верно! Правильный ответ -\n')
                    print(value[0], '\n')
                    answer = input('Введите правильный ответ:\n')


def main():
    dictionary = opening_dictionary()
    run(dictionary)



if __name__ == '__main__':
    main()
