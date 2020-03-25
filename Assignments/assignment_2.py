# TODO:
# 1. Create a list of names and use a for loop to output the length of each name
# 2. Add an if check inside the loop to only output names longer than 5 characters
# 3. Add another if check to see whether a name includes an "n" or "N" characters
# 4. Use a while loop to empty the list of names (via pop())


name_list = ['Jim', 'Jan', 'Claire', 'Claire', 'Manacle', 'Art', 'Nana', 'Bon']

def name_len():
    for name in range(len(name_list)):
        print(name_list[name])


name_len()
