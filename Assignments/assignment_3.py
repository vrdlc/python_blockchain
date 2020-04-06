# TODO
# 1. Create a list of "person" dictionaries with a name, age, and list of hobbies for each one <**DONE**>
# 2. Use a list comprehension to convert this list of persons into a list of names (of the persons) <**DONE**>
# 3. Use a list comprehension to check whether all persons are older than twenty <**DONE**>
# 4. Copy the person list such that you can safely edit the name of the first person (without changing) the original list <**DONE**>
# 5. Upack the persons of the original list into different variables and output these VARIABLES <**DONE**>
eugene = {'name': 'Eugene', 'age':30, 'hobbies':['reading', 'writing', 'rithmatic']}
frank = {'name': 'Frank', 'age': 85, 'hobbies': ['napping', 'doing pushups', 'brawling']}
sally = {'name': 'Sally', 'age': 15, 'hobbies': ['cutting class', 'running a small business', 'not sleeping']}

persons = [eugene, frank, sally]
names = []
over_20 = []
n = len(names)

def list_names():
    for person in persons:
        names.append(person['name'])
    print(names)

def age_check():
    for person in persons:
        if person['age'] > 20:
            over_20.append(person['age'])
    print(over_20)

def copy_names():
    list_names()
    dup_names = names[:]
    dup_names[0] = 'Gene'
    print(names)
    print(dup_names)

def unpack_names():
    name_1, name_2, name_3 = names
    print(name_1)
    print(name_2)
    print(name_3)

copy_names()
age_check()
unpack_names()
