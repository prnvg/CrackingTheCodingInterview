#Check Permutation: Given two strings, write a method to decide if one is a permutation of the other.

import collections
def checkPermutation(string1, string2):
    """
    Counting the number of occurrence of each letter in both strings and comparing the count of corresponding letters.
    If the count is same for each letter, then the strings are permutations, otherwise not.
    Time complexity: O(n)
    Space complexity: O(n)
    where n is assumed to be the length of each string.
    If the lengths are different, then the two strings are definitely not permutations, and we can simply return False.
    """
    if len(string1) != len(string2):
        return False
    counter1 = collections.Counter(string1)
    counter2 = collections.Counter(string2)
    if len(counter1) != len(counter2):
        return False
    for val in counter1:
        if counter2[val] != counter1[val]:
            return False
    return True

def checkPermutation1(string1, string2):
    """
    Sorting both the strings and then checking if the two resulting strings are the same.
    If they are exactly same, then the strings are permutations, otherwise not.
    Time complexity: O(nlogn)
    Space complexity: O(1)
    where n is assumed to be the length of each string.
    If the lengths are different, then the two strings are definitely not permutations, and we can simply return False.
    """
    if len(string1) != len(string2):
        return False
    string1 = sorted(string1)
    string2 = sorted(string2)
    
    return string1 == string2

#Testing...
string1 = "abba"
string2 = "bbaa"
string3 = "aaab"

checkPermutation(string1, string2) #True
checkPermutation1(string1, string2) #True
checkPermutation(string1, string3) #False
checkPermutation1(string1, string3) #False
