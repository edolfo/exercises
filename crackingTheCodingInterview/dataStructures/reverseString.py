#!/usr/bin/env python3

# Implement an algorithm to determine if a string has all unique characters.
# What if you can not use additional data structures?

def _reverse(candidate: str):
    reversed = []
    strLen = len(candidate)
    for i in range(len(candidate)):
        if candidate[strLen - i - 1] != '\0':
            reversed.append(candidate[strLen - 1 - i])
    reversed.append('\0')
    return "".join(reversed)

def main():
    testStrings = [
        "racecar\0",
        "not a palindrome\0",
        "leper repel\0"
    ]
    for candidate in testStrings:
        print(candidate, " <--reversed-->", _reverse(candidate))

if __name__ == "__main__":
    main()
