#Palindrome
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if(x<0):
            return(False)
        t=x
        r=0
        while(t!=0):
            digit=t%10
            r=(r*10)+digit
            t//=10
        return(r==x)