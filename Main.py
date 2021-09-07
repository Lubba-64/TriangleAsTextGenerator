from IsoscelesTriangle import IsoscelesTriangle as Isosceles
from RightTriangle import RightTriangle as Right

print('''
Welcome to Ascii triangle!\n
\n
I made this in class because I had nothing else to do\n
when I get more time to myself to do my own stuff,\n
more impressive stuff will come\n
\n
either way, here's the tool
''')

triangleType = input('Triangle Type: ').lower()
if (triangleType == 'right'):
    print(Right().ParamsAndTriangle())
if (triangleType == 'isosceles'):
    print(Isosceles().ParamsAndTriangle())