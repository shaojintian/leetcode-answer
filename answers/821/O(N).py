class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        if len(S) == 0:
            return []
        dp = [len(S) for _ in range(len(S))]
        for i in range(len(S)):
            if C == S[i]:
                dp[i] = 0
                continue
            #左右同时找
            pre,aft = i-1,i+1
            while pre >=0:
                if C == S[pre]:
                    dp[i] = i-pre
                    break
                else:
                    pre-=1
            while aft <= len(S) -1:
                if C==S[aft]:
                    dp[i] = min(dp[i],aft-i)
                    break
                else:
                    aft+=1
        return dp            









