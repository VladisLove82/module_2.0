my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]

first = 0
while first < len(my_list):

    if my_list[first] == 0:
        first = first + 1
        continue

    elif my_list[first] < 0:
        break

    print(my_list[first])
    first = first + 1