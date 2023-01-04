import os
COMMAND_QUERY = "SELECT * FROM {input}"

def new_function(
    number_1,
    number_2
):
    return number_1 + number_2

def bad_function(
    path
    name
):
   os.mkdir(path, name)

def bad_output_function(
    input
):
    try:
        return input + 1
    except Exception as e:
        print(e)
    finally:
