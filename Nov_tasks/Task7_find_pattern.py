import re

def isMatch(s, p):
    pattern = re.sub(r'\*', '.*', re.sub(r'\?', '.', p))
    return bool(re.match(pattern, s) and re.match(pattern, s).group() == s)

s = "cb"
p = "?a"
result = isMatch(s, p)
print(result)  
