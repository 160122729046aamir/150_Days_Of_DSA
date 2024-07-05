class Solution(object):
    def removeDuplicates(self, nums):
        nums[:]={i for i in nums}
        nums.sort()
        return len(nums)
        
