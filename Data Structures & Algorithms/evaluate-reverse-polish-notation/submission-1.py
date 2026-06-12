class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = {'+', '-', '*', '/'}
        if len(tokens) == 1:
            return tokens[0]
        for token in tokens:
            # 2 1 + 3 *
            stack.append(token)
            if len(stack) > 2:
                if token in operations:
                    stack.pop()
                    b = int(stack.pop())
                    a = int(stack.pop())
                    if token == '+':
                        stack.append(a + b)
                    elif token == '-':
                        stack.append(a - b)
                    elif token == '*':
                        stack.append(a * b)
                    elif token == '/':
                        stack.append(a / b)
        return stack[0]
