# Password_Manager_with_python

## Overview
A secure CLI-based password manager to store and generate passwords for different websites.

---

## Features & Functionalities
- **Store website usernames and passwords**: Securely save credentials for different websites.
- **Generate strong passwords automatically**: Create strong, random passwords with customizable complexity.
- **View saved passwords**: Retrieve and display stored credentials.
- **Delete stored credentials**: Remove saved passwords when no longer needed.

---

## Technologies & Concepts Used
- **String Manipulation**: Use of `string.ascii_letters` and `random.choice()` for password generation.
- **Functions**: Parameterized functions with return values for modular and reusable code.
- **Data Structures**: Lists and dictionaries for storing and managing passwords.
- **File Handling**: Save and load passwords using JSON for persistent storage.
- **Error Handling**: Input validation for password strength and user input.

---

## Code Structure
- **`main.py`**: Manages the menu and user interaction.
- **`password_operations.py`**: Implements password logic (store, generate, delete).
- **`file_handler.py`**: Saves and loads passwords to/from a file.

---

## Challenges & Learnings
- **Understanding modules**: Using modules likes Random,String,OS was my first experience.
- **Understing reference counting and garbage collection.** : Understanding Reference Retention and Delayed Garbage Collection concept quite challenge to me
- **Implementing Trade off**: In file_handler.py, I have implement the trade-offs between using os.path.exists() and relying solely on try/except
---

## Future Improvements
- **Implement encryption for storing passwords**: Enhance security by encrypting passwords before saving them to a file.
- **Develop a GUI for better user experience**: Create a graphical user interface for easier interaction and improved usability.

---
##  **📂[Python Fundamentals Projects List →](https://github.com/DhawaDG/Python_fundaments/blob/main/README.md)** 
