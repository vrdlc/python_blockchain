# Py uses "def" to declare functions and doesn't require a closing symbol to close the funciton. Instead it uses indents.
# def sampleFunction():
#     print("Hi there")

# Initializing blockchain list
blockchain = []

def get_last_blockchain_value():
    """ Returns the last value of the current blockchian (builds a docstring (doesn't work in Atom...)) """
    return blockchain[-1]

def add_value(trans_amnt, last_transaction = [1]):
    """ Append a new value as well as the last value """
    """ Arguments:
        :trans_amnt: the amount to add
        :last_transaction: the last blockchain transaction (default [1]) """
    blockchain.append([last_transaction, trans_amnt])

def get_user_input():
    """ Returns user input as a float """
    return float(input('Your transaction amount, please: '))


tx_amount = get_user_input()
add_value(tx_amount)
tx_amount = get_user_input()
add_value(trans_amnt=get_last_blockchain_value(), last_transaction=[2])
tx_amount = get_user_input()
add_value(tx_amount, get_last_blockchain_value())
get_user_input()

print(blockchain)
