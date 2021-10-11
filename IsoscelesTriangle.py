import string
from StringFunctions import GetStringOfLengthOfChar
from ConsoleInputs import InputBoolean
from ConsoleInputs import InputInt
from TextTriangle import TextTriangle as Triangle
class IsoscelesTriangle(Triangle):
    def GetParamsFromConsole(self):
        size = InputInt('size of triangle: ')
        if (size%2==0):
            size+=1
        innerChar = input('inner character: ')
        outerChar = input('outer character: ')
        flip = InputBoolean('Flip Vertically: ')
        return (size,innerChar,outerChar,flip)
    def GetTriangle(self,size:int=0,flip:bool=False,outerChar:string='',innerChar:string='&') -> string:
        returned = ''
        triangleRange = range(0,size) if not flip else range(size,0,-1)
        for i in triangleRange:
            blankspace = GetStringOfLengthOfChar(size-1-i,outerChar)
            returned += f'{blankspace}{GetStringOfLengthOfChar(i*2+1,innerChar)}{blankspace}\n'
        return returned
    def ParamsAndTriangle(self) -> string:
        params = self.GetParamsFromConsole()
        return self.GetTriangle(params[0],params[3],params[2],params[1])