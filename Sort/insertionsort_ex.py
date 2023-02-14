from array import array

def insertionsort(A):

    for i in range(1,len(A)):
        Key=A[i]
        j=i-1
        while j >= 0 and Key < A[j]:
            A[j + 1] = A[j]
            j=j-1

        A[j + 1] = Key
    return A
nums1 = [5, 2, 4, 6, 1, 3]
nums2 = [6, 5, 4, 3, 2, 1]
print(insertionsort(nums1))
print(insertionsort(nums2))
