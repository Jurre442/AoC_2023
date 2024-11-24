# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 13:08:45 2024

@author: jurre
"""

import numpy as np

All_text=open('Day1.txt')
All_text_lines=All_text.readlines()
N=len(All_text_lines)
Sum_all_lines=0
All_numbers=[]
for i in range(0,N):
    k=0
    First_number=[]
    Last_number=[]
    while k<len(All_text_lines[i]):
        if First_number==[]:
            if All_text_lines[i][k].isdigit()==True:
                First_number=int(All_text_lines[i][k])
                Last_number=int(All_text_lines[i][k])
            k=k+1
        else:
            if All_text_lines[i][k].isdigit()==True:
                Last_number=int(All_text_lines[i][k])
            k=k+1
    Number_this_line=10*First_number+Last_number
    All_numbers.append(Number_this_line)
    Sum_all_lines=Sum_all_lines+Number_this_line  
