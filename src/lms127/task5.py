from to_do import TODO


def task5(value_for_a, value_for_b):
    a = value_for_a
    b = value_for_b
    b, a = a, b #swaping value_for_a for value_for_b

    # Do not erase or change the below statement
    return a, b


if __name__ == "__main__":
    print (task5(1, 2))
