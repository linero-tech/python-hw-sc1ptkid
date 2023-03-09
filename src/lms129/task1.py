from to_do import TODO


def task1(a, b):
    result = 0
    if a < b:
        for i in range(a, b + 1):
            result += i
            # result = result + i

    return result


if __name__ == "__main__":
    print(task1(a=1, b=5))  # 15
    print(task1(a=3, b=3))  # 0
    print(task1(a=5, b=9))  # 35
    print(task1(a=9, b=15))  # 84
