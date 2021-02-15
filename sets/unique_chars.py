# Problem: Is Unique
# Write a method name unique_chars which accepts a string as input parameters
# Function returns true if string contains all unique characters
# Else it will return False

def unique_chars(s):
    string_list = list(s)
    unique_list = list(set(s))
    return sorted(unique_list) == sorted(string_list)

if __name__ == '__main__':

    sample = ['abcd', 'abcdeb', 'zzy']
    for s in sample:
        print('String', s, ' contains unique characters?', unique_chars(s))
