# Py uses "def" to declare functions and doesn't require a closing symbol to close the funciton. Instead it uses indents.
# def sampleFunction():
#     print("Hi there")

# Initializing blockchain list
#genesis_block is the first default block to prevent empty array errors
genesis_block = {
        'previous_hash': '',
        'index': 0,
        'transactions': []
}
blockchain = [genesis_block]
open_transaction = []
owner = 'Eugene'


def get_last_blockchain_value():
    """ Returns the last value of the current blockchian (builds a docstring (doesn't work in Atom...)) """
    if len(blockchain) < 1:
        return None
    return blockchain[-1]

# This function accepts two arguments.
# One required one (trans_amnt) and one optional one (last_transaction)
# The optional one is optional because it has a default value => [1]
def add_transaction(recepient, sender = owner, amount = 1.0):
    """ Append a new value as well as the last value """
    """ Arguments:
        :sender: the sender of the values
        :recipient: the receiver of the values
        :amount: the value being sent (default is 1.0)
    """
    transaction = {
        'sender': sender,
        'recipient': recepient,
        'amount': amount
        }
    open_transaction.append(transaction)


def mine_block():
    #pass allows an empty function to not cause an error
    #pass
    last_block = blockchain[-1]
    hashed_block = '-'.join([str(last_block[key]) for key in last_block])
    print(hashed_block)
    # for keys in last_block:
    #     value = last_block[keys]
    #     hashed_block = hashed_block + str(value)

    print(hashed_block)

    block = {
            'previous_hash': hashed_block,
            'index': len(blockchain),
            'transactions': open_transaction
    }
    blockchain.append(block)

def get_transaction_value():
    """ Returns user input as a float """
    tx_recipient = input('Enter the recipient of the transation: ')
    tx_amount = float(input('Your transaction amount please: '))
    #tuple with one data pair doesn't need parens
    return (tx_recipient, tx_amount)

def get_user_choice():
    user_input = input('Your choice: ')
    return user_input

def print_blockchain_elements():
    # Output the blockchain list to the console
    for block in blockchain:
        print('Outputting Block')
        print(block)
    else:
        print('-' * 20)

def verify_chain():
    # block_index = 0
    is_valid = True
    for block_index in range(len(blockchain)):
        if block_index == 0:
            block_index += 1
            continue
        elif blockchain[block_index][0] == blockchain[block_index - 1]:
            is_valid = True
        else:
            is_valid = False
            break
    return is_valid

waiting_for_input = True

while waiting_for_input:
    print('Please choose')
    print('1: Add a new transaction value')
    print('2: Mine a new block')
    print('3: Output the blockchain blocks')
    print('h: Manipulate the chain')
    print('q: Quit')
    user_choice = get_user_choice()
    if user_choice == 1:
        tx_data = get_transaction_value()
        #this unpacks the tuple, placing the first element into recipient, the second into amount, etc, etc
        recipient, amount = tx_data
        #add transaction amount to blockchain
        add_transaction(recipient, amount=amount)
        print(open_transaction)
    elif user_choice == 2:
        mine_block()
    elif user_choice == 3:
        print_blockchain_elements()
    elif user_choice == 'h':
        if len(blockchain) >= 1:
            blockchain[0] = [2]
    elif user_choice == 'q':
        waiting_for_input = False
    else:
        print('You chose... poorly')
    # if not verify_chain():
    #     print_blockchain_elements()
    #     print('Invalid chain')
    #     break

else:
    print('User Left')

print('Done!')
