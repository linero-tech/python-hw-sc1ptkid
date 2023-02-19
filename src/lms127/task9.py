from to_do import TODO


def task9(sentence, character):
    result = character.lower() in sentence.lower()
    return result


if __name__ == "__main__":
    print("Result is", task9(sentence="I code In KOTLIN", character="i"))
