from to_do import TODO


def task8(number):
    result = 0
    for digit in str(number):
        result += int(digit)

    return result


if __name__ == "__main__":
    print(task8(number=123))  # 6
    print(task8(number=1))  # 1
    print(task8(number=9999))  # 36
