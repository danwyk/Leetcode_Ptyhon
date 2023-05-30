class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """


        fast = 0 # 用来指下一个element
        slow = 0 # 用来指要更新的element

        while fast < len(nums):
            
            # 每次找到 val，都要把 slow 指向它，等待更新
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
            
            elif nums[fast] == val:
                fast += 1

        return slow


        