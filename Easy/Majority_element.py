class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if not nums:
            return 0
        if len(nums) <= 2:
            return nums[0]

        major = nums[0]
        max_count = 0
        set_nums = set(nums)
        for i in set_nums:
            if nums.count(i) > max_count:
                major = i
                max_count = nums.count(i)
        return major


        


solution = Solution()
print(solution.majorityElement([2,2,1,1,1,2,2,1,1]))