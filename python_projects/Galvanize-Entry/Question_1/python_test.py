# Challenge 1 - Done
# def letter_counter(path_to_file, letters_to_count):
#     new_dict = {}
#     with open(path_to_file) as in_file:
#         f = in_file.read()
#         for char in f:
#             if char in letters_to_count:
#                     new_dict[char] = f.count(char)
#     return new_dict
#
# print(letter_counter('test.txt', 'aeiouAEIOU'))

#Challenge 2 - Done
# def remove_item(list_items, item_to_remove):
#     if item_to_remove in list_items:
#         return [item for item in list_items if item != item_to_remove]
#     else:
#         return 'The item is not in the list.'
#
# print(remove_item([1,3,7,8,0], 7))

#Challenge 3 - Done
# def cipher(text, cipher_alphabet, option='encipher'):
#     new_str = ''
#     if option == 'encipher':
#         for char in text:
#             if char == ' ':
#                 new_str += char
#             else:
#                 new_str += cipher_alphabet[char]
#         return new_str
#     elif option == 'decipher':
#         for char in text:
#             if char == ' ':
#                 new_str += char
#             else:
#                 new_str += list(cipher_alphabet.keys())[list(cipher_alphabet.values()).index(char)]
#         return new_str
#     else:
#         return 'Please Select a valid option.'
#
# d = dict(zip('abcdefghijklmnopqrstuvwxyz','phqgiumeaylnofdxjkrcvstzwb'))
# print(cipher('defend the east wall of the castle', d))

#Challenge 4 - Done
# def count_isograms(list_of_words):
#     return [len(set(x)) == len(x) for x in list_of_words].count(True)
#
# print(count_isograms(['conduct', 'letter', 'contract', 'hours', 'interview']))

# Challenge 5 - Done
# from itertools import combinations
#
# def matching_pairs(data_list):
#     vowels = 'aeiou'
#     matches = []
#     for combo in list(combinations(data_list, 2)):
#         if (combo[0][0] in vowels and combo[1][0] in vowels) and ((combo[0][1] + combo[1][1]) % 3 == 0):
#             matches.append((data_list.index(combo[0]), data_list.index(combo[1])))
#         elif (combo[0][0] not in vowels and combo[1][0] not in vowels) and ((combo[0][1] + combo[1][1]) % 3 == 0):
#             matches.append((data_list.index(combo[0]), data_list.index(combo[1])))
#     return matches
#
#
# data = [('a', 4), ('b', 5), ('c', 1), ('d', 3), ('e', 2), ('f', 6)]
# print(matching_pairs(data))
