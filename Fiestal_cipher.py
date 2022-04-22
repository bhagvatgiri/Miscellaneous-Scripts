

def feistel_block(L_inp, R_inp, k):
    for i in range(16):
        f1 = F(R_inp, k[i])
        f2 = xor(L_inp, f1)
        L_inp = R_inp
        R_inp = f2

    L_out = R_inp

    R_out = L_inp

    return L_out, R_out


def xor(byteseq1, byteseq2):
    # Python already provides the ^ operator to do xor on interger values
    # but first we need to break our input byte sequences into bye size integers
    l1 = [b for b in byteseq1]
    l2 = [b for b in byteseq2]
    l1attachl2 = zip(l1, l2)
    # zip(l1,l2) is actually a list as [(b'\xaa',b'\xcc), (b'\x33', b'\x55')]

    l1xorl2 = [bytes([elem1 ^ elem2]) for elem1, elem2 in l1attachl2]
    result = b''.join(l1xorl2)

    return result


import hmac
import hashlib
import random


def F(byteseq, k):
    # we use the hmac hash (don't worry about the meaning for now)
    h = hmac.new(k, byteseq, hashlib.sha1)
    # return the first 8 bytes of the hash value
    return h.digest()[:8]


def gen_keylist(keylenbytes, numkeys, seed):
    # We need to generate numkeys keys each being keylen bytes long
    keylist = []
    random.seed(seed)

    # Use the random.randint(min,max) function to generate individual
    # random integers in range [min, max]. Generate a list of numkeys
    # random byte sequences each of them keylenbytes bytes long to be used as
    # keys for numkeys stages of the feistel encoder. To make sure we have control over
    # the generated random numbers meaning that the same sequence is
    # generated in different runs of our program,

    # keylist = [numkeys elements of 'bytes' type and keylenbytes bytes long each]
    keylist = []
    for i in range(numkeys):
        bytelist = b''.join([bytes([random.randint(0, 255)]) for x in range(keylenbytes)])
        keylist.append(bytelist)

    return keylist


# Now the actual encoder
def feistel_enc(inputbyteseq, num_rounds, seed):
    # This is the function that accepts one bloc of plaintext
    # and applies all rounds of the feistel cipher and returns the

    # cipher text block.
    # Inputs:
    # inputblock: byte sequence representing input block
    # num_rounds: integer representing number of rounds in the feistel
    # seed: integer to set the random number generator to defined state
    # Output:
    # cipherblock: byte sequence

    # first generate the required keys
    keylist = gen_keylist(8, num_rounds, seed)
    while len(inputbyteseq) % 16 != 0:
        inputbyteseq += b'\x20'
    n = int(len(inputbyteseq) // 2)
    L1 = inputbyteseq[0:n]
    R1 = inputbyteseq[n::]
    LC_out, RC_out = feistel_block(L1, R1, keylist)
    ciphertext = LC_out + RC_out

    # implement num_rounds of calling the block function
    # print(n)
    # print(keylist)
    print(ciphertext)
    return ciphertext


y = feistel_enc(b'howyoudoing?', 16, 800)


def feistel_dec(inputbyteseq, num_rounds, seed):
    # Make sure you use the keys in reverse order during decryption
    keylist = gen_keylist(8, num_rounds, seed)
    keylist1 = [ele for ele in reversed(keylist)]
    n = int(len(inputbyteseq) // 2)
    L1 = inputbyteseq[0:n]
    R1 = inputbyteseq[n::]
    LP_out, RP_out = feistel_block(L1, R1, keylist1)
    plaintextblock = LP_out + RP_out
    print(plaintextblock)

    return plaintextblock


#y = feistel_dec(b'}\xd9\x93-G\x8e\xaa5\x95\x84\n\xb7q\xc4>\xb6', 16, 50)

