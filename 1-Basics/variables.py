# Variables and Simple Data Types

# Variables are like labels for data
# You can use just about anything for a variable name
favorite_food = "burritos"
magicNumber = 42
number_12 = 12

# There are some restrictions
10_numbers = 1234567890 # can't start with a number
*stars* = "*"           # can't use special characters
break = "Coffee time!"  # can't use reserved words


# STRINGS
# The string data type is a string of text.
string = "This is a string."

word = " antidisestablishmentarianism "

name = "guido van rossum"

# Strings can be enclosed by single ('') or double quotes ("")
quote = 'John 11:35 says, "Jesus wept."'

# Different modifiers can be used on strings

name.title() # "Guido Van Rossum"
name.upper() # "GUIDO VAN ROSSUM"
name.lower() # "guido van rossum"

# Did you notice the extra spaces in the word variable? Let's remove them.

word.rstrip() # removes space to the right
word.lstrip() # removes space to the left

# These can only work on one side at a time.
# If only there was a way to do both at the same time...

word.strip() # value: "antidisestablishmentarianism"
# this removes spaces on both sides of a string


# NUMBERS
# There are two types of numbers we'll get into here, integer and float

# Integers are whole numbers
# You can add [+], subtract [-], multiply [*], or divide [/] with them

newNumber = magicNumber + number_12 # 42+12 = 54
newNumber = magicNumber - number_12 # 42-12 = 30
newNumber = magicNumber * number_12 # 42*12 = 504
newNumber = magicNumber / number_12 # 42/12 = 3.5 ... That's not a whole number

# Floats are numbers with decimal points
# they work the same way as integers, but they are more precise

# When working with integers and floats at the same time,
# python will default to floats

penny = 0.01
nickel = 0.05
dime = 0.1
quarter = 0.25
dollar = 1

change = dollar + quarter # 1 + 0.25 = 1.25

# sometimes they get *too* precise
# open a terminal and input "0.2 + 0.1"

# Here's what happens...
# >>> 0.2+0.1
# 0.30000000000000004

# Computers are weird, man.
