# ============================================
# PASSWORD GENERATOR
# ============================================

import random
import string

def generate_password(length=12, use_upper=True, use_numbers=True, use_symbols=True):
    """Generate a random password with custom options."""
    
    # Start with lowercase letters (always included)
    characters = string.ascii_lowercase
    
    if use_upper:
        characters += string.ascii_uppercase    # A-Z
    if use_numbers:
        characters += string.digits             # 0-9
    if use_symbols:
        characters += string.punctuation        # !@#$%^&* etc.

    # Build the password by picking random characters
    password = ""
    for i in range(length):
        password += random.choice(characters)
    
    return password


def check_strength(password):
    """Check how strong a password is."""
    score = 0
    
    if len(password) >= 8:
        score += 1
    if len(password) >= 12:
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in string.punctuation for c in password):
        score += 1
    
    if score <= 2:
        return "Weak"
    elif score <= 3:
        return "Medium"
    else:
        return "Strong"


# ---------- Main Program ----------
print("=" * 40)
print("     PASSWORD GENERATOR")
print("=" * 40)

while True:
    print("\nOptions:")
    print("  1. Generate a password")
    print("  2. Generate multiple passwords")
    print("  3. Check a password's strength")
    print("  4. Quit")
    
    choice = input("\nPick an option (1-4): ")
    
    if choice == "1":
        length = input("Password length (default 12): ")
        if length.strip():
            try:
                length = int(length)
            except ValueError:
                print("Invalid number, using 12.")
                length = 12
        else:
            length = 12
        
        pwd = generate_password(length)
        strength = check_strength(pwd)
        print(f"\n  Your password: {pwd}")
        print(f"  Strength: {strength}")
    
    elif choice == "2":
        count = input("How many passwords? (default 5): ")
        count = int(count) if count.strip().isdigit() else 5
        length = input("Password length? (default 12): ")
        length = int(length) if length.strip().isdigit() else 12
        
        print(f"\n  Generated {count} passwords:")
        for i in range(count):
            pwd = generate_password(length)
            strength = check_strength(pwd)
            print(f"  {i+1}. {pwd}  ({strength})")
    
    elif choice == "3":
        pwd = input("Enter a password to check: ")
        strength = check_strength(pwd)
        print(f"  Strength: {strength}")
    
    elif choice == "4":
        print("Goodbye!")
        break
    
    else:
        print("Invalid option. Pick 1-4.")