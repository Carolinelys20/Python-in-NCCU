# coding: utf-8
get_ipython().run_line_magic('matplotlib', 'inline')

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from numpy.random import choice
from numpy.random import randint
words='''
我
我的
妳
妳的
心
溫柔
日子
雨
風
天空
雲
等待
哭泣
戀愛
相遇
分離
忘記
心醉
驀然
吹過
思念
靈魂
停止'''
for i in range(randint(2,6)): #段數
    k = randint(5,8) #字數
    egg = choice(phrase,k) #美劇選k個字
    poem = ' '.join(egg) #合併清單
    print(poem)
