__author__ = 'atalanki'


# Write a function to return if two words are exactly "one edit" away.
# bool OneEditApart(string s1, string s2);
# That returns true if two words are exactly one edit apart, where an edit is:
# Insert one character anywhere in the word (including at the beginning and end)
# Remove one character
# Replace exactly one character

def OneEditApart(s1, s2):
    """
    :param s1: First word
    :param s2: Second word
    :return: True if they are 1 edit away, False otherwise
    """
    if abs(len(s1) - len(s2)) > 1:
        return False
    return True


str1 = 'abc'
str2 = 'defef'

print OneEditApart(str1, str2)
