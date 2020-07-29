"""
URLify: Write a method to replace all spaces in a string with "%20". You may assume that the string has sufficient space at the end to hold the additional
characters, and that you are given the "true" length of the string. (Please use a character array so that you can perform this operation in place.)
"""

def URLify(s, true_length):
    """
    We will edit the string starting from the end and working backwards since we have an extra buffer at the end.
    First pass: we count the number of spaces, and calculate the length of final string (true length + 2 * number of spaces, because each space becomes 3 times!)
    Second pass: we go from end to start, editing the string. If we come across a space, we replace it by "%20", otherwise copy the original character as it is.
    Time complexity: O(n)
    Space complexity: O(1)
    where n is the length of final string.
    """
    num_spaces = 0
    s = list(s)
    for i in range(true_length):
        if s[i] == " ":
            num_spaces += 1
    index = true_length + 2 * num_spaces
    
    for i in range(true_length-1, 0, -1):
        if s[i] == " ":
            s[index-1] = "0"
            s[index-2] = "2"
            s[index-3] = "%"
            index -= 3
            
        else:
            s[index-1] = s[i]
            index -= 1
            
    return "".join(s)
