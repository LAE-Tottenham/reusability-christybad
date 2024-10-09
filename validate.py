import math
def validate_input(value):
    while True:
        if value <= 0:
            value = float(input('enter a valid number: '))
        else:
            break
    return value
