"""
Given an array of string as input, create an array of the strings ending in e or t.
Input-> ["cat","bite","roar","had","lamb"]
Output-> ["cat","bite"]
"""

ls = ["cat","bite","roar","had","lamb"]
ln = len(ls)
st = []
for i in range(0,ln):
  e = ls[i]
  ch = e[i-1]
  if((e[-1]=='e') or (e[-1]=='t')):
    st += [e]
print(st)