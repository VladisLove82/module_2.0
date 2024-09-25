def password(_num):
    num_pass = ""
    for pass_check in range(1, _num):
        for pass_find in range(pass_check + 1, _num):
            if _num % (pass_check + pass_find) == 0:
                num_pass += (str(pass_check) + str(pass_find))

    print(f"{_num} - {num_pass}")

for i in range(3,21):
    password(i)
