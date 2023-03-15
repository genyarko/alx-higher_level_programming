#!/usr/bin/python3

def uniq_add(my_list=[]):
    result = 0 
    seen = set() 
    for num in my_list: 
        if num not in seen: 
            seen.add(num) 
            result += num 
    return result
