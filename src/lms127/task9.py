from to_do import TODO


def task9(sentence, character):
    return character.lower() in sentence.lower()

if __name__ == "__main__":
    print("result is", task9(sentence="I code In KOTLIN", character="i"))
