class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def where_is(point):
    match point:
        case Point(x=0, y=0):
            print("Original point")
        case Point(x=0, y=y):
            print(f"Y=f{y}")
        case Point(x=x, y=0):
            print(f"X=f{x}")
        case Point():
            print("where")
        case _ :
            print("Not a Point")
point1 = Point(0,y=vars)
point2 = Point
where_is(point1)
where_is(point2)

#Keyword arguments
def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")
# 1 positional argument
parrot(1000)         

 # 1 keyword argument
parrot(voltage=1000)                                 

# 2 keyword arguments
parrot(voltage=1000000, action='VOOOOOM')             

parrot(action='VOOOOOM', voltage=1000000)            

s1 = {1,2,3,4,5,6}
s2 = {6,7,8,9}
print(s1&s2)
print('i am learning Python'.capitalize())