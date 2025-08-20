class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_map = {}
        for i, num in enumerate(nums):
            difference = target - num
            if difference in num_map:
                return [num_map[difference], i]
            num_map[num] = i
        return []
                
solution = Solution()                
print(solution.twoSum([1,2,3,7,11,4,15],4))