#!/usr/bin/env python3
# -*- coding: utf-8 -*-Word = input("Введите текст ")
if __name__ == '__main__':
    s = len(Word)
    mx = 0
    k = 0
    for i in range(s):
        if Word[i] == ' ' and Word[i+1] == ' ':
            k += 1
        else:
            if k > mx:
                mx = k
                k = 0
    print("Количество пробелов подряд", mx)






