# Variable in Python

Python will automatically determine which data type it will store data as. 
You need to be aware of data types in order to convert data from one type to another.


## Data type Meaning Examples
Integer A whole number 1, 5, 17, 0
Float Floating point number A decimal/real number 5.27, 2.0, 3.14
Boolean True or False True, False
Char A character - one letter or symbol, in Python this is a string) 'H', '7', 'g', '@'
String A list of characters 'Hello', 'Some text'
List A list (similar to an array) ['Earth', 'Fire', 'Water']


## Type Casting
int(string)    #convert string to integer
int(float)     #convert float to integer
float(integer) #convert integer to float
float(string)  #convert string to float
str(integer)   #convert integer to string
str(float)     #convert float to string
type(value)    #find the type of the value given

### Notes
Python can use both ‘ and ” for strings. So "hello" and 'hello' are both exactly the same.

You can find out what data type a value or a variable is storing by using type(value).

Python doesn’t have a different data type for strings and characters. It treats a character as a string of length one.
