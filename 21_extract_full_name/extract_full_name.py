def extract_full_names(people):
    return [f"{fullName['first']} {fullName['last']}" for fullName in people]


names = [
             {'first': 'Ada', 'last': 'Lovelace'},
             {'first': 'Grace', 'last': 'Hopper'},
         ]

print(extract_full_names(names))