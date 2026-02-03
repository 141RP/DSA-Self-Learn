'''
Two Pointer:
l and r move towards each other, swapping elements in l and r spots
'''

#typical style
def reverse(arr):
    l, r = 0, len(arr) -1
    while l < r:
        arr[l], arr[r] = arr[r], arr[l]
        l +=1
        r +=1


def is_palindrome(str):
    l,r = 0, len(str)-1
    while l < r and not str[l].isalnum():
        l += 1
    while l < r and not str[r].isalnum():
        r -= 1

    if str[l].lower() != str[r].lower():
        return False

    l += 1
    r -= 1

    return True

print(is_palindrome("A man, a plan, a canal: Panama"))
print(is_palindrome("Meow! Woof! Oink!"))