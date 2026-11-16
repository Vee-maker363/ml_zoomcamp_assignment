# Module 1: Boolean Values & Functions - Solutions
# Only open this after you've tried every exercise yourself.


# %%
# Exercise 1
# bool is its own type. True behaves like 1 and False like 0 in math,
# and str(True) is the text 'True'.

print(type(True))      # <class 'bool'>
print(type("True"))    # <class 'str'>: quotes make it text
print(True + True)     # 2
print(True * 10)       # 10
print(int(False))      # 0
print(float(True))     # 1.0
print(str(True) + "!") # True!


# %%
# Exercise 2
# Rule: zero numbers (0, 0.0), empty things ("", [], {}, ()) and None are falsy.
# Everything else is truthy, including " " (a space is a character),
# "False" (a non-empty string) and [0] (a list that has one item).

values = [0, 1, -5, 0.0, "", " ", "False", [], [0], None, {}, ()]
for v in values:
    print(repr(v), "->", bool(v))
# 0 F | 1 T | -5 T | 0.0 F | "" F | " " T | "False" T | [] F | [0] T | None F | {} F | () F


# %%
# Exercise 3
# True + False = 1 here, which means ONE of the two conditions is true.
# Adding booleans counts how many are True.

has_license = True
is_verified = False

print(type(has_license))                  # <class 'bool'>
print(int(has_license), int(is_verified)) # 1 0
print(has_license + is_verified)          # 1
print(f"License: {has_license} | Verified: {is_verified}")


# %%
# Exercise 4
# isalnum() is False because _ is neither a letter nor a digit.
# islower() is False because the string has uppercase letters (D, E).

username = "Data_Eng2024"
print(username.isalpha())          # False: has _ and digits
print(username.isalnum())          # False: _ is not alphanumeric
print(username.isdigit())          # False
print(username.islower())          # False
print(username.isupper())          # False
print(username.startswith("Data")) # True
print(username.endswith("2024"))   # True
print(username[-4:].isdigit())     # True: "2024"


# %%
# Exercise 5
# bool is a SUBCLASS of int in Python, so isinstance(True, int) is True.
# If you need to tell real integers apart from booleans, check for bool first.

print(isinstance(25, int))            # True
print(isinstance(2.5, float))         # True
print(isinstance("25", int))          # False: it's a str
print(isinstance(True, bool))         # True
print(isinstance(True, int))          # True (!)
print(isinstance(2.5, (int, float)))  # True: matches any type in the tuple


# %%
# Exercise 6
# 10 / 2 is 5.0 because / always returns a float.
# Bonus: Python 3.12 added int.is_integer(), which always returns True.
# In older versions, (7).is_integer() raises AttributeError because the
# method only existed on floats.

print((7.0).is_integer())         # True
print((7.5).is_integer())         # False
print((10 / 2).is_integer())      # True: 5.0
print((10 / 3).is_integer())      # False: 3.333...
print(float("3.0").is_integer())  # True


# %%
# Exercise 7
# This chains a transformation and a check. You clean the data first,
# then validate it, just like Challenge 4 in your course notebook.

zip_code = "  10115 "
print(zip_code.strip().isdigit())            # True

zip_code = "10 115"
print(zip_code.strip().isdigit())            # False: inner space
print(zip_code.replace(" ", "").isdigit())   # True


# %%
# Exercise 8
# all() returns True only if EVERY item is truthy. 0 and "" break it.
# any() returns True if AT LEAST ONE item is truthy.
# all([]) is True because there's no item that fails.
# any([]) is False because there's no item that passes.
# This is called "vacuous truth", and it's a classic interview question.

readings = [12, 0, 7, 3]
names = ["Anna", "", "Ben"]

print(all(readings))  # False: 0 is falsy
print(any(readings))  # True
print(all(names))     # False: "" is falsy
print(any(names))     # True
print(all([]))        # True
print(any([]))        # False


# %%
# Exercise 9
# The big lesson: bool() of a STRING only asks whether it's empty,
# not what the text says. Convert to a number first if you mean the number.

print(bool("0"))                       # True: non-empty string
print(bool(int("0")))                  # False: the number 0
print(bool("0.0"))                     # True: non-empty string
print(bool(float("0.0")))              # False: the number 0.0
print(True == 1)                       # True
print(sum([True, False, True, True]))  # 3: counts the Trues
print(max(True, False))                # True: 1 > 0
print(len(str(False)))                 # 5: len("False")


# %%
# Exercise 10
# The bug: bool("false") is True, because "false" is a non-empty string.
# bool() never reads the text. You have to compare the actual value instead.

record = "  1042;Maria;;false  "

parts = record.strip().split(";")
print(parts)                      # ['1042', 'Maria', '', 'false']

id_valid = parts[0].isdigit()     # True
name_valid = parts[1].isalpha()   # True
email_present = bool(parts[2])    # False: empty string

print(bool(parts[3]))             # True: the bug
is_active = parts[3].strip().lower() == "true"   # False: correct

record_complete = all([id_valid, name_valid, email_present])  # False

print(f"ID ok: {id_valid} | Name ok: {name_valid} | Email: {email_present} | "
      f"Active: {is_active} | Complete: {record_complete}")
