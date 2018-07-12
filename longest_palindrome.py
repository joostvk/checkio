
def longestPalindromic(s):
    if len(s) == 1 or s == '':
        return str(len(s)) 
    else:
        if s == s[::-1]:
            return s
        else:
            for i in range(len(s)-1, 0, -1):
                for j in range(len(s)-i+1):
                    temp = s[j:j+i]
                    if temp == temp[::-1]:
                        return temp
                    
longestPalindromic("artrartrt") == "rtrartr"
longestPalindromic("abacada") == "aba"
longestPalindromic("aaaa") == "aaaa"

s = "12345"
s[::-1]
str(len(s))

