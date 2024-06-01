class Solution:
    def removeOuterParentheses(self, S):
        res = ""
        count = 0
        first = 0
        for i in range(len(S)):
            if S[i] == "(":
                count +=1
            else:
                count -= 1
            
            if(count == 0):
                res +=(S[first+1:i])
                first = i+1
        return res