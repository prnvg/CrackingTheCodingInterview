#Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?

def normalise(string):
    """
    Used for normalizing the string before checking for uniqueness
    """
    string = string.replace(" ", "")
    string = string.lower()
    return string
    
def isUnique(string):
    """
    Brute Force approach using nested loops.
    Time complexity: O(n^2)
    Space complexity: O(1)
    where n = number of characters in the string
    """
    string = normalise(string)
    for i in range(len(string)):
        for j in range(i+1, len(string)):
            if string[i] == string[j]:
                return False
    return True

def isUnique1(string):
    """
    Optimal time approach using a hashmap.
    Time complexity: O(n)
    Space complexity: O(n)
    where n = number of characters in the string
    
    We can argue that Space complexity is O(1) since the string can only have a maximum of 26 letters
    """
    string = normalise(string)
    hashmap = dict()
    for i in string:
        if i in hashmap:
            return False
        hashmap[i] = True
        
    return True
    
def isUnique2(string):
    """
    Not using extra space and improving on Time complexity with sorting
    Time complexity: O(nlogn)
    Space complexity: O(1)
    where n = number of characters in the string
    """
    string = normalise(string)
    string = sorted(string)
    for i in range(1, len(string)):
        if string[i-1] == string[i]:
            return False
    return True
                       
#Testing...

string = "Qwertyuiop sadf zcv"
isUnique(string) #True
isUnique1(string) #True
isUnique2(string) #True


string = "Qwertyuiop q w T"
isUnique(string) #False
isUnique1(string) #False
isUnique2(string) #False
