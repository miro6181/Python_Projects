def ParityParty(d):
    out_list = []

    out_list.append(0) if d % 2 == 0 else out_list.append(1)
    out_list.append(int(d/2)) if d % 2 == 0 else out_list.append(int((d-1)/2))


    #Longer way to do it
    # if d % 2 == 0:
    #     out_list.append(0)
    #     out_list.append(int(d/2))
    # else:
    #     out_list.append(1)
    #     out_list.append(int((d-1)/2))

    return(out_list)

print(ParityParty(33))
