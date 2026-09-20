class Solution:
    def isPalindrome(self, s: str) -> bool:
        s="".join(char.lower() for char in s if char.isalnum())
        for i in range(len(s)//2):
            j=len(s)-1-i
            if s[i]!=s[j]:
                return False
        return True