from helper import validate_and_execute

# build in modules
import os


user_input = ""

while user_input != "exit":
    user_input = input("Please write days and convention type in format dd:type\n")
    if user_input != "exit":
        input_to_list = user_input.split(":")
        #check that exactly 2 values passed in the list
        if len(input_to_list) == 2:
            list_to_dictionary = {"days": input_to_list[0], "type": input_to_list[1]}
            validate_and_execute(list_to_dictionary)

