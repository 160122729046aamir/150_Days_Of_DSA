class Solution(object):
    def removeDuplicates(self, nums):
        nums[:]={i for i in nums}
        return len(nums)
        
        
