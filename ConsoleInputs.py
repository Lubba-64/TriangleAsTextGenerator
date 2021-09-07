import string
import numbers
def InputBoolean(message:string='') -> bool:
    val = input(message).lower()
    return (val == 'true') and (not val == 'false')

def InputInt(message:string='') -> int:
    try:
        return int(input(message))
    except:
        return float("nan")