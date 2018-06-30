def is_palindrome():
    return "malayalam" == "malayalam"[::-1]

res=is_palindrome()
if res == True:
  print("String is a palindrome")
else:
  print("String is not a palindrome")
