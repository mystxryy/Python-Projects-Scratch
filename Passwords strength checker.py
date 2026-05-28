print()
print("=" * 50)
print("   PASSWORD STRENGTH CHECKER")
print("=" * 50)
print()
print("Disclaimer: Your password must contain some special characters like '!@#$%^&*()[]?><\\|' to make it more secure.")

password = input("Enter a password: ")

print()
print("Analyzing...")
print()
print("=" * 50)
print()

strength = 0

length = len(password)
if length >= 8:
    print("Length: 8+ characters")
    strength += 1
else:
    print(f"Length: Only {length} characters (need 8+)")

has_lower = any(c.islower() for c in password)
if has_lower:
    print("Lowercase letters: Found")
    strength += 1
else:
    print("Lowercase lettrs: Missing")

has_upper = any(c.isupper() for c in password)
if has_upper:
    print("Uppercase letters: Found")
    strength += 1
else:
    print("Uppercase letters: Missing")

has_digit = any(c.isdigit() for c in password)
if has_digit:
    print("Numbers: Found")
    strength += 1
else:
    print("Numbers: Missing")

has_special = any(c in '!@#$%^&*()[]?><\\|' for c in password)
if has_special:
    print("Special characters: Found")
    strength += 1
else:
    print("Special characters: Missing")

print()
print("=" * 50)

if strength <= 1:
    rating = "VERY WEAK"
elif strength == 2:
    rating = "WEAK"
elif strength == 3:
    rating = "FAIR"
elif strength == 4:
    rating = "STRONG"
else:
    rating = "VERY STRONG"

print(f"Final Rating: {rating}")
print(f"Strength Score: {strength}/5")
print("=" * 50)