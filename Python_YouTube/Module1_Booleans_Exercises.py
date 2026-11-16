# Module 1: Boolean Values & Functions - Exercises
#
# Rules:
# 1. For "predict" exercises, write your predictions as comments BEFORE you run anything.
#    Then run the code and compare.
# 2. Don't open Module1_Booleans_Solutions.py until you've tried every exercise.
# 3. When you're done, ask Claude to "grade Module 1".
#
# Pass mark: 8/10 correct, including at least 2 of the 3 Level 3 exercises.
# Tip: each "# %%" line starts a cell. In VS Code, click "Run Cell" above it to run just that part.


# ============================================================
# LEVEL 1: MILD
# ============================================================

# %%
# Exercise 1: Booleans are a data type
# Predict the output of each line, then run it.

# My predictions:

print(type(True)) #Bool
print(type("True"))#String
print(True + True)#2
print(True * 10)#10
print(int(False))#0
print(float(True))#1.0
print(str(True) + "!")#True!


# %%
# Exercise 2: Truthy or falsy?
# Predict True or False for bool() of each value, then check with code:
#   0, 1, -5, 0.0, "", " ", "False", [], [0], None, {}, ()
# Then write ONE sentence describing the rule: which values are falsy?

# My predictions:

# My rule:
#bool() returns False for values that are 0, empty, or None
# Your code:
print(bool(0))#False
print(bool(1))#True
print(bool(-5))#True
print(bool(0.0))#False
print(bool("")) #False
print(bool(" "))#True
print(bool("False"))#True
print(bool([]))#False
print(bool([0]))#True
print(bool(None)) #False
print(bool({}))#False
print(bool(()))#False
# %%
# Exercise 3: Create and convert
# 1. Create has_license = True and is_verified = False.
# 2. Print the type of has_license.
# 3. Print both variables converted to int.
# 4. Print has_license + is_verified. What does the result mean?
# 5. Print the sentence "License: True | Verified: False" using an f-string.

# Your code:
has_license = True
is_verified = False

print(type(has_license))
print(int(has_license), int(is_verified))
print(has_license + is_verified) #1 Both True and False are treated as numerical values namely 1 and 0 respectfully.
print(f"License: {has_license} | Verified: {is_verified}")

# ============================================================
# LEVEL 2: INTERMEDIATE
# ============================================================

# %%
# Exercise 4: String methods that return booleans
# Predict, then run each one:
#   isalpha(), isalnum(), isdigit(), islower(), isupper(),
#   startswith("Data"), endswith("2024"), and username[-4:].isdigit()
# Explain why isalnum() gives the result it does.

username = "Data_Eng2024"

# My predictions:
#False
#False
#False
#False
#False
#True
#True
#True

# Your code:

print(username.isalpha())
print(username.isalnum())
print(username.isdigit())
print(username.islower())
print(username.isupper())
print(username.startswith("Data"))
print(username.endswith("2024"))
print(username[-4:].isdigit())

# Explain why isalnum() gives the result it does. This is because the "Data_Eng2024" has an underscore in it. 
# %%
# Exercise 5: isinstance()
# Use isinstance() to check:
# 1. Is 25 an int?
# 2. Is 2.5 a float?
# 3. Is "25" an int?
# 4. Is True a bool?
# 5. Is True an int? Predict this first. The answer surprises most people.
# 6. Is 2.5 an int OR a float, checked in ONE call? (Hint: you can pass a tuple of types.)

# My predictions:
# True
# True
# False
# True
# True
# True

# Your code:
print(isinstance(25, int))
print(isinstance(2.5, float))
print(isinstance("25", int))
print(isinstance(True, bool))
print(isinstance(True, int))
print(isinstance(2.5, (int, float)))

# %%
# Exercise 6: is_integer()
# Predict, then run.
# Bonus: why does (7).is_integer() behave differently from (7.0).is_integer()?
#        Try it in a recent Python version and explain what you see.

# My predictions:

print((7.0).is_integer()) # True
print((7.5).is_integer()) # False
print((10 / 2).is_integer()) #True
print((10 / 3).is_integer()) # False
print(float("3.0").is_integer()) # True


# %%
# Exercise 7: Clean, then validate
# A user typed a postal code: zip_code = "  10115 "
# 1. Write ONE expression that returns True if the code contains only digits
#    once you remove the surrounding spaces.
# 2. Now zip_code = "10 115". Your expression should return False.
#    Change it so the code counts as valid when you ignore ALL spaces.

zip_code = "  10115 "

# Your code:
zip_code = zip_code.strip()
print(zip_code.isdigit())


#2
zip_code = "10 115"
print(zip_code.replace(" ", "").isdigit())


# ============================================================
# LEVEL 3: ADVANCED
# ============================================================

# %%
# Exercise 8: any() and all()
# Predict, then run. Explain the last two results in your own words.

# My predictions:

readings = [12, 0, 7, 3]
names = ["Anna", "", "Ben"]

print(all(readings)) #False
print(any(readings)) #True
print(all(names)) #False
print(any(names)) #True
print(all([]))#True Because it has no Falses to find in the list
print(any([]))#False Becaue it has no Trues in the list


# %%
# Exercise 9: Trick round
# Predict ALL of these before running anything. Each one tests a specific trap.

# My predictions:

print(bool("0"))#True
print(bool(int("0"))) #False
print(bool("0.0"))#True
print(bool(float("0.0")))#False
print(True == 1) #True
print(sum([True, False, True, True]))#3
print(max(True, False))#True
print(len(str(False))) #5


# %%
# Exercise 10: Data quality check (challenge)
# Fields in the record: id ; name ; email ; is_active
#
# 1. Strip the record and split it into a list called parts.
# 2. Create these boolean variables:
#    - id_valid: the id contains only digits
#    - name_valid: the name contains only letters
#    - email_present: the email field is not empty (use bool())
#    - is_active: the user is active, based on the last field
# 3. A teammate wrote is_active = bool(parts[3]). What does it return,
#    and WHY is that a bug? Write a correct version.
#    (A preview of comparison operators is fine here.)
# 4. Create record_complete, which is True only if id_valid, name_valid
#    and email_present are all True. Use one built-in function.
# 5. Print one summary line with an f-string.

record = "  1042;Maria;;false  "

# Your code:
record = "  1042;Maria;;false  "

part = record.strip().split(';') #["1024", "Maria", "", "false"]
print(part)

id_valid = part[0].isdigit() #True
name_valid = part[1].isalpha() #True
email_present = bool(part[2]) #False

print(bool(part[3])) #True This bool only asks if the string is empty or not, not what the string actually tells us, which is an inactive user.
is_active = part[3].strip().lower() == "true"

record_complete = all([id_valid, name_valid, email_present])
print(record_complete)

print(f"Id: {id_valid} | name: {name_valid} | email:{email_present} | is_active: {is_active} | Record: {record_complete}")

