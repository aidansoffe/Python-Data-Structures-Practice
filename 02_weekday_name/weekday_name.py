def weekday_name(num):
    """Return name of weekday.
    
        >>> weekday_name(1)
        'Sunday'
        
        >>> weekday_name(7)
        'Saturday'
        
    For days not between 1 and 7, return None
    
        >>> weekday_name(9)
        >>> weekday_name(0)
    """
    if num < 1 or num > 7:
        return None
    elif num == 1:
        return ("Monday")
    elif num == 2:
        return ("Tuesday")
    elif num == 3:
        return ("Wednesday")
    elif num == 4:
        return ("Thursday")
    elif num == 5:
        return ("Friday")
    elif num == 6:
        return ("Saturday")
    elif num == 7:
        return ("Sunday")

       



print(weekday_name(44))              