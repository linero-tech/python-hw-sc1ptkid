from to_do import TODO


def task4(base, height):
    result = 0.5 * base * height
    return result


if __name__ == "__main__":
   print(task4(base=5.0, height=10.0))
   print(task4(base=0.0, height=10.0))
   print(task4(base=50.0, height=0.0))
