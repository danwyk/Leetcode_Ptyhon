import math
import pdb


class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """

        result = []

        # base case
        if rowIndex == 0:
            result.append(1)

        elif rowIndex == 1:
            result.append(1)
            result.append(1)

        else:
            # append left most 1
            result.append(1)
            
            last_row = self.getRow(rowIndex - 1)
            # print(f"----------- current row: {rowIndex}---------------")
            
            # print(f"last row length: {len(last_row)}")
            # print(f"last row: {last_row}")

            for i in range(rowIndex - 1):
                # print("========")
                # print(f"i: {i}")
                # print(f"last row[i]: {last_row[i]}")
                # print(f"last row[i + 1]: {last_row[i + 1]}")
                
                tmp = last_row[i] + last_row[i + 1]

                result.append(tmp)
            
            # append right most 1
            result.append(1)
        
        return result


solu = Solution()

# test case 1
# Input: rowIndex = 3
# Output: [1,3,3,1]


# test case 2
# Input: rowIndex = 0
# Output: [1]


# test case 3
# Input: rowIndex = 1
# Output: [1,1]

rowIndex = 1
print(solu.getRow(rowIndex))


