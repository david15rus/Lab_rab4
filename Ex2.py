#!/usr/bin/env python3
# -*- coding: utf-8 -*-
Word = input("Введите словосочетание ")
for i in range(len(Word)):
    if (Word[i] == 'ж' or Word[i] == 'ш') and Word[i+1] != 'и':
        input("Вы написали все верно")
    else: input("Вы написали буквосочетание Жи Ши неверно ")

