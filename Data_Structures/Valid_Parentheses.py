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

print(isValid(''))
