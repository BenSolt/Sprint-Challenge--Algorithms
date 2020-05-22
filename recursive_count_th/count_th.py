'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    # TBC
    # n = len(word)
    if len(word) < 2:
        return 0
    # get length of array, counts number of th's that are in each word
    elif len(word) == 'th':
        #if true, adds 1
        return 1 + count_th(word)
    else:
        return count_th(word)
    
print(count_th('theee'))
