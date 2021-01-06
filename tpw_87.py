def center_string(string: str,length: int) -> str:
    left_spaces = (length - len(string)) // 2
    result = " " * left_spaces + string
    return result
    
def main():

    string = input("What word do you want to center?: ")

    while True:
        try:
            length = int(input("How big is your terminal?: "))
            break
        except ValueError:
            print("Invalid input please try again")

    centered_string = center_string(string,length)
    print(centered_string)

def tests():
    assert center_string("a", 3) == " a"
    assert center_string("aa", 4) == " aa"
    assert center_string("b", 5) == "  b"
    assert center_string("hello", 11) == "   hello"
    print("all passed!")


tests()
