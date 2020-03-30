#Given a string containing just the characters '(', ')',# '{', '}', '[' and ']', determine if the input string is valid.

#An input string is valid if:

#Open brackets must be closed by the same type of brackets.
#Open brackets must be closed in the correct order.

def isValid(s: str) -> bool:
   d = {'{':'}', '[': ']','(':')'}
   if s == []:
     return True
   stack =  []; 
   for i in range(len(s)):
      if s[i] in [')','}',']']:
        if stack == []:
          return False
        current =stack.pop()
        if d[current] != s[i]:
          return False;
      else:
        stack.append(s[i])
   if stack ==[]:
     return True

