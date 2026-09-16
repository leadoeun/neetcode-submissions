class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        alphanumeric = "abcdefghijklmnopqrstuvwxyz0123456789"
        while i < j:
            while i < len(s) and s[i].lower() not in alphanumeric:
                i += 1
            while s[j].lower() not in alphanumeric and j >= 0:
                j -= 1

            if i > j : 
                break
            if s[i].lower() != s[j].lower():
                return False
            
            i += 1
            j -= 1
        return True
        