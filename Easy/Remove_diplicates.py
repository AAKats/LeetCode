class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        unique = 1
        i = 1
        while i < len(nums):
            if nums[i] != nums[i - 1]:
                nums[unique] = nums[i]
                unique += 1
            i += 1
        return unique 


solution = Solution()
print(solution.removeDuplicates([1,1,2]))