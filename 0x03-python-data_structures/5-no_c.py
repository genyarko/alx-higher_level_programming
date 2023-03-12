#!/usr/bin/python3

def no_c(my_string):
    no_c = my_string.translate({ord('c'): None})
    no_c = no_c.translate({ord('C'): None})
    return no_c
