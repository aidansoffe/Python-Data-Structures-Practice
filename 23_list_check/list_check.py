def list_check(lst):
    for item in lst:
        if isinstance(item, list):
            return True;

print(list_check([[1], [2, 3]]))