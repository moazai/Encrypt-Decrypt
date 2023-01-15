Encrypt.py:
Searches for .xlsx files in the documents folder, using Fernet (symmetric encryption) Cryptography module the script generate a random key for each file and encrypt it.
Then the script will send the file path and the key for decryption to your email and generate a txt file in the same folder as the encrypted files with custom text info and delete itself.
#Check IF chkfile.txt Exist IF True Exit ELSE Decrypt, To Avoid Encrypting the Files Again



Decrypt.py:
GUI script that decrypt each file with his special key.


install:

pip install cryptography

pip install pysimplegui
