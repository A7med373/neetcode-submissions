class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if not s:
            return False
        valid = {ord('[') + ord(']'), ord('{') + ord('}'), ord('(') + ord(')')}
        for c in s:
            if stack and ord(c) + ord(stack[-1]) in valid:
                stack.pop()
            else:
                stack.append(c)
        return True if not stack else False
        