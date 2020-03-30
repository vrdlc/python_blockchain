# TODO:
# 1. Create a list of names and use a for loop to output the length of each name DONE
# 2. Add an if check inside the loop to only output names longer than 5 characters DONE
# 3. Add another if check to see whether a name includes an "n" or "N" characters
# 4. Use a while loop to empty the list of names (via pop())


names = ['Jim', 'Jan', 'Claire', 'Manacle', 'Art', 'Nala', 'Bon', 'Jason', 'Nannette']
five_char = []
n_char = []

def name_len():
    i = 0

# This is the elegant solution, but I wanted my nested loops to work more effectively. I can get the required resultes, but it's not clean.
    for name in names:
        if len(name) >= 5 and 'n' in name:
            five_char.append(name)
    print(five_char)

    while five_char:
        print(five_char.pop())

    print(five_char)
#I was trying to use a for loop to pop out names when I needed a while loop...
    # for name in names:
    #     # print(name)
    #     # name_list[name] is the name in the array at that index point
    #     if len(name) >= 5:
    #         # This adds the a name > 5 characters to the array
    #         five_char.append(name)
    #         # print(five_char)
    #
    #         # I'm sure there's a match() style function, but I want to play with for loops
    #         for name in five_char:
    #             # print(name)
    #             # i = i + 1
    #             for char in name:
    #                 if char == 'n':
    #                     n_char.append(name)
    #                 else:
    #                     if len(five_char) <= 1:
    #                         break
    #
    #                 if five_char[char] == 'n':
    #                     n_char.append(name)
    #                     print(n_char)
    #             while five_char:
    #                 print(five_char.pop())



    # Remember to remove an indent to remove something from a loop but to keep it in the function. Python has no dedicated closing characters!
        # print(n_char)
        # print(five_char)

name_len()
