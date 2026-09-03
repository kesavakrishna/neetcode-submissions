class Solution:
    def encode(self, strs: List[str]) -> str:
        out = ""
        for s in strs:
            out += str(len(s)) + "#" + s
        return out

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":              # walk j forward over the digits
                j += 1
            length = int(s[i:j])            # the digits between i and j, as a number
            j += 1                          # step over the "#"
            result.append(s[j:j + length])  # copy exactly that many characters
            i = j + length                  # jump to where the next entry starts
        return result