__author__ = 'atalanki'


# Write a function to return if two words are exactly "one edit" away.
# bool OneEditApart(string s1, string s2);
# That returns true if two words are exactly one edit apart, where an edit is:
# Insert one character anywhere in the word (including at the beginning and end)
# Remove one character
# Replace exactly one character

def isOneEditApart(s1, s2):
    """
    :param s1: First word
    :param s2: Second word
    :return: True if they are 1 edit away, False otherwise
    """
    editCount = 0
    if abs(len(s1) - len(s2)) > 1:
        editCount = abs(len(s1) - len(s2))

    i = 0
    j = 0
    while editCount <= 1 and i < len(s1) and j < len(s2):
        if s1[i] != s2[j]:
            editCount += 1
            if (j + 1) < len(s2):
                if s1[i] == s2[j + 1]:
                    j += 1
            if (i + 1) < len(s1):
                if s1[i + 1] == s2[j]:
                    i += 1
        editCount = editCount + len(s1) - i + len(s2) - j
        i += 1
        j += 1

    print "Edit Count is %s" % editCount
    if editCount == 1:
        return True
    else:
        return False


# Testing
s1, s2 = 'xyz', 'xz'
print isOneEditApart(s1, s2)  # True
s1, s2 = 'xyz', 'xyk'
print isOneEditApart(s1, s2)  # True
s1, s2 = 'xy', 'xyz'
print isOneEditApart(s1, s2)  # True

s1, s2 = 'xyz', 'xyz'
print isOneEditApart(s1, s2)  # False
s1, s2 = 'xyz', 'xzy'
print isOneEditApart(s1, s2)  # False
s1, s2 = 'x', 'xyz'
print isOneEditApart(s1, s2)  # False
