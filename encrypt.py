import uuid
from utils import *
import sys 

# Generate a uuid that can be used as a password.
password = uuid.uuid4().hex

# The file that needs to be transferred
filename = sys.argv[1]
publicKeyPath = sys.argv[2]

#This function is invoke the zip the file
compressFile(filename)

# Read the zip file (fIn), Create a new file for the encrypted output (fOut)
# Encrypt the password that is generated using the public key and write it 
# as the first line in the output file.The decrypt will use the private key to 
# extract the password
# Encrypt the zip file with AES256 and append it to the fOut
with open(filename + '.zip', 'rb') as fIn:
    with open(filename + '.dat', 'wb') as fOut:
        cipherText = encryptUsingPublicKey(password, publicKeyPath) + '\n'
        fOut.write(cipherText.encode('UTF-8'))
        encryptFileWithAESKey(fIn, fOut, password)
remove(filename + '.zip')