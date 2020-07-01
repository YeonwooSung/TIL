class Circle:
    def __init__(self, radius):
        super().__init__()
        self.radius = radius
    def getRadius(self):
        return self.radius

circle = Circle(5)

# 1. isinstance()
#
# Return True if the object argument is an instance of the classinfo argument, or of a (direct, indirect or virtual) subclass thereof.

if isinstance(True, bool):
    print('True is a bool')
if isinstance(1, int):
    print('1 is an integer')

if isinstance(3, bool):
    print('3 is bool type instance')
else:
    print('3 is not a bool type')

if isinstance(1, float):
    print('1 is a float')
else:
    print('1 is not a float type')

if isinstance(1.0, float):
    print('1.0 is a float type')

# we could apply this to the instance
if isinstance(circle, Circle):
    print('circle is a Circle type instance')



# 2. hasattr()
#
# Returns True if an object contains specified attribute, and False otherwise.

if hasattr(circle, 'radius'):
    print('circle has "radius"')

if hasattr(circle, 'getRadius'):
    print('circle has an attribute called "getRadius"')



# 3. exec()
#
# Function for dynamic query building

statement = '''a = 10; print(a + 5)'''
exec(statement)
