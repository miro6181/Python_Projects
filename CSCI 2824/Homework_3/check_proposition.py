# Homework 2 number 16 - Not correct

def check_proposition(lst):
    for i in lst:
        if i % 2 == 0:
            for j in lst:
                if i == 2*j:
                    return True
                    break
                else:
                    continue

    return False


print(check_proposition([-2,-1,0,1,3,4]))
