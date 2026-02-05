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


'''Another Two-Sum -- count all pairs equal to target'''
nums = [1, 1, 2, 3, 4, 4, 5]
target = 6

def count_pairs(nums, target):
    l, r = 0, len(nums)-1
    count = 0

    while l < r:
        s = nums[l] + nums[r]

        if s == target:
            count += 1

            left_v = nums[l]
            while l < r and nums[l] == left_v:
                l +=1

            right_v = nums[r]
            while l < r and nums[r] == right_v:
                r -= 1


        elif s < target:
            l += 1
        else:
            r -= 1

    return count

print(count_pairs(nums, target))


'''Two Pointer Problem: Container With Most Water -- '''

heights = [1,8,6,2,5,4,8,3,7]
# Output: 49

# Minimal / Boundary
tiny_pair = [1, 1]                  # expected = 1

# Monotonic
strictly_increasing = [1, 2, 3, 4, 5] # expected = 6

# Tall walls, skinny gap
tall_ends = [10, 1, 1, 1, 10]        # expected = 40

# Peaks and valleys
classic_peaks = [1, 8, 6, 2, 5, 4, 8, 3, 7]  # expected = 49

# Tricky pointer decision
false_tallest = [1, 3, 2, 5, 25, 24, 5]      # expected = 24

# Gotcha case
zero_inside = [0, 2, 0, 2]           # expected = 4

# Stress / intuition
alternating_peaks = [1, 100, 1, 100, 1, 100, 1]  # expected = 400


def max_area(heights):
    l, r = 0, len(heights) - 1
    max_water = 0

    while l < r:
        area = min(heights[l], heights[r]) * (r - l)
        if area > max_water:
            max_water = area
        elif l<r:
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        else:
            continue

    return max_water

print(max_area(heights))
print(max_area(tiny_pair))
print(max_area(strictly_increasing))
print(max_area(tall_ends))
print(max_area(classic_peaks))
print(max_area(false_tallest))
print(max_area(zero_inside))
print(max_area(alternating_peaks))
