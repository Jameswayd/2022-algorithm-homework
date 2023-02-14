"""
Given a array of length n, max_subarray_sum() finds
the maximum of sum of contiguous sub-array using divide and conquer method.

Time complexity : O(n log n)
"""

def max_subarray_sum(array, left, right):
    # base case: array has only one element
    if (left == right): 
        return array[left]
    # Recursion
    mid=int((left+right)/2)
    return max(max_subarray_sum(array, left, mid),
    max_subarray_sum(array, mid+1, right),
    maxCrossSum(array, left, mid, right))
        
def maxCrossSum(array, left, mid, right):
 
    #left 
    sum = 0
    left_sum = -10000
 
    for i in range(mid, left-1, -1):
        sum = sum + array[i]
 
        if (sum > left_sum):
            left_sum = sum
 
    #right 
    sum = 0
    right_sum = -10000
    for i in range(mid + 1, right + 1):
        sum = sum + array[i]
 
        if (sum > right_sum):
            right_sum = sum
    #return left right and cross mid sum
    return max(left_sum, right_sum,left_sum + right_sum)

'''
array2 = [-2, -5, 6, -2, -3, 1, 5, -6]
array_length = len(array2)
print(
    "Maximum sum of contiguous subarray2:", max_subarray_sum(array2, 0, array_length - 1))
)
'''
array = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
array_length = len(array)
print(
    "Maximum sum of contiguous subarray:", max_subarray_sum(array, 0, array_length - 1))

