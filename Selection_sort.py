#Selection sort

def selection_sort(nums):
     n = len(nums)

     for i in range(n-1):
         min_index = i
         for j in range(i+1,n):
             if nums[j] < nums[min_index]:
                 nums[j],nums[min_index] = nums[min_index],nums[j]
     print(nums)

nums = [5,3,8,6,7,2]

selection_sort(nums)
