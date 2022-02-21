# Author: Esteban Cajamarca
# GitHub username: EstebanCajamarca
# Date: 2/19/2022

# Write a function named count_letters that takes as a parameter a string and returns a dictionary that tabulates how
# many of each letter is in that string. The string can contain characters other than letters, but only the letters
# should be counted. The string could even be the empty string (just ""). Lower-case and upper-case versions of a
# letter should be part of the same count. The keys of the dictionary should be upper-case letters. If a letter does
# not appear in the string, then it would not get added to the dictionary

def count_letters(string):
    import re
    """counts all the letters in a given string, lower and upper case"""
    new_string = re.sub(r"[^a-zA-Z0-9]", "", string) # removing special characters from string.
    letter_dict = dict()
    for x in new_string:
        x = x.upper()  # makes lowercase upper
        if x not in letter_dict:
            letter_dict[x] = 1
        else:
            letter_dict[x] += 1
    return letter_dict

""" Testing
print(count_letters("Quis custodiet ipsos custodes?"))
"""