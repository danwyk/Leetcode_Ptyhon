import pdb


class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        left = 0
        right = len(nums) - 1
        tmp_result = [-1, -1] # 规定 nums 中没有 target 的默认值

        # find right bound
        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                tmp_result[0] = mid
                right = mid - 1 # 向左 slide window

            elif nums[mid] > target:
                right = mid - 1

            else:
                # nums[mid] < target
                left = mid + 1


        # find left bound
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                tmp_result[1] = mid
                left = mid + 1 # 向右 slide window

            elif nums[mid] > target:
                right = mid - 1
            
            else:
                # nums[mid] < target
                left = mid + 1

        return tmp_result



solu = Solution()
nums = [5,7,7,8,8,10]
target = 6
print(solu.searchRange(nums, target))