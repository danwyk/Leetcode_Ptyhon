class Solution(object):
    def removeDuplicates(self, nums):

        slow = 0
        for fast in range(1, len(nums)):
            
            if nums[slow] != nums[fast]:
                slow += 1 # 为了保证每个element只有一个，所以 +1 取其下一个 
                nums[slow] = nums[fast]
        
        return slow + 1 # 返回数组长度，所以要 +1 从 index 变成长度


solu = Solution()
nums = [1, 1, 2]
end = solu.removeDuplicates(nums)

print(nums[:end])
