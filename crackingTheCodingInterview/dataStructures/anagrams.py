#!/usr/bin/env python3

# Write a method to decide if two strings are anagrams or not.

def isAnagram(first: str, second: str):
    if len(first) != len(second):
        return False
    counts = {}
    for char in first:
        if char not in second:
            return False
        if first.count(char) != second.count(char):
            return False
    return True

def main():
    anagrams = [
        ["anagram", "margana"],
        ["racecar", "racecar"]
    ]
    notAnagrams = [
        ["abc123", "123zyx"],
        ["abc!@#", "abc!@3"],
        ["hello", "helo"]
    ]
    errorsFound = False
    for item in anagrams:
        try:
            assert(isAnagram(item[0], item[1]))
        except AssertionError:
            print("Error: Items (", item[0], ", ", item[1], ") are not an anagram")
            errorsFound = True
    for item in notAnagrams:
        try:
            assert(not isAnagram(item[0], item[1]))
        except AssertionError:
            print("Error: Items (", item[0], ", ", item[1], ") are an anagram")
            errorsFound = True
    if not errorsFound:
        print("Tests check out")

if __name__ == "__main__":
    main()
