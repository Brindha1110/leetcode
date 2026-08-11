class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def findBound(isFirst):
            left, right = 0, len(nums) - 1
            bound = -1
            
            while left <= right:
                mid = (left + right) // 2
                
                if nums[mid] == target:
                    bound = mid
                    if isFirst:
                        right = mid - 1  # Keep searching left to find the first occurrence
                    else:
                        left = mid + 1   # Keep searching right to find the last occurrence
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
                    
            return bound

        start = findBound(isFirst=True)
        if start == -1:
            return [-1, -1]
            
        end = findBound(isFirst=False)
        return [start, end]

