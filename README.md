<h1>Encrypt and Decrypt</h1>
<p> </p>
<h2>Encrypt.py:</h2>
<p>Searches for .xlsx files in the documents folder, using Fernet (symmetric encryption) Cryptography module the script generate a random key for each file and encrypt it.</p>
<p>Then the script will send the file path and the key for decryption to your email and generate a txt file in the same folder as the decrypted files with custom text info and delete itself.</p>
<p> #Check IF chkfile.txt Exist IF True Exit ELSE Decrypt, To Avoid Decrypting the Files Again </p>
<h2>Decrypt.py:</h2>
<p>GUI script that decrypt each file with his special key.</p>
<p> </p>
<h2>install:</h2>
<p>pip install cryptography</p>
<p>pip install pysimplegui</p>
<p><strong> </strong></p>
<p> </p>
