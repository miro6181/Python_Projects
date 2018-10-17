def DecToBin(d):
    out_list = []
    new_num = d

    if d == 0:
        return [0]
    else:
        while new_num > 0:
            if new_num % 2 == 0:
                out_list.insert(0, 0)
                new_num = int(new_num/2)
            else:
                out_list.insert(0, 1)
                new_num = int((new_num-1)/2)

        return out_list

print(DecToBin(0))
