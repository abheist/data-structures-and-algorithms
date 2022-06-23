
def string_reverser(string_):
    # first way: pythonic version
    return string_[::-1]


def string_reverser_2(string_):
    """
    Second Way:
    convert the string to array with chars, reverse the array and join
    """
    arr = []
    for i in string_:
        arr.insert(0, i)

    return "".join(arr)


def string_reverser_3(string_):
    """
    Third way
    Create a new string, and start appending the last element from the string while looping,
    and loop index will point to the last element.
    """
    new_string = ""
    for i in range(len(string_)):
        # new_string += string_[:-i]
        new_string += string_[(len(string_) - 1) - i]

    return new_string

# test 1st function: string_reverser
print("Pass" if ('retaw' == string_reverser('water')) else "Fail")
print("Pass" if ('!noitalupinam gnirts gnicitcarP' == string_reverser('Practicing string manipulation!')) else "Fail")
print("Pass" if ('3432 :si edoc esuoh ehT' == string_reverser('The house code is: 2343')) else "Fail")


# test 1st function: string_reverser_2
print("Pass" if ('retaw' == string_reverser_2('water')) else "Fail")
print("Pass" if ('!noitalupinam gnirts gnicitcarP' == string_reverser_2('Practicing string manipulation!')) else "Fail")
print("Pass" if ('3432 :si edoc esuoh ehT' == string_reverser_2('The house code is: 2343')) else "Fail")


# test 1st function: string_reverser_3
print("Pass" if ('retaw' == string_reverser_3('water')) else "Fail")
print("Pass" if ('!noitalupinam gnirts gnicitcarP' == string_reverser_3('Practicing string manipulation!')) else "Fail")
print("Pass" if ('3432 :si edoc esuoh ehT' == string_reverser_3('The house code is: 2343')) else "Fail")

