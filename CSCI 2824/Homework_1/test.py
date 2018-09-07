def BinToDec(binary_in):
    # initialize
    decimal_out = 0
    # add up the binary expression of the decimal number
    for position in range(0,len(binary_in)):
        decimal_out = decimal_out + binary_in[len(binary_in)-position-1]*(2** position)
    return (decimal_out)

print(BinToDec([1,0,1,0]))
