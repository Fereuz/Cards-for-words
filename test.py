# -*- coding: utf-8 -*-

import os
import random
import sqlite3

#Таблица - dictionary; столбцы - word, translation


def add_data(cursor):
    """ """

    w = input('Введите английское слово для занесения его в базу:\n')
    t = input('Введите его перевод:\n')
    
    cursor.execute("INSERT INTO word VALUES {}".format(w))
    cursor.execute("INSERT INTO translation VALUES {}".format(t))
    cursor.commit()


def del_data(cursor):
    pass


def read_data(cursor):
    """ """
    return cursor.execute("SELECT * FROM dictionary")


def run(dictionary):
    """ """

    number = int(input('Введите количество слов для повторения:\n'))

    for i in range(number):
        print(dictionary[i])


def main():
    conn = sqlite3.connect('Dictionary.sqlite')
    # Курсор через который осуществляется обращение к БД
    cursor = conn.cursor()
    dictionary = read_data(cursor)
    conn.close()

    #random.shuffle(dictionary)

    while True:
        answer = input('Возможные действия:\n'
                       '1: Начать повторение слов.\n'
                       '2: Пополнить словарь.\n')
        if answer == '1':
            run(dictionary)
        elif answer == '2':
            add_data(cursor)
        else:
            print('Недопустимая команда. Попробуйте еще раз.')

#
#
#
if __name__ == '__main__':
    main()

"""
CREATE TABLE months (id int, name varchar(10), days int);

INSERT INTO months VALUES (1, 'January', 31);
INSERT INTO months (id, name, days) VALUES (2, 'Febreary', 29);

SELECT * FROM characters
SELECT name, weapon FROM characters
SELECT name, weapon FROM "characters" ORDER BY name DESC

SELECT *
FROM characters
WHERE weapon = 'pistol';

SELECT *
FROM albums
WHERE genre = 'rock' AND sales_in_millions <= 50
ORDER BY released;

IN — сравнивает значение в столбце с несколькими возможными значениями и возвращает true, если значение совпадает хотя бы с одним из значением
BETWEEN — проверяет, находится ли значение в каком-то промежутке
LIKE — ищет по шаблону
SELECT * FROM albums WHERE genre IN ('pop','soul');
SELECT * FROM albums WHERE released BETWEEN 1975 AND 1985;
SELECT * FROM albums WHERE album LIKE '%R%';

"""
