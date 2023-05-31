class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        sPrime = []
        tPrime = []


        # 处理 s
        for i in s:

            # 数组不为空，且 current char == '#'
            if i == '#' and len(sPrime) != 0:
                print(f"丢掉 {tmp}")
                tmp = sPrime.pop()
            
            # 数组为空，current char != '#'
            elif i != '#':
                print(f"加入 {i}")
                sPrime.append(i)

            print(f"目前的s: {sPrime}")

        print("==============")


        # 处理 t
        for i in t:

            # 数组不为空，且 current char == '#'
            if i == '#' and len(tPrime) != 0:
                print(f"丢掉 {tmp}")
                tmp = tPrime.pop()
            
            # 数组为空，current char != '#'
            elif i != '#':
                print(f"加入 {i}")
                tPrime.append(i)

            print(f"目前的t: {tPrime}")

        
        
        # 长度不一样，一定是 False
        if len(sPrime) != len(tPrime):
            return False
        
        else:

            # 遍历数组，一旦有一位不一样，就是 False
            for i in range(len(sPrime)):
                if sPrime[i] != tPrime[i]:
                    return False
        
        return True
            

            
            

# test case 1
# Input: 
# s = "ab#c"
# t = "ad#c"
# Output: true
# Explanation: Both s and t become "ac".

# test case 2
# Input: 
# s = "ab##"
# t = "c#d#"
# Output: true
# Explanation: Both s and t become "".

# test case 3
s = "y#fo##f"
t = "y#f#o##f"

solu = Solution()
print(solu.backspaceCompare(s, t))
