import os
import time

file_path = "index.txt"

while True:
    with open(file_path, 'r') as file:
        content = file.read()

    os.system('cls')  # Clear the Windows Command Prompt

    print(content)

    time.sleep(3)
    
   
