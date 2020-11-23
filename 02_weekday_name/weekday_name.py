def weekday_name(num):

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