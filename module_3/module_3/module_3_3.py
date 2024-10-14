def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()
print_params(b = 25)
print_params(c = [1,2,3])

values_list = [10, 'вторая строка', False]
values_dict = {'a': 12, 'b': 'третья строка', 'c': None}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [7.2, 'четвёртная строка']
print_params(*values_list_2, 42)