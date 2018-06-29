def reverseStr(s):
  return ' '.join([x[::-1] for x in s.split(' ')])

st=reverseStr("This is a test for test reversal")
print(st)
