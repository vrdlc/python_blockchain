#TODO:
    #1. Create two variables - one w/ name, one w/ age
    #2. Create a function which prints data as one string
    #3. Create a function which prints ANY data (two arguments) as one string
    #4. Create a function which calculates and returns the number of decades you have already lived


input_1 = input('Enter your name: ')
input_2 = input('Enter your age: ')

input_3 = input("Enter anything you like! ")
input_4 = input("May as well do it again! ")

def concat_name_age(input_1, input_2):
    """This function takes in user inputted name and age and concatenates them into a string

    Parameters
    ----------
    input_1 : string
        User's name, entered when prompted
    input_2 : int
        User's age, entered when prompted. Comes in as an int, but will convert to a string for the concatenation

    Returns
    -------
    type
        Concatenated string
    """

    name = input_1
    age = input_2
#    age = str(age)

    data = "Name: " + name + " Age: " + age
    print(data)

def concat_two_inputs(input_3, input_4):
    """Function takes two inputs and concatenates them

    Parameters
    ----------
    input_3 : string
        Description of parameter `input_3`.
    input_4 : string
        Description of parameter `input_4`.

    Returns
    -------
    type
        Description of returned object.

    """
    print(input_3 + " " + input_4)


def decade_calc():
    """Function calculats number of decades user has been alive

    Returns
    -------
    type
        Description of returned object.

    """
    age = int(input_2)
    total_decades = age/10
    print("You have been alive for " + str(total_decades) + " decades.")


concat_name_age(input_1, input_2)
concat_two_inputs(input_3, input_4)
decade_calc()
