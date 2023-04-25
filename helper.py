import logging

logger = logging.getLogger("HELPER")
def day_to_units (num_of_days, conversion_type):
    if conversion_type == "hours":
        return num_of_days * 24
    elif conversion_type == "minutes":
        return num_of_days * 24 * 60
    else:
        logger.error("type conversion error")
        return f" {conversion_type} is not a type we can convert days to"


def validate_and_execute(list_to_dictionary):
    try:
        user_input_number = int(list_to_dictionary["days"])
        user_input_type = list_to_dictionary["type"]
        if user_input_number > 0:
            calculated_value = day_to_units(user_input_number, user_input_type)
            if isinstance(calculated_value, int):
                print(f"{user_input_number} days are {calculated_value} {user_input_type}")
            else:
                print(calculated_value)
        elif user_input_number == 0:
            print("Number of days should be possitive")
    except ValueError:
        logger.error("Validation of input error")
        print("Validation of input error")

