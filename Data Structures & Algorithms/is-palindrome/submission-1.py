class Solution:
    def isPalindrome(self, s: str) -> bool:
        front = 0
        back = len(s) - 1
        

        while front < back:
            if not((s[back].lower() >= 'a' and s[back].lower() <= 'z') or (s[back] >= '0' and s[back] <= '9')):
                back -= 1
                continue
            if not((s[front].lower() >= 'a' and s[front].lower() <= 'z') or (s[front] >= '0' and s[front] <= '9')):
                front += 1
                continue
            if s[front].lower() != s[back].lower(): 
                return False
            front += 1
            back -= 1
        
        return True