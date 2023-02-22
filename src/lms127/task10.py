from to_do import TODO


def task10_1(assessments):
    result = len(assessments)
    return result


def task10_2(assessments):
    result = assessments[3]
    return result


def task10_3(assessments):
    result = assessments[len(assessments) // 2]
    return result


def task10_4(assessments):
    result = assessments[0:3]
    return result


if __name__ == "__main__":
    print("result is", task10_1(assessments="LMHHF"), "min")
    print("result is", task10_2(assessments="LMFHMF"), "(High)")
    print("result is", task10_3(assessments="LMFHM"), "(Failure)")
    print("result is", task10_4(assessments="LMFHM"), "(Low, Medium, Failure)")
