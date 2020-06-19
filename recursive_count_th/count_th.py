'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    # base case
    if 'th' not in word:
        return 0
    # looks at first two letters in the string and counts them if equal to 'th'
    elif 'th' in word[0:2]:
        return count_th(word[1:]) + 1
    # if 'th' not first two letters in the string iterate by 1 to check next two
    else:
        return count_th(word[1:])


# Test
word = 'abcthxyzththabthabth'
print(count_th(word))
