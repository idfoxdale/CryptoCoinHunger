# Coding for usual stuff Bitcoin mining, hmmm that's typical
# how hashing looks like, bbay steps!!
from hashlib import sha256
# display sha256 for a string 
# print(sha256("ABC".encode("ascii")).hexdigest())

# deffing a function for
def SHA256(text):
    return sha256(text.encode("ascii")).hexdigest()

#guess iterating block
def mine(block_number, transactions, previous_hash, prefix_zeros):
    #hardcoding nonce initially 1
    nonce=1
    #defing the entire text block as string
    text = str(block_number) + transactions + previous_hash + str(nonce)
    new_hash = SHA256(text)
    return new_hash


if __name__ == '__main__':
    transactions='''
    Ishann->Kumar->27,
    Jack->Jill->36
    '''

    difficulty = 4

    new_hash = mine(5, transactions, '0000000xa036944e29568d0cff17edbe038f81208fecf9a66be9a2b8321c6ec7', difficulty )

    print(new_hash)
