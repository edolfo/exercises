#!/usr/bin/env python3

# Design an algorithm and write code to remove the duplicate characters in a string without using any additional
# buffer. NOTE: One or two additional variables are fine. An extra copy of the array is not.
# FOLLOW UP
# Write the test cases for this method.

def removeDuplicates(item: str):
    """
        Since python strings are immutable, we can't really do this without any additional buffer.  That is, on
        every 'mutation' of the input string, python is making a new string.  We try to get around
        this design by converting to a list, and removing items from the list as we go.
    """
    item = list(item)
    finished = False
    while not finished:
        for i in range(len(item)):
            for j in range(len(item)):
                if i != j and item[i] == item[j]:
                    item.pop(j)
                    break
                if i == j and i == len(item) - 1:
                    finished = True
            else:
                continue
            break

    return ''.join(item)

def main():
    testStrings = {
        "The quick brown fox jumps over the lazy dog.": "The quickbrownfxjmpsvtlazydg.",
        "hello": "helo",
        " ": " ",
        "     ": " ",
        "abcabcabc": "abc"
    }
    errorsFound = False
    for item in testStrings.keys():
        try:
            assert(testStrings[item] == removeDuplicates(item))
        except AssertionError:
            errorsFound = True
            print("Test failed for item ", item)
    if not errorsFound:
        print("Everything seems to check out")

if __name__ == "__main__":
    main()
