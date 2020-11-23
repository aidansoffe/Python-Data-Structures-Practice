def min_max_keys(d):
    keys = d.keys()

    return (min(keys), max(keys))

print(min_max_keys({"apple": "red", "cherry": "red", "berry": "blue"}))