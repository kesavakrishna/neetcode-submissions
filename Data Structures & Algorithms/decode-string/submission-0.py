class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        current = ""
        number = 0

        for char in s:
            if char.isdigit():
                number = number * 10 + int(char)
            elif char == '[':
                stack.append((current, number))
                current = ""
                number = 0
            elif char == ']':
                prev_string, repeat = stack.pop()
                current = prev_string + repeat * current

            else:
                current += char
            
        return current