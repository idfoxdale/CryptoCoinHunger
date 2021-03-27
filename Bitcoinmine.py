# Coding for usual stuff Bitcoin mining, hmmm that's typical
# how hashing looks like, bbay steps!!
from hashlib import sha256
# display sha256 for a string 
# print(sha256("ABC".encode("ascii")).hexdigest())

#at later stage defining a max number for nonce iteration based on compute powr of the system
# so here we go
MAX_NUMBER = 100000

# deffing a function for
def SHA256(text):
    return sha256(text.encode("ascii")).hexdigest()

#guess iterating block
def mine(block_number, transactions, previous_hash, prefix_zeros):
    #hardcoding nonce initially 1 the 2 and then 3 and then i fed up and intro a for loop
    #nonce=3
    prefix_str = '0' *prefix_zeros

    for nonce in range(MAX_NUMBER):
    #defing the entire text block as string
     text = str(block_number) + transactions + previous_hash + str(nonce)
     new_hash = SHA256(text)
     if new_hash.startswith(prefix_str):
         print(f"HellYa!! mined the crypto block with Nonce Value:{nonce}  (nonce here is means iteration count)")

         return new_hash

    raise BaseException(f"Couldn't find correct has after trying {MAX_NUMBER} times")


if __name__ == '__main__':
    transactions='''
    Ishann->Kumar->27,
    Jack->Jill->36
    '''

    difficulty = 4 # changing this to higher number will take more time for mining as computation increases

    new_hash = mine(5, transactions, '0000000xa036944e29568d0cff17edbe038f81208fecf9a66be9a2b8321c6ec7', difficulty )

    print(new_hash)
