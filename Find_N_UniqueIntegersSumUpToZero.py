# Question
# Given an integer n, return any array containing n unique integers such that they add up to 0.
# Example 1:

# Input: n = 5
# Output: [-7,-1,1,3,4]
# Explanation: These arrays also are accepted [-5,-1,1,2,3] , [-3,-1,2,-2,4].

class Solution:
    def sumZero(self, n: int) -> List[int]:
        ans = []
        if(n%2 == 0):
            for i in range(0,math.floor(n/2)):
                ans.insert(i,i+1)
                ans.insert(n-i,(i+1)*-1)
        else:
            x = math.ceil(n%2)
            ans.insert(x,0)
            for i in range(0,math.floor(n/2)):
                ans.insert(i,i+1)
                ans.insert(n-i,(i+1)*-1)
        return ans
