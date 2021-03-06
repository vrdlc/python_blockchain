# Py uses "def" to declare functions and doesn't require a closing symbol to close the funciton. Instead it uses indents.
# def sampleFunction():
#     print("Hi there")

# Initializing blockchain list
#genesis_block is the first default block to prevent empty array errors

""" VARIABLES """

MINING_REWARD = 10 #All caps to indicate an immutable variable

GENESIS_BLOCK = {
        'previous_hash': '',
        'index': 0,
        'transactions': []
}

blockchain = [GENESIS_BLOCK]
open_transactions = []
owner = 'Eugene'
participants = {'Eugene'}

""" FUNCTIONS """

def hash_block(block):
    """ TODO """
    return '-'.join([str(block[key]) for key in block])



def get_balance(participant):
    """ Takes a user as an input, breaks out the amount of coin a user has and how much they are attempting to send, and returns the new balance """
    """ Arguments:
        :participant: currently (as of Lesson 4) just a user name
    """
    tx_sender = [[tx['amount'] for tx in block['transactions'] if tx['sender'] == participant] for block in blockchain]
    open_tx_sender = [tx['amount'] for tx in open_transactions if tx['sender'] == participant]
    tx_sender.append(open_tx_sender)
    amount_sent = 0

    for tx in tx_sender:
        if len(tx) > 0:
            amount_sent += tx[0]
    tx_recipient = [[tx['amount'] for tx in block['transactions'] if tx['recipient'] == participant] for block in blockchain]
    amount_received = 0
    for tx in tx_recipient:
        if len(tx) > 0:
            amount_received += tx[0]
    return amount_received - amount_sent

def get_last_blockchain_value():
    """ Returns the last value of the current blockchian (builds a docstring (doesn't work in Atom...)) """
    if len(blockchain) < 1:
        return None
    return blockchain[-1]

def verify_transaction(transaction):
    """ Verifies that sender has enough coins to complete a transaction """
    """ Arguments:
        :transaction: a dictionary including sender, recipient, and amount to be sent
    """
    sender_balance = get_balance(transaction['sender'])
    return sender_balance >= transaction['amount']

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
    if verify_transaction(transaction):
        open_transactions.append(transaction)
        participants.add(sender)
        participants.add(recipient)
        return True
    return False


def mine_block():
    """ Allows a user to mine a block, adding funds to their account """
    last_block = blockchain[-1]
    hashed_block = hash_block(last_block)
    reward_transaction = {
        'sender': 'MINING',
        'recipient': owner,
        'amount': MINING_REWARD
    }
    copied_transactions = open_transactions[:]
    copied_transactions.append(reward_transaction)
    block = {
            'previous_hash': hashed_block,
            'index': len(blockchain),
            'transactions': copied_transactions
    }
    blockchain.append(block)
    return True

def get_transaction_value():
    """ Returns user input as a float """
    tx_recipient = input('Enter the recipient of the transation: ')
    tx_amount = float(input('Your transaction amount please: '))
    #tuple with one data pair doesn't need parens
    return (tx_recipient, tx_amount)

def get_user_choice():
    """ Gathers user input from selection options """
    user_input = input('Your choice: ')
    return user_input

def print_blockchain_elements():
    """ Returns the elements of the current blockchain """
    # Output the blockchain list to the console
    for block in blockchain:
        print('Outputting Block')
        print(block)
    else:
        print('-' * 20)

def verify_chain():
    """ Verify the current chain and return True if it's valid, False if it's not """
    for (index, block) in enumerate(blockchain):
        if index == 0:
            continue
        if block['previous_hash'] != hash_block(blockchain[index - 1]):
            return False
    return True

def verify_transactions():
    return all([verify_transaction(tx)for tx in open_transactions])

waiting_for_input = True

while waiting_for_input:
    print('Please choose')
    print('1: Add a new transaction value')
    print('2: Mine a new block')
    print('3: Output the blockchain blocks')
    print('4: Output participants')
    print('5: Check transaction validity')
    print('h: Manipulate the chain')
    print('q: Quit')
    user_choice = get_user_choice()
    if user_choice == 1:
        tx_data = get_transaction_value()
        recipient, amount = tx_data #this unpacks the tuple, placing the first element into recipient, the second into amount, etc, etc
        if add_transaction(recipient, amount = amount): #add transaction amount to blockchain
            print('Added transaction')
        else:
            print('Transaction failed')
        print(open_transactions)
    elif user_choice == 2:
        if mine_block():
            open_transactions = []
    elif user_choice == 3:
        print_blockchain_elements()
    elif user_choice == 4:
        print(participants)
    elif user_choice == 5:
        if verify_transactions:
            print('All transactions are valid')
        else:
            print('There are invalid transactions')
    elif user_choice == 'h':
        if len(blockchain) >= 1:
            blockchain[0] = {
                'previous_hash': '',
                'index': 0,
                'transaction': [{'sender': 'Chris', 'recipient': 'Fart', 'amount': 100.0}]
            }
    elif user_choice == 'q':
        waiting_for_input = False
    else:
        print('You chose... poorly')
    if not verify_chain():
        print_blockchain_elements()
        print('Invalid chain')
        break
    print(get_balance('Eugene'))

else:
    print('User Left')

print('Done!')
