# TODO:
# 1. Create a list of names and use a for loop to output the length of each name
# 2. Add an if check inside the loop to only output names longer than 5 characters
# 3. Add another if check to see whether a name includes an "n" or "N" characters
# 4. Use a while loop to empty the list of names (via pop())


name_list = ['Jim', 'Jan', 'Claire', 'Claire', 'Manacle', 'Art', 'Nana', 'Bon']
five_char = []

def name_len():
    # 'name' is the index point
    for name in range(len(name_list)):
        # name_list[name] is the name in the array at that index point
        if len(name_list[name]) >= 5:
            # This adds the a name > 5 characters to the array
            five_char.append(name_list[name])
        else:
            continue

    # Remember to remove an indent to remove something from a loop but to keep it in the function. Python has no dedicated closing characters!
    print(five_char)


name_len()
