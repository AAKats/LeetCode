class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        if len(nums) <= 2:
            return len(nums)
        
        unique = 2
        i = 2
        
        while i < len(nums):
            if nums[i] != nums[unique - 2]:
                nums[unique] = nums[i]
                unique += 1
            i += 1
        return unique 


solution = Solution()
print(solution.removeDuplicates([1,1,1,2,2,3]))