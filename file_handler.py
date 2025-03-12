import json
import os
#global variable
FILE_PATH="data/passwords.json"

def save_passwords_to_file(passwords):
    try:
        with open(FILE_PATH,"w") as file: #open file in write mode
            json.dump(passwords,file) #convert passwords object to a JSON string
        print("Password saved to file.")
    except Exception as e:
        print(f"Error sabing passwords:{e}") #catch-all approach

def load_passwords_to_file():
    try:
        if not os.path.exists(FILE_PATH): #check file if exits and void error if file doesnt exist
            return[] #if not return empty list
        with open(FILE_PATH,"r") as file: #open file in read mode
            return json.load(file) #return loaded data
        
    except(FileNotFoundError,json.JSONDecodeError):
        return[]
    

    """
    why you used os.path.exists() in addition to try and except in the load_passwords_to_file() function?
    -- Both approaches are valid, and the choice depends on the specific use case and coding style preferences.
       In this case, I chose to use os.path.exists() to make the code more explicit, but I could also have relied
       solely on try/except to handle all errors.  
    """
    