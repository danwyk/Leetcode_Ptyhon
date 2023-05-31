from collections import defaultdict

class Solution(object):
    def totalFruit(self, fruits):
        # Fruit count in baskets
        basket = defaultdict(int)

        # Pointers to keep track of subarray
        start, end = 0, 0

        # Max number of fruits that can be picked
        max_fruits = 0
        
        # Iterate through fruit array
        # for r in range(len(fruits)):
        while end < len(fruits):

            basket[fruits[end]] += 1

            # If there is more then 2 fruits
            while len(basket) > 2:

                basket[fruits[start]] -= 1
                if basket[fruits[start]] == 0:
                    del basket[fruits[start]]

                start += 1

            if end - start + 1 > max_fruits:
                max_fruits = end - start + 1

            end += 1

        return max_fruits if max_fruits != float('inf') else 0


fruits = [1,2,1]
# Output: 3
# Explanation: We can pick from all 3 trees.


# Input: fruits = [0,1,2,2]
# Output: 3
# Explanation: We can pick from trees [1,2,2].
# If we had started at the first tree, we would only pick from trees [0,1].


# Input: fruits = [1,2,3,2,2]
# Output: 4
# Explanation: We can pick from trees [2,3,2,2].
# If we had started at the first tree, we would only pick from trees [1,2].


fruits = [3,3,3,1,2,1,1,2,3,3,4]


solu = Solution()
print(solu.totalFruit(fruits))