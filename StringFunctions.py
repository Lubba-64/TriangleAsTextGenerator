import string
def GetStringOfLengthOfChar(len:int=0,char:string=' ') -> string:
    returned=''
    for i in range(0,len):
        returned += char
    return returned