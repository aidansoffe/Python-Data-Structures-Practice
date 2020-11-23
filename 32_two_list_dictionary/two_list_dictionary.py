def two_list_dictionary(keys, values):

    out = {}

    for idx, val in enumerate(keys):
        out[val] = values[idx] if idx < len(values) else None

    return out

print(two_list_dictionary(['a', 'b', 'c', 'd'], [1, 2, 3]))