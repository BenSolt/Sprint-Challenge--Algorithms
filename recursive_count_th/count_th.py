'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    # TBC
    
    # get length of array, counts number of th's that are in each word
    if "th" in word:
        #if true, adds 1
        return 1, True
    else:
        #do nothing
        return 0, False


    # if "th" in word:
    #     print('true') 
    # else:
    #     print('false')


    if len(word) > 2:
        return "a"
    else:
        return "b"
   


    
print(count_th('theeth'))
