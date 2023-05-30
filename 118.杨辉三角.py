import pdb

class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = []

        for i in range(numRows):
            last_row = i
            current_row = i + 1

            if current_row == 1:
                result.append([1])

            elif current_row == 2:
                result.append([1, 1])

            else:
                level = [1]
                
                for j in range(1, last_row):
                    level.append(result[-1][j - 1] + result[-1][j])

                level.append(1)
                result.append(level)

        return result


# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

numRows = 5
solu = Solution()
print(solu.generate(numRows))
