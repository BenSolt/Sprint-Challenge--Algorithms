'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    # TBC
    
    # 1. get length of list (array) of word
    # 2. count number of "th" that are in each word
    # 3. add 1 for each set of "th" that occures in said word.
    # 4. Return/print number of times th occured.
    
    # -- need to loop..somehow the number of times "th" occures in said
    # word and add 1 each time.. Not sure.

    # lenght of word = 0
    if len(word) == 0:
        return 0
    # if "th" in word:
    # example: word "the" contains th
    if (word[:len("th")] == "th"):
        # lenght of word contains "th" + 1
        return count_th(word[len("th"):]) + 1
    else:
        #do nothing
        return count_th(word[len("th") -1:])
        

# def factorial(x):

#     if x == 1:
#         return 1
#     else:
#         return (x * factorial(x-1))

    # if len(word) > 2:
    #     return "a"
    # else:
    #     return "b"
   
print(count_th('tee'))


    

