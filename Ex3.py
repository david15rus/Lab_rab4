#!/usr/bin/env python3
# -*- coding: utf-8 -*-Word = input("Введите текст ")
Word = input("Введите предложение:")
s = len(Word)
for i in range(s):
    if Word[i] == 'C' or Word[i] == 'c' or Word[i] == 'С' or Word[i] == 'с':
        Word = Word.replace(Word[i], ' ')
print(Word)







