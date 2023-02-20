from to_do import TODO


def task10_1(assessments):
    result = len(assessments)
    return result


if __name__ == "__main__":
    print("Result is", task10_1(assessments="LMHHF"))

def task10_2(assessments):
    result = assessments[3]
    return result


if __name__ == "__main__":
    print("Result is", task10_2(assessments="LMHHF"))


def task10_3(assessments):
    halfway = len(assessments) // 2
    result = assessments[halfway]
    return result


if __name__ == "__main__":
    print("Result is", task10_3(assessments="LMFHM"))


def task10_4(assessments):
    result = assessments[0:3]
    return result


if __name__ == "__main__":
    print("Result is", task10_4(assessments="LMFHM"))
