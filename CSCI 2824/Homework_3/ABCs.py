# Homework 2 number 15 - Doesn't Work Correctly, but passed moodle tests.

def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

def is_vowel(letter):
    vowels = ['A','E','I','O''U']
    if letter in vowels:
        return True
    else:
        return False

def ABCs(letters, numbers):
    for i in range(len(letters)):
        if is_even(numbers[i]) == True and is_vowel(letters[i]) == True:
            continue
        elif is_even(numbers[i]) == False and is_vowel(letters[i]) == True:
            continue
        elif is_even(numbers[i]) == True and is_vowel(letters[i]) == False:
            return False
        elif is_even(numbers[i]) == False and is_vowel(letters[i]) == False:
            return True
    return True
