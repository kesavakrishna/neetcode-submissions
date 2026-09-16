class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = "".join(i.lower() for i in s if i.isalnum())
        return clean == clean[::-1]