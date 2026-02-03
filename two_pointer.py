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

'''Given a string str, return True if it is a palindrome, otherwise False.'''

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





'''Two Sum Problem -- Return True if there exist two numbers in the array whose sum equals target.'''
nums = [1, 2, 4, 6, 9]
target = 6

def two_sum_sorted(nums, target):
    l, r = 0, len(nums) - 1

    while l < r:
        s = nums[l] + nums[r]

        if s == target:
            return True
        elif s < target:
            l += 1
        else:
            r -= 1

    return False

print(two_sum_sorted(nums, target))