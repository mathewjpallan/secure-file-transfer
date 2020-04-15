# Secure file transfer
This is a sample code to allow one to zip & encrypt a csv using AES 256 for secure transfer. A random uuid is generated and used as the password. The password is then encrypted using a public key so that only the owner of the private key can read it and included in the transferred file.


# How to run
## Let us assume that B wants to received files from A.
- B has to generate a public private key pair by issuing the following commands. Please set a passphrase for the private key. Let us assume you have set the passphrase as `test` for this private key

```
   openssl genrsa -des3 -out private.pem 4096
   openssl rsa -in private.pem -outform PEM -pubout -out public.pem
```
- B secures the private key (private.pem) on a machine that is secure.
- B shares the public key (public.pem) with A over any channel (need not be secure channel)

### Actions by sender
- A clones this repo and cd to the cloned repo src folder and executes the following commands
```
    pip3 install -r requirements.txt
```
- A can now encrypt the files using this lib by issuing the following command
```
    python3 encrypt.py file.csv public.pem
    # file.csv is the csv file that needs to be transferred securely and public.pem points to the location of the public.pem that was received from B
```
- A can now transfer the file.csv.dat file (zip and encrypted) that was created by encrypt.py over a secure channel to B. The file is encrypted and a third party who gets access will not be able to decipher the file. However it is recommended that we use a secure channel for transmitting this file.

### Actions by Receiver
- B clones this repo and cd to the cloned repo src folder and executes the following commands
```
    pip3 install -r requirements.txt
```
- B can now decrypt the files using this lib by issuing the following command
```
    python3 decrypt.py file.csv.dat private.pem test
    # file.csv.dat is the (encrypted csv zip) file that was received securely from A, private.pem points to the location of the private.pem that was created by B and test is the passphrase for the private key
```
- B should now have the decrypted file that was securely transmitted from A and can use it for processing