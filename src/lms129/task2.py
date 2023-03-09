from to_do import TODO


def task2(number):
    result = False
    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                return result
        else:
            result = True
    return result


if __name__ == "__main__":
    print(task2(number=5))
    print(task2(number=0))
    print(task2(number=29))
    print(task2(number=99))
