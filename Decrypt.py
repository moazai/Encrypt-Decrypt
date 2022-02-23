import PySimpleGUI as sg
from cryptography.fernet import Fernet

# Window Design
sg.theme("BlueMono")
layout = [sg.T("")], [[sg.Text("Insert Decrypt Key: "), sg.InputText()],
                      [sg.T("")], [sg.Text("Choose a file: "), sg.Input(),
                                   sg.FileBrowse(key="-IN-")], [sg.Button("Please Decrypt My File!!")]]

# Building GUI Window
window = sg.Window('Decrypt My Files', layout, size=(500, 160))
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == "Please Decrypt My File!!":

        x = (values["-IN-"])
    try:
        # Read the KEY
        key = (values[0])
        # Create a Fernet Object Using the KEY
        fernet = Fernet(key)

        # Read the File to Decrypt
        with open(x, 'rb') as f:
            file = f.read()

        # Decrypt the File
        decrypt_file = fernet.decrypt(file)

        # Open File and Write the Decryption Data
        with open(x, 'wb') as decrypted_file:
            decrypted_file.write(decrypt_file)
        print(x, 'File Decrypted')
    except:
        print('the KEY does not match the File', 'Error')
