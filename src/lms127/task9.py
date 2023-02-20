from to_do import TODO


def task9(sentence, character):
    result = character in sentence.lower()
    return result


if __name__ == "__main__":
    print("result is", task9(sentence="I code In KOTLIN", character="i"))
