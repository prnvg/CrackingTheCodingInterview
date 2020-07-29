#Check Permutation: Given two strings, write a method to decide if one is a permutation of the other.

import collections
def checkPermutation(string1, string2):
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
    if len(string1) != len(string2):
        return False
    string1 = sorted(string1)
    string2 = sorted(string2)
    
    return string1 == string2

string1 = "abba"
string2 = "aaba"

checkPermutation1(string1, string2)
