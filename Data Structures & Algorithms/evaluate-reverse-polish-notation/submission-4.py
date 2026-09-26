class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = list()
        for t in tokens:
            if self.checkInt(t):
                stack.append(int(t))
            else:
                y = stack.pop()
                x = stack.pop()
                if t == "+":
                    stack.append(x + y)
                elif t == "-":
                    stack.append(x - y)
                elif t == "*":
                    stack.append(x * y)
                    # print(x * y)
                else: 
                    stack.append(int(x / y))
                    # print(x)
                    # print(y)
                    # print(x // y)
        return stack.pop()

    def checkInt(self, string):
        if string[:1] == "-":
            return string[1:].isdigit()
        else:
            return string.isdigit()