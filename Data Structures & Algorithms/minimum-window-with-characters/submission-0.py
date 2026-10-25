from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        missing = len(t)
        left = 0
        result = ""

        for right, char in enumerate(s):
            
            if need[char] > 0:
                missing -= 1
            
            need[char] -= 1

            while missing == 0:
                if not result or right - left + 1 < len(result):
                    result = s[left:right + 1]

                need[s[left]] += 1

                if need[s[left]] > 0:
                    missing += 1
                
                left += 1
        return result