# Py uses "def" to declare functions and doesn't require a closing symbol to close the funciton. Instead it uses indents.
# def sampleFunction():
#     print("Hi there")


blockchain = []

def get_last_blockchain_value():
    return blockchain[-1]

def add_value(trans_amnt, last_transaction = [1]):
    blockchain.append([last_transaction, trans_amnt])

def get_user_input():
    return float(input('Your transaction amount, please: '))


tx_amount = get_user_input()
add_value(tx_amount)
tx_amount = get_user_input()
add_value(trans_amnt=get_last_blockchain_value(), last_transaction=[2])
tx_amount = get_user_input()
add_value(tx_amount, get_last_blockchain_value())

print(blockchain)
