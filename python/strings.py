
# Check string

txt = "This is a string text"
if ("string" in txt):
    print("Yes, string is present")

if ("expensive" not in txt):
    print("expensive is not present")

# Slicing strings

## Get characters from positoin 2 to position 5
a = "Hello world"
print(a[2:5])

## Slice to the end

print(a[2:])

## Slice with negative index

print(a[-5:-2])

# Modify Strings
## upper case
print(a.upper())
## lower case
print(a.lower())
## Remove whitespace
b = " Hello World! "
print(b.strip())

## Replace
print(a.replace("H", "J"))

## Split
print(a.split(" "))

a = "hello"
b = "world"
c = a + " " + b
print(c)

age = 36
print("I am " + str(age))
print(f"I am {age}")


## Capitalize: Converts first character to uppercase
txt= "hello"
print(txt.capitalize())

## casefold: converts string into lower case
txt = "HELLO"
print(txt.casefold())

## center: Returns a centered string, optionally filled with a character
print(txt.center(30,"#"))

print(txt.count("L"))
print(txt.encode())

if (txt.endswith("O")):
    print("Yes, ends with O")

print(txt.find("LL"))
print(txt.index("LL"))

## Join iterable

a = ("John", "Peter", "Lisa")
print(" ".join(a))

txt = "banana"

x = txt.rjust(20)

print(x, "is my favorite fruit.")

