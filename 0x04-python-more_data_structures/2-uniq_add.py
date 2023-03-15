#!/usr/bin/python3

def uniq_add(my_list=[]): 
    result = 0
    for i in my_list: 
        if i not in my_list[:my_list.index(i)]:  
            result += i
    return result
