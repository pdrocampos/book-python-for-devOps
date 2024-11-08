'''
The string sequence type is a collection of ordered characters 
surrounded by quota‐ tion marks. As of Python 3, strings default 
to using UTF-8 encoding.
'''

print("some new string!")
print('or with single quotes')

# The string constructor can be used to make strings from other objects:

my_list = list()
print(str(my_list))

# You can create multiline strings by using triple quotes around the content:

multi_line = """ this is a multi-line string,
wich includes linebreaks.
"""
print(multi_line)

# Python strings have a strip method just for this case. 
# It returns a string with the whitespace removed from the beginning and end

input = "  I want more  "
print(input)
print(input.strip())
print(input.rstrip())
print(input.lstrip())

'''
On the other hand, if you want to add padding to a string, you can use the 
ljust or rjust methods. Either one pads with whitespace by default, or takes
a character argument
'''

output = 'Barry'
print(output.ljust(10))
print(output.rjust(10, '*'))

'''
O método split divide uma string em uma lista de strings, usando o espaço 
em branco como separador por padrão. Um argumento opcional pode definir 
outro caractere para a divisão:
'''

text = 'Mary had a little lamb'
print(text.split())
url = "gt.motomomo.io/v2/api/asset/143"
print("url = " , url.split('/'))

'''
You can easily create a new string from a sequence of strings and join 
them into a single string. This method inserts a string as a separator 
between a list of other strings:
'''

items = url.split('/')
print("items = ", items)
items = " and ".join(items)
print(items)

'''
Changing the case of text is a common occurrence, whether it is making 
the case uni‐ form for comparison or changing in preparation for user consumption.
 Python strings have several methods to make this an easy process:
'''

name = "pedro henrique"
print(name.capitalize())
print(name.upper())
print(name.title())
print(name.swapcase())
print(name.lower())

'''
Python also provides methods to understand a string’s content. Whether it’s checking
the case of the text, or seeing if it represents a number, there are quite a few 
built-in methods for interrogation. Here are just a few of the most commonly used 
methods:
'''

name = "Sophia Campos"
print(name.startswith('S'))
print(name.startswith('Soph'))
print(name.endswith('os'))
print(name.isalnum())
print(name.isalpha())
print(name.isnumeric())
print(name.istitle())
print(name.islower())
print(name.isupper())

'''
The older form of string formatting in Python comes from the C language printf function. 
You can use the modulus operator, %, to insert formatted values into a string. 
This technique applies to the form string % values, where values can be a single nontuple
 or a tuple of multiple values. The string itself must have a conversion specifier for each 
 value. The conversion specifier, at a minimum, starts with a % and is followed by a 
 character representing the type of value inserted:
'''

print("%s + %s = %s" % (1,2,"Three"))

'''
Additional format arguments include the conversion specifier. For example, you can control 
the number of places a float, %f, prints:
'''

print("%.3f" % 1.234567)

'''
Python 3 introduced a new way of formatting strings using the string method format. 
This way of formatting has been backported to Python 2 as well. This specification uses 
curly brackets in the string to indicate replacement fields rather than the modulus-based 
conversion specifiers of the old-style formatting. The insert values become arguments to 
the string format method. The order of the arguments deter‐ mines their placement order 
in the target string:
'''

print('{} come before {}'.format('first' , 'second'))

'''
You can specify index numbers in the brackets to insert values in an order different 
than that in the argument list. You can also repeat a value by specifying the same
'''

print('{1} come after {0}, but {1} '
      'comes before {2}'.format('first', 
      'second', 'third'))

'''
An even more powerful feature is that the insert values can be specified by name:
'''

print('{country} is an island. {country}' 
      ' is off of the coast of {continent}'
      ' in the {ocean}'.format(
        ocean='India Ocean', continent='Africa',
        country ='Madagascar'))

'''
Here a dict works to supply the key values for name-based replacement fields:
'''

values = {'first': 'Bill', 'last': 'Bailey'}
print('Won´t you come home {first} {last}?'.format(**values))

'''
You can also specify format specification arguments. Here they add left and right 
pad‐ ding using > and <. In the second example, we specify a character to use in the padding:
'''

text = "|{0:>22}||{0:<22}|"
print(text.format('0','0'))
text = "|{0:<>22}||{1:><22}|"
print(text.format('first','second'))

'''
Python f-strings use the same formatting language as the format method, but offer a more 
straightforward and intuitive mechanism for using them. f-strings are prepen‐ ded with either 
f or F before the first quotation mark. Like the format string previ‐ ously described, f-strings 
use curly braces to demarcate replacement fields. In an f- string, however, the content of the 
replacement field is an expression. This approach means it can refer to variables defined in the 
current scope or involve calculations:
'''

a = 1
b = 2
print(f'a is {a}, b is {b}. Adding them results in {a + b}')

'''
As in format strings, format specifications in f-strings happen within the curly brack‐ ets 
after the value expression and start with a ::
'''

count = 43
print(f'|{count:5d}')
count = 21433
print(f'|{count:5d}')

'''
The value expression can contain nested expressions, referencing variables, and expressions 
in the construction of the parent expression:
'''
padding = 10
print(f'|{count:{padding}d}')

'''
Template strings are designed to offer a straightforward string substitution mecha‐ nism. 
These built-in methods work for tasks such as internationalization, where sim‐ ple word 
substitutions are necessary. They use $ as a substitution character, with optional curly 
braces surrounding them. The characters directly following the $ iden‐ tify the value to 
be inserted. When the substitute method of the string template exe‐ cutes, these names are
used to assign values.
Built-in types and functions are available whenever you run Python code, but to access the
 broader world of functionality available in the Python ecosystem, you need to use the import
 statement. This approach lets you add functionality from the Python Standard Library or 
 third-party services into your environment. You can selectively import parts of a package by
   using the from keyword:
'''

from string import Template
greeting = Template("$hello Mark Anthony")
print(greeting.substitute(hello='Bonjour'))







