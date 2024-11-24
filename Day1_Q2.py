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
            elif All_text_lines[i][k:k+3]=='one':
                First_number=1
                Last_number=1
            elif All_text_lines[i][k:k+3]=='two':
                First_number=2
                Last_number=2
            elif All_text_lines[i][k:k+5]=='three':
                First_number=3
                Last_number=3
            elif All_text_lines[i][k:k+4]=='four':
                First_number=4
                Last_number=4
            elif All_text_lines[i][k:k+4]=='five':
                First_number=5
                Last_number=5
            elif All_text_lines[i][k:k+3]=='six':
                First_number=6
                Last_number=6
            elif All_text_lines[i][k:k+5]=='seven':
                First_number=7
                Last_number=7
            elif All_text_lines[i][k:k+5]=='eight':
                First_number=8
                Last_number=8
            elif All_text_lines[i][k:k+4]=='nine':
                First_number=9
                Last_number=9
            k=k+1
        else:
            if All_text_lines[i][k].isdigit()==True:
                Last_number=int(All_text_lines[i][k])
            elif All_text_lines[i][k:k+3]=='one':
                Last_number=1
            elif All_text_lines[i][k:k+3]=='two':
                Last_number=2
            elif All_text_lines[i][k:k+5]=='three':
                Last_number=3
            elif All_text_lines[i][k:k+4]=='four':
                Last_number=4
            elif All_text_lines[i][k:k+4]=='five':
                Last_number=5
            elif All_text_lines[i][k:k+3]=='six':
                Last_number=6
            elif All_text_lines[i][k:k+5]=='seven':
                Last_number=7
            elif All_text_lines[i][k:k+5]=='eight':
                Last_number=8
            elif All_text_lines[i][k:k+4]=='nine':
                Last_number=9
            k=k+1
    Number_this_line=10*First_number+Last_number
    All_numbers.append(Number_this_line)
    Sum_all_lines=Sum_all_lines+Number_this_line
    

            
        
    
