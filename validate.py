import math
def validate_input(value):
    while True:
        if value <= 0:
            value = float(input('enter a valid number: '))
        else:
            break
    return value

def calc(pOpp, pAdj):
    # work out the hyp
    pHyp = math.sqrt(pOpp**2 + pAdj**2)
    return pHyp

