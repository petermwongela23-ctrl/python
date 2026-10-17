# ============================================
# PYTHON BASICS PRACTICE
# ============================================

# ---------- 1. VARIABLES & DATA TYPES ----------
name = "Peter"
age = 20
gpa = 3.7
is_student = True

print("=== Variables & Data Types ===")
print("Name:", name)
print("Age:", age)
print("GPA:", gpa)
print("Is Student:", is_student)
print("Type of name:", type(name))
print("Type of age:", type(age))
print()

# ---------- 2. STRINGS ----------
first_name = "Peter"
last_name = "Student"
full_name = first_name + " " + last_name  # concatenation

print("=== Strings ===")
print("Full Name:", full_name)
print("Upper:", full_name.upper())
print("Lower:", full_name.lower())
print("Length:", len(full_name))
print("Contains 'Student'?", "Student" in full_name)
print()

# ---------- 3. INPUT & TYPE CASTING ----------
print("=== Input & Type Casting ===")
user_age = input("Enter your age: ")        # input always returns a string
user_age_int = int(user_age)                # convert to integer
print("In 10 years you will be:", user_age_int + 10)
print()

# ---------- 4. IF / ELIF / ELSE ----------
print("=== If / Elif / Else ===")
score = 78

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print("Score:", score, "-> Grade:", grade)
print()

# ---------- 5. LOOPS ----------
print("=== For Loop ===")
for i in range(1, 6):        # 1 to 5
    print("  Count:", i)

print()
print("=== While Loop ===")
countdown = 5
while countdown > 0:
    print("  Countdown:", countdown)
    countdown -= 1
print("  Go!")
print()

# ---------- 6. LISTS ----------
print("=== Lists ===")
fruits = ["apple", "banana", "cherry"]
print("Fruits:", fruits)
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])

fruits.append("mango")       # add to end
print("After append:", fruits)

fruits.remove("banana")     # remove by value
print("After remove:", fruits)

print("Loop through list:")
for fruit in fruits:
    print("  -", fruit)

print("Number of fruits:", len(fruits))
print()

# ---------- 7. DICTIONARIES ----------
print("=== Dictionaries ===")
student = {
    "name": "Peter",
    "age": 20,
    "major": "CS",
    "gpa": 3.7
}

print("Student info:", student)
print("Name:", student["name"])
print("GPA:", student["gpa"])

student["year"] = "Sophomore"   # add new key
print("After adding year:", student)

print("Loop through dictionary:")
for key, value in student.items():
    print(f"  {key}: {value}")
print()

# ---------- 8. FUNCTIONS ----------
print("=== Functions ===")

def greet(person_name):
    return "Hello, " + person_name + "!"

def add(a, b):
    return a + b

def is_passing(score):
    return score >= 60

print(greet("Peter"))
print("3 + 7 =", add(3, 7))
print("Is 78 passing?", is_passing(78))
print("Is 45 passing?", is_passing(45))
print()

# ---------- 9. F-STRINGS (formatted strings) ----------
print("=== F-Strings ===")
subject = "Python"
days = 7
print(f"I am learning {subject} for {days} days.")
print(f"2 + 3 = {2 + 3}")
print(f"My GPA is {3.7:.2f}")  # 2 decimal places
print()

# ---------- 10. LIST COMPREHENSION ----------
print("=== List Comprehension ===")
squares = [x ** 2 for x in range(1, 11)]
print("Squares 1-10:", squares)

even_numbers = [x for x in range(1, 21) if x % 2 == 0]
print("Even numbers 1-20:", even_numbers)
print()

# ---------- 11. TRY / EXCEPT (error handling) ----------
print("=== Try / Except ===")
try:
    number = int("hello")   # this will fail
except ValueError:
    print("That's not a valid number!")

try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
print()

# ---------- 12. MINI CHALLENGE: Guess the Number ----------
print("=== Mini Challenge: Guess the Number ===")
import random

secret = random.randint(1, 100)
attempts = 0

print("I'm thinking of a number between 1 and 100.")

while True:
    guess_input = input("Your guess: ")
    try:
        guess = int(guess_input)
    except ValueError:
        print("Please enter a valid number!")
        continue

    attempts += 1

    if guess < secret:
        print("Too low! Try again.")
    elif guess > secret:
        print("Too high! Try again.")
    else:
        print(f"Correct! You got it in {attempts} attempts!")
        break