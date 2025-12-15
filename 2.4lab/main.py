def divisible_by(numbers, divisor=2):
    res = []
    for n in numbers:
        if n%divisor == 0:
            res.append(n)
    return res
print(divisible_by([10, 15, 20, 23], divisor=5))

def transform_numbers(numbers, transform_function=None):
    if transform_function is None:
        resb = []
        for n in numbers:
            if n>0:
                resb.append(n)
    else:
        resb = []
        for n in numbers:
            resb.append(transform_function(n))
    return resb
print(transform_numbers([1, 2, 3], transform_function=lambda x: x**2))

def sorted_values_by_keys(*dicts):
    alldicts = []
    for d in dicts:
        for key, value in d.items():
            alldicts.append((key, value))
    sorteddict = sorted(alldicts, key=lambda x: int(str(x[0])))
    res = []
    for key, value in sorteddict:
        res.append(value)
    return res
print(sorted_values_by_keys({'10': 'j'}, {'5': 'e', '15': 'o'}))

def common_keys_in_dicts(*dicts):
    common_keys = []
    for key in dicts[0]:
        keyin = True
        for i in range(1, len(dicts)):
            if key not in dicts[i]:
                keyin = False
                break
        if keyin:
            common_keys.append(key)
    result = {}
    for key in common_keys:
        result[key] = dicts[-1][key]
    return result
print(common_keys_in_dicts({'x': 5, 'y': 6}, {'y': 7, 'z': 8}, {'y': 9, 'w': 10}))
