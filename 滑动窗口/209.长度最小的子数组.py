class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """

        length = len(nums)
        start = 0
        end = 0
        current_sum = 0
        current_length = 0
        min_length = float('inf')

        print(nums)


        # 双指针，sliding window
        while end < length:
            print("----------------")
            print(f"start: {start}")
            print(f"end: {end}")
            print(f"current window: {nums[start:end + 1]}")


            current_sum += nums[end]

            while current_sum >= target:
                print("------- inner loop ------")
                
                current_length = end - start + 1
                print(f"current sum: {current_sum}")
                print(f"current window: {nums[start:end + 1]}")

                if current_length < min_length:
                    min_length = current_length

                current_sum -= nums[start]
                start += 1


            end += 1

        return min_length if min_length != float('inf') else 0








    def BruteForce(self, target, nums):
        length = len(nums)
        min_length = float('inf')

        for i in range(length):
            current_sum  = 0
            result = []

            for j in range(i, length):
                current_sum += nums[j]
                result.append(nums[j])

                # print(f"current result: {result}")

                if current_sum >= target:
                    current_length = j - i + 1
                    print(f"current sum: {current_sum}")

                    if current_length < min_length:
                        min_length = current_length
                        print(result)

        return min_length if min_length != float("inf") else 0




# test case 1
target = 7
nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: The subarray [4,3] has the minimal length under the problem constraint.

# test case 2
# Input: target = 4, nums = [1,4,4]
# Output: 1

# test case 3
# Input: target = 11, nums = [1,1,1,1,1,1,1,1]
# Output: 0

solu = Solution()
# print(solu.BruteForce(target, nums))
print(solu.minSubArrayLen(target, nums))

