import os

def new_function(
    number_1,
    number_2
):
    return number_1 + number_2

def bad_function(
    input
):
   os.system(input)
   return

def bad_output_function(
    input
):
    try:
        return input + 1
    except Exception as e:
        print(e)