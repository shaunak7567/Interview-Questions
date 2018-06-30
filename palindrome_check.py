def isPalindrome(str):
 
    # Run loop from 0 to len/2 
    for i in range(0, len(str)//2): 
        if str[i] != str[len(str)-i-1]:
            return False
    return True
 
# main function
s = "malayalam"
ans = isPalindrome(s)
 
if (ans):
    print("Yes!!! The String is a palindrome")
else:
    print("No!!! The String is not a palindrome")
