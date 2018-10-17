# Homework 2 number 16 - Done

def check_proposition(lst):
    for i in lst:
        if i % 2 == 0 and (i / 2) not in lst:
            return False
    return True

# Testing
print(check_proposition([-2, -1, 0, 1, 2, 3]))
print(check_proposition([-2, -1, 0, 1, 3, 4]))
