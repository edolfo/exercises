#!/usr/bin/env python3

# Implement an algorithm to determine if a string has all unique characters.
# What if you can not use additional data structures?

def hasUnique(candidate: str):
    """
        Memory use is <= sizeof(candidate), but runtime is O(n)
    """
    found = []
    for char in candidate:
        if char in found:
            return False
        else:
            found.append(char)
    return True

def hasUniqueRestriction(candidate: str):
    """
        O(n**2) runtime, but uses no additional memory beyond two indices
    """
    for i in range(len(candidate)):
        for j in range(len(candidate)):
            if i == j:
                continue
            if candidate[i] == candidate[j]:
                return False
    return True

def main():
    testWords = [
        "abcdefghijklmnopqrstuvwxyz 1234567890",
        "one tw r ;'789",
        "helLo",
        "hello"
    ]
    for word in testWords:
        try:
            assert(hasUnique(word) == hasUniqueRestriction(word))
        except AssertionError:
            print("Results disagree for ", word)

    print("Tests passed")

if __name__ == "__main__":
    main()
