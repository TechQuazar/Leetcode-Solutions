class Solution:
    def calculate(self, s: str) -> int:
        def helper(chars):
            stack = []
            num = 0
            op = '+'

            while chars:
                ch = chars.pop(0)

                if ch.isdigit():
                    num = num * 10 + int(ch)
                if ch == '(':
                    num = helper(chars)  # evaluate subexpression
                if ch in '+-*/)' or not chars:
                    if op == '+':
                        stack.append(num)
                    elif op == '-':
                        stack.append(-num)
                    elif op == '*':
                        stack.append(stack.pop() * num)
                    elif op == '/':
                        stack.append(int(stack.pop() / num))  # truncate toward zero
                    num = 0
                    op = ch
                if ch == ')':
                    break

            return sum(stack)

        # Preprocess: remove spaces and turn string into list for easy pop(0)
        return helper(list(s.replace(" ", "")))
