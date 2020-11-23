def valid_parentheses(parens):
    brackets = ['()'] 
    while any(x in parens for x in brackets): 
        for br in brackets: 
            parens = parens.replace(br, '') 
    return not parens

print(valid_parentheses("()"))