def safe_print_list(my_list=[], x=0):
    elements_printed = 0
    try:
        for element in range(x):
            print(my_list[element], end="")
            elements_printed += 1
        print()
    except:
        print()
    return elements_printed
