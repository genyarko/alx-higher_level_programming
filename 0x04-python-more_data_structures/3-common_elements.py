#!/usr/bin/python3
def common_elements(set_1, set_2):
    # Initialize an empty set
    common = set()
    
    # Loop through the first set 
    for element in set_1:
        # If element is in the second set, add it to the common set
        if element in set_2:
            common.add(element)
    
    # Return the set of common elements
    return common
