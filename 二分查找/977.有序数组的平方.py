import math

class Solution(object):

    # Given an integer array nums sorted in non-decreasing order, 
    # return an array of the squares of each number sorted in non-decreasing order.
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        print(nums)
        result = [0] * len(nums)

        # 三个指针， 左，右分别用来read数组，还有一个用来
        left = 0
        right = len(nums) - 1
        write = right

        # while write >= 0:
        while left <= right:

            print(f"left: {nums[left]}")
            print(f"right: {nums[right]}")

            print("abs left:", abs(nums[left]))
            print("abs right:", abs(nums[right]))


            if abs(nums[left]) > abs(nums[right]):
                print("左边大 left += 1")
                result[write] = nums[left] ** 2
                left += 1


            else:
                # abs(nums[left]) < abs(nums[right])
                print("右边大 right -= 1")
                result[write] = nums[right] ** 2
                right -= 1

            write -= 1

            # 一样大，也要先写入一个，再写入另一个
            # else:
            #     # abs(nums[left]) == abs(nums[right]):
            #     print("一样大 left += 1")
            #     left += 1

        # print(result)
        return result




        


solu = Solution()

# test case 1
nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].

# test case 2
nums = [-7,-3,2,3,11]
# Output: [4,9,9,49,121]

# test case 3
# nums = [-5,-3,-2,-1]

# test case 4
nums = [-7,-3,2,3,11]

print(solu.sortedSquares(nums))