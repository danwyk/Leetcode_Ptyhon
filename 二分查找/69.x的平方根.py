class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        # 特殊情况， 如果 x == 0，那么结果只有0
        if x == 0:
            return 0
        
        # 平方根落在这个区间内
        left = 1
        right = (x / 2) + 1

        while left <= right:
            mid = (left + right) // 2
            
            # 这里不用 mid * mid == x 是因为，相乘出来，有可能超出 int 的大小限制
            if (mid == x / mid):
                return mid
            elif( mid > x / mid):
                right = mid - 1
            else:
                left = mid + 1

        return right




solu = Solution()

# test case 1
# x = 4

# test case 2
x = 8


print(solu.mySqrt(x))
