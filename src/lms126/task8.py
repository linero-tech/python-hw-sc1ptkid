from to_do import TODO


def task8():
    return """
    START
    INPUT X
        IF X = %3
        OUTPUT print ("Foo")
        IF X = %5
        OUTPUT print ("Bar")
        IF X = [%3] and [%5]
        OUTPUT print ("FooBar")
        ELSE X = [%3=0] or [%5=0]
        OUTPUT print ("Qix")
    ENDIF  
    """
