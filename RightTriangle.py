import string
from TextTriangle import TextTriangle as Triangle
from ConsoleInputs import InputBoolean
from ConsoleInputs import InputInt
from StringFunctions import GetStringOfLengthOfChar
class RightTriangle(Triangle):
    def GetParamsFromConsole(self):
        size = InputInt('size of triangle: ')
        if (size%2==0):
            size+=1
        innerChar=input('inner character: ')
        outerChar=input('outer character: ')
        flipX = InputBoolean('Flip Horizantally: ')
        flipY = InputBoolean('Flip Vertically: ')
        return (size,innerChar,outerChar,flipY,flipX)
    def GetTriangle(self,size:int=0,flipX:bool=False,flipY:bool=False,outerChar:string='',innerChar:string='&') -> string:
        returned = ''
        triangleRange = range(1,size) if not flipY else range(size-1,0,-1)
        for i in triangleRange:
            inner = GetStringOfLengthOfChar(i,innerChar)
            outer = GetStringOfLengthOfChar(size-i-1,outerChar)
            first = inner if not flipX else outer
            second = inner if flipX else outer
            returned += f'{first}{second}\n'
        return returned
    def ParamsAndTriangle(self) -> string:
        params = self.GetParamsFromConsole()
        return self.GetTriangle(params[0],params[4],params[3],params[2],params[1])