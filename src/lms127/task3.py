from to_do import TODO


def task3(radius):
    result = 2.0 * 3.1416 * radius
    return result


if __name__ == "__main__":
    print(task3(radius=2.0))    # 12.57
    print(task3(radius=0.0))    # 0.0
    print(task3(1.0))           # 6.28