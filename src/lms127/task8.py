from to_do import TODO


def task8(sentence, character):
    result = sentence.count(character)
    return result


if __name__ == "__main__":
    print("result is", task8(sentence="I code in KOTLIN", character="I"))
