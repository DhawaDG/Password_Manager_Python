# add_password,view_password,delete_password,generate_password
import random
import string
def add_password(passwords):
    
    special_chars=string.punctuation #"£$%^&*"

    user_website=input("Please Enter Your Websites Name.").strip() #removes leading and trailing whitespace from a string

    while True: #repeat code multiple times until condition True
        
        user_name=input("Please Enter your User Name").strip()
        if user_name.replace(" ","").isalpha():  #replace() replaces all spaces in the string with empty strings("") effectively removing all spaces from the string
            break #exits loop                    #.isalpha() checks letters in strings if yes True if not False 
        else:
            print("Invalid entry. User Name must be aplhabetic order")

        
    

    while  True:
        user_password= input("Enter your password:").strip()

        if len(user_password)<8:
            print("password must be at least 8 characters long.try again")
        
        if not any(char in special_chars for char in user_password): #any() checks atleast 1 conditions True
            print("Password must contain atleast one special character.try again")

        if not any(char.isdigit() for char in user_password):
            print("Password must contain aleast one digit.try again")
            continue    #skips the current iterations and moves to the next

        print("password is valid.")
        break

    password={
        "website":user_website,
        "username":user_name,
        "password":user_password
        }

    passwords.append(password)  #append() add values to passwords dict

    print("your website, username and password are successfully saved")

def view_password(passwords):
    if not passwords:
        print("No Records available")
        return #exit functions
    
    print("\n Password List")
    for users in passwords:
        print(f"WEBSITES:{users['website']} | USERNAME:{users['username']} | PASSWORD:{users['password']}")

def delete_password(passwords):
    view_password(passwords)
    print("\n Enter the name of user you want to remove password.")
    try:
        input_username=str(input("enter the Username"))
        for queryname in passwords:
            if queryname['username']==input_username:
                passwords.remove(queryname) #remove a list matching username
                #using reference counting and garbage collection.
                print(f"Removed password {queryname['password']} and username {queryname['username']} ")
                return
            else:
                print("Please enter matching username")
    except ValueError:
        print("Please enter alphabetic order user name")



def generate_password(passwords):
    
    lowercase_letters = string.ascii_lowercase  # a-z
    uppercase_letters = string.ascii_uppercase  # A-Z
    digits = string.digits  # 0-9
    special_chars = string.punctuation  # special characters: !"#$%&'()*...etc

    # combine all character sets
    all_chars = lowercase_letters + uppercase_letters + digits + special_chars

    # define password length (e.g., 12 characters)
    password_length = 12

    while True:
        # generate a random password
        generated_password = ''.join(random.choice(all_chars) for _ in range(password_length))

        # ensure the password meets requirements (e.g., at least one of each character type)
        if (any(char in lowercase_letters for char in generated_password) and
            any(char in uppercase_letters for char in generated_password) and
            any(char in digits for char in generated_password) and
            any(char in special_chars for char in generated_password)):
            break  

    
    user_website=input("Please Enter Your Websites Name.").strip()
    while True:
        
        user_name=input("Please Enter your User Name").strip()
        if user_name.replace(" ","").isalpha():
            break
        else:
            print("Invalid entry. User Name must be aplhabetic order")
    
    
    passwords.append({"website": user_website, "username": user_name, "password": generated_password})
    # display generated password to user
    print(f"  Password generated is: {generated_password}")
    



