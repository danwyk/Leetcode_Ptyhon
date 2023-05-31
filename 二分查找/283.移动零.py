class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """


        fast = 1
        slow = 0

        while fast < len(nums):
            if nums[fast] != 0 and nums[slow] == 0:
                tmp = nums[slow]
                nums[slow] = nums[fast]
                nums[fast] = tmp
                

            # slow 始终指到需要更新的位置，就是 0 所在
            if nums[slow] != 0:
                slow += 1
        
            fast += 1
        
solu = Solution()
nums = [0,1,0,3,12]

solu.moveZeroes(nums)
print(nums)