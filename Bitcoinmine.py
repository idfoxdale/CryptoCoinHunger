# Coding for usual stuff Bitcoin mining, hmmm that's typical
# how hashing looks like, bbay steps!!
from hashlib import sha256
# display sha256 for a string 
# print(sha256("ABC".encode("ascii")).hexdigest())

# deffing a function for
def SHA256(text):
    return sha256(text.encode("ascii")).hexdigest()

def mine():
    pass


if __name__ == '__main__':
    transactions='''
    Ishann->Kumar->27,
    Jack->Jill->36
    '''

    new_hash = mine(transactions)

    print(new_hash)
