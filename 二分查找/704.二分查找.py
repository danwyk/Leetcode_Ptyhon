import pdb


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        print(nums)
        print("--------------")

        while (left <= right):
            print(f"current left: {left}")
            print(f"current right: {right}")
            
            mid = left + (right - left) // 2
            print(f"current mid: {mid}")
            print(f"current num: {nums[mid]}")

            if (nums[mid] == target):
                print("-------- 等于 target ---------")
                return mid;

            elif (nums[mid] > target):
                print("-------- 大于 target ---------")
                right = mid - 1
            else:
                # target > nums[mid]
                print("-------- 小于 target ---------")
                left = mid + 1

        return -1

solu = Solution()
# test case 1
# nums = [-1,0,3,5,9,12]
# target = 9

# test case 2
nums = [-1, 0, 5]
target = -1




print(f"index is {solu.search(nums, target)}")



