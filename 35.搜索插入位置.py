import pdb


class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        left = 0
        right = len(nums) - 1

        while (left <= right):
            mid = left + (right - left) // 2
            print("mid", mid)


            if (nums[mid] == target):
                return mid
            elif (nums[mid] < target):
                left = mid + 1
                print("left", left)
            elif (nums[mid] > target):
                right = mid - 1
                print("right", right)

        return right + 1
        
solu = Solution()

# test case 1
# nums = [1, 3, 5, 6]
target = 2

# test case 1
nums = [1, 3, 5, 6]
target = 7

print(solu.searchInsert(nums, target))