class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        for i in range(len(strs[0])):
            ans = strs[0][i]
            for x in strs[1:]:
                if len(x) == i or x[i] != ans:
                    return strs[0][:i]
        return strs[0]