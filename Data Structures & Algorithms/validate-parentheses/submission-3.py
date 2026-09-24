class Solution:
    def isValid(self, s: str) -> bool:
        pair = {"(": ")", "{": "}", "[": "]"}
        if len(s) == 0:
            return True
        elif len(s) % 2 != 0:
            return False
        else:
            front = []
            for i in range(len(s)):
                if s[i] in pair.keys():
                    front.append(s[i])
                else:
                    if s[i] in pair.values() and len(front) == 0:
                        return False
                    elif pair[front.pop()] != s[i]:
                        return False
        if len(front) != 0:
            return False
        return True
        