def quick_sort(nums,low,high):
   if len(nums) == 1:
      return nums
   if low < high:
      mid = partition(nums, low, high)
      quick_sort(nums,low,mid-1)
      quick_sort(nums,mid+1,high-1)
	
def partition(nums,low,high):
   i= low - 1
   comparison_num = nums[high]
   for j in range(low,high):
      if nums[j] <= comparison_num :
         i = i + 1
         nums[i] , nums[j] = nums[j] ,nums[i]
   nums[i+1], nums[high] = nums[high], nums[i+1]
   return (i+1) 
	
if __name__ == "__main__":
   nums = [2,8,7,1,3,5,6,4]
   nums2 = [8,7,6,5,4,3,2,1]
   quick_sort(nums, 0, len(nums)-1)
   quick_sort(nums2, 0, len(nums2)-1)
   print(nums)
   print(nums2)
   
  