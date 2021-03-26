def isPalindrome(word):
    pass
    # for i in range(len(word)):
    #     if word[i] != word[-1 - i]:
    #         return False
    # return True

    # for i in range(len(word)):
    #     if word[i] != word[len(word) - 1 - i]:
    #         return False
    #     return True

    list1 = list(word)
    list2 = []
    list2 = list1.copy()
    list2.reverse()
    # print(list1)
    # print(list2)
    if list1 == list2:
        return True
    return False
# t o p o t
# 0 1 2 3 4
#-5-4-3-2-1
s = input()
print(isPalindrome(s))



