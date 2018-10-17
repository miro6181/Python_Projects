#Doesn't work

def sequence_slayer(N):
    if N - 1 == 1 and N - 2 == 0:
        a_n = 7
    else:
        a_n = (N ** 2) * sequence_slayer(N - 1) - sequence_slayer(N - 2)
    return a_n


print(sequence_slayer(2))
