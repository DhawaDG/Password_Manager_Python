from password_operations import add_password,view_password,delete_password,generate_password
from file_handler import save_passwords_to_file, load_passwords_to_file

#load_passwords_to_filr() returns a value which is assigned to passwords variable.
passwords=load_passwords_to_file()

#creating a functions to display menu 
def show_menu():
    print("\n Passwords Manager:--  ")
    print("1. Enter 1 to add password:--  ")
    print("2. Enter 2 to View passwords:-  ")
    print("3. Enter 3 to Delete Password:--  ")
    print("4. Enter 4 to generate Passwords:--  ")

while True:
    show_menu()
    choice=input("Enter your choice:--  ")

    if choice == "1":
        add_password(passwords)
    elif choice == "2":
        view_password(passwords)
    elif choice == "3":
        delete_password(passwords)
    elif choice == "4":
        generate_password(passwords)
    elif choice == "5":
        save_passwords_to_file(passwords)
        print("Password is saved successfully.")
    else:
        print("\n Invalid choice")

