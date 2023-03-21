#!/Library/Frameworks/Python.framework/Versions/3.10/bin/python3
import os

#A phrase is a palindrome if, after converting all uppercase letters into
#lowercase letters and removing all non-alphanumeric characters, it reads
#the same forward and backward. Alphanumeric characters include letters
#and numbers.
#Given a string s, return true if it is a palindrome, or false otherwise.



class Solution:
    def isPalindrome(self, s: str) -> bool :
        a = ""
        for x in [*s]:
            if x.isalpha(): a += x.lower()
            if x.isnumeric(): a += x
        return a == a[::-1]

