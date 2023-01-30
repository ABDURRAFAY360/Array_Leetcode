class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        temp = s.split()
        temp = temp[0:k]
        ans = " "
        return ans.join(temp)

