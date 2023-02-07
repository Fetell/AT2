my_dict = {'a': 500, 'b': 5874, 'c': 560, 'd': 400, 'e': 5874, 'f': 20}
for key, value in sorted(my_dict.items(), key=lambda x: x[1], reverse=True)[:3]:
    print(key, "", end="")
