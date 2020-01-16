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



# The string data type is a string of text.
string = "This is a string."

word = " antidisestablishmentarianism "

name = "guido van rossum"

# Strings can be enclosed by single ('') or double quotes ("")
quote = 'John 11:35 says, "Jesus wept."'

# Different modifiers can be used on Strings

name.title() # "Guido Van Rossum"
name.upper() # "GUIDO VAN ROSSUM"
name.lower() # "guido van rossum"

# Did you notice the extra spaces in the word variable? Let's remove them.

word.rstrip() # removes space to the right
word.lstrip() # removes space to the left

# These can only work on one side at a time.
# If only there was a way to do both at the same time...

word.strip() # value: "antidisestablishmentarianism"
# this removes spades on both sides of a String
