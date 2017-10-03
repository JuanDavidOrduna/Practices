
# print("Hello World")
import sys
print(sys.executable)
print(sys.version)

class Employee:
    """A sample Employee class"""

    def __init__(self, first, last):
        self.first = first
        self.last = last

    def test_method(self):
        pass

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{}.{}'.format(self.first, self.last)


emp_1 = Employee('John', 'Smith')

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

TextVariable =  """ this is
some text
several lines"""

print(TextVariable)


variable = input('Type something in: ')
print(variable)



print("Example Heading\n\nFollowed by a line\nor two of text\n \
... \tName\n\tRace\n\tGender\nDon\'t forget to escape \'\\\'."
)
