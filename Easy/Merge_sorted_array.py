class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return nums1
        elif m == 0:
            for i in range(len(nums2)):
                nums1[i] = nums2[i]
            return nums1
        else:
            nums1[m:] = nums2
            for i in range(1, len(nums1)):
                key = nums1[i]
                j = i - 1
                while j >= 0 and nums1[j] > key:
                    nums1[j + 1] = nums1[j]
                    j -= 1
                nums1[j + 1] = key
            return nums1
        
solution = Solution()                
print(solution.merge([1,2,3,0,0,0],3,[2,5,6],3))