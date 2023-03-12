#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
  # Get the first elements of each tuple
  a1 = tuple_a[0] if len(tuple_a) >= 1 else 0
  b1 = tuple_b[0] if len(tuple_b) >= 1 else 0
  
  # Get the second elements of each tuple
  a2 = tuple_a[1] if len(tuple_a) >= 2 else 0
  b2 = tuple_b[1] if len(tuple_b) >= 2 else 0
  
  # Return the addition of the two tuples
  return (a1 + b1, a2 + b2)
