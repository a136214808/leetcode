'''
Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
'''

s='()[]{}'
def isValid(s):
    bracket = {'(':')','{':'}','[':']'}

    l=[]
    if len(s)%2:
        return False

    for i in s:
        #put left breacket into list
        if i in bracket:
            l.append(i)
        #right bracket and list is empty(no match)
        elif i not in bracket and not l:
            return False
        #right bracet and list is not empty(compare top left bracket and right bracket)
        elif i not in bracket and l:
            tmp = l.pop()
            if bracket[tmp] != i:
                return False
    if l:
        return False

    return True

print(isValid(s))
