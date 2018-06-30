def is_palindrome():
    return "malayalam" == ''.join(reversed("malayalam"))

res=is_palindrome()
if res == True:
  print("String is a palindrome")
else:
  print("String is not a palindrome")
