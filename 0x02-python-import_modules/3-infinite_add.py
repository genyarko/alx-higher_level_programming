#!/usr/bin/python3
import sys

# get list of arguments
args = sys.argv[1:]

# convert each argument to int
args = [int(x) for x in args]

# add all arguments
result = sum(args)

# print result
print(result)
