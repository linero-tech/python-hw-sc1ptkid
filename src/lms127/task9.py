from to_do import TODO


def task9(sentence, character):
    result = sentence.lower().count(character)
    return bool(result)


if __name__ == "__main__":
    print(task9(sentence="I code In KOTLIN", character="i"))
