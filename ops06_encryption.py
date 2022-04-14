#!/bin/python3
# Script Name: ops06_encryption.py
# Author: Gina Hobbs
# Date of last revision: 14 April 2022
# Description of purpose: encrypt and decrypt files and messages
# Declaration of variables: file_name, message, e_message, d_message, ecrypted_data,
# decrypted_data, key, f, option, decrypted, encrypted, folder
# Declaration of functions (if used): write_key(), load_key(), encrypt_file(), 
# decrypt_file(), encrypt_message(), decrypt_message(), menu(), encrypt_folder(),
# decrypt_folder(), change_wallpaper()

# Import libraries
import ctypes
from cryptography.fernet import Fernet
import os
from tkinter import messagebox

### Functions for key processing

# Write a new fernet key to a file
def write_key():
    # Generate a key and save it to a file
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

# Load the key from the current file named key.key
def load_key():
    return open("key.key", "rb").read()

# Prompt the user to input a 1 or 2 for encrypting a file or a message
def menu():
    print("1: Encrypt a file")
    print("2: Decrypt a file")
    print("3: Encrypt a message")
    print("4: Decrypt a message")
    print("5: Encrypt a folder.")
    print("6: Decrypt a folder.")
    print("7: Ransomware Simulation - Popup")
    print("8: Ransomware Simulation - Change Wallpaper")
    option = input("Please enter the value for what you would like to do.\n")
    return option

# Run menu
option = menu()

def change_wallpaper():
    ctypes.windll.user32.SystemParametersInfoW(20, 0, "c:\Users\fhopkins\ransomware.jpg" , 0)

def encrypt_folder(folder):
    for root, dirs, files in os.walk(folder, topdown=False):
        for name in files:
            file_name = (os.path.join(root, name))
            encrypt_file(file_name)
        for name in dirs:
            file_name = (os.path.join(root, name))
            encrypt_file(file_name)

def decrypt_folder(folder):
    for root, dirs, files in os.walk(folder, topdown=False):
        for name in files:
            file_name = (os.path.join(root, name))
            decrypt_file(file_name)
        for name in dirs:
            file_name = (os.path.join(root, name))
            decrypt_file(file_name)

# Define the encrypt file function
def encrypt_file(file_name):
    key = load_key()
    f = Fernet(key)
    with open(file_name, "rb") as file:
        file_data = file.read()
    encrypted_data = f.encrypt(file_data)
    with open(file_name, "wb") as file:
        file.write(encrypted_data)
    print(key)

# Define the decrypt file function
def decrypt_file(file_name):
    key = load_key()
    f = Fernet(key)
    with open(file_name, "rb") as file:
        encrypted_data = file.read()
    print(encrypted_data)
    decrypted_data = f.decrypt(encrypted_data)
    with open(file_name, "wb") as file:
        file.write(decrypted_data)
    print(decrypted_data)
    
# Define the encrypt_message function
def encrypt_message(message):
    key = load_key()
    e_message = message.encode()
    print("Plaintext is " + str(e_message.decode('utf-8')))
    f = Fernet(key)
    encrypted = f.encrypt(e_message)
    print("Ciphertext is " + str(encrypted.decode('utf-8')))

# Define the decrypt_message function
def decrypt_message(message):
    key = load_key()
    e_message = message.encode('utf-8')
    f = Fernet(key)
    decrypted = f.decrypt(e_message)
    print("Plaintext is " + decrypted.decode('utf-8'))

# Capture the message or file name from the user.
def menu():
    if option == '1':
        file_name = input("Please enter the file name you wish to encrypt.\n")
        write_key()
        encrypt_file(file_name)
    elif option == '2':
        file_name = input("Please enter the name you wish to decrypt.\n")
        decrypt_file(file_name)
    elif option == '3':
        message = input("Please enter the message you wish to encrypt.\n")
        write_key()
        encrypt_message(message)
    elif option == '4':
        message = input("Please enter the message you wish to decrypt.\n")
        decrypt_message(message)
    elif option == '5':
        folder = input("Please enter the folder you wish to decrypt.\n")
        write_key()
        encrypt_folder(folder)
    elif option == '6':
        folder = input("Please enter the folder you wish to decrypt.\n")
        decrypt_folder(folder)
    elif option == '7':
        messagebox.showinfo("Ransomware","Your data has been encrypted.")
    elif option == '8':
        change_wallpaper()
    else:
        print("Please enter a valid menu option, a numeral between 1 and 4.\n")
        menu()

menu()