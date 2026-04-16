s = "Hello,World"
s1 = " Hello,World "
print("String:",s)

# slicing string
print("Slicing string:")
print(s[:4])
print(s[1:4])
print(s[-4:-1])
print(s[-4:])
print(s[-1])

# modification in string
print("Uppercase:",s.upper())
print("Lowercase:",s.lower())
print("Remove whitespaces:",s1.strip())
print("Spilting strings:",s1.split(","))
print("replace:",s1.replace('o','p'))
print(s1)

# Concadinating Strings
print("Concadination:",s+s1)   # there is no space between two strings

# format string
price = 39
print(f"Format String is : This Book is rupees {price:.2f}")

# casefold
user_name = input("Enter username:")
if user_name.casefold() == "admin":
    print("Login successful!!")

