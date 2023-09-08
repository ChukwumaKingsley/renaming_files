import inputting, rename
from pyperclip import copy

def change_name():
    while True:
        change_type = input("Input change type: a for space-underscore, b for underscore-space: ")
        if (change_type == "a") or (change_type == "b"):
            break
        else:
            print("Invalid input!!!")

    name = inputting.get_input_name()
    if change_type == "a":
        new_name = rename.space_to_underscore(name)
    else:
        new_name = rename.underscore_to_space(name)
    
    copy(new_name)
    print(f"The new name is \"{new_name}\"")

def change_names():
    while True:
        change_name()
        cont = input("Do you want to change another (y/n): ")
        if cont == "n":
            break

    
change_names()
    