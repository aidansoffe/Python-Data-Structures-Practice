def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False
    """
    brackets = ['()'] 
    while any(x in parens for x in brackets): 
        for br in brackets: 
            parens = parens.replace(br, '') 
    return not parens

print(valid_parentheses("()"))