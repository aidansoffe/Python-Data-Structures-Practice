def two_oldest_ages(ages):
    uniq_ages = set(ages)
    oldest = None
    second = None
    
    for age in uniq_ages:
        if oldest is None or age > oldest:
            second = oldest
            oldest = age
        elif second is None or age > second:
            second = age
    
    return (second, oldest)

print(two_oldest_ages([1, 5, 5, 2]))