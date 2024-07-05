class Solution(object):
    def removeElement(self, nums, val):
        k=0
        for i in range(0,len(nums)-k):
            if nums[i]==val:
                nums.pop(i)
                k =+ 1
        return len(nums)
        
        return nums
        
