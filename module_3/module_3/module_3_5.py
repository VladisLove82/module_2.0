def get_multiplied_digits(number):
    if number == 0:
        return 0

    str_number = str(number)
    first = int(str_number[0])

    if first == 0:
        return first * get_multiplied_digits(int(str_number[1:]))
    if len(str_number) > 2:
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return first


result1 = get_multiplied_digits(40203)
print(result1)

result2 = get_multiplied_digits(0)
print(result2)

result3 = get_multiplied_digits(4020)
print(result3)