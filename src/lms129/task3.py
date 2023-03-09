from to_do import TODO


def task3(number):
    result = 1
    for i in range(number, 0, -1):
        result = result * i

    return result


if __name__ == "__main__":
    print(task3(number=5))  # 120
    print(task3(number=3))  # 6
    print(task3(number=0))  # 1
    print(task3(number=4))  # 24
