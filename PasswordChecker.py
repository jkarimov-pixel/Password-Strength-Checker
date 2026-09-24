print("PASSWORD STRENGTH CHECKER")

password = input("Enter a password: ")

score = 0

# Check length
if len(password) >= 8:
    print("✓ At least 8 characters")
    score += 1
else:
    print("✗ At least 8 characters")

# Check uppercase letters
if any(letter.isupper() for letter in password):
    print("✓ Contains uppercase letter")
    score += 1
else:
    print("✗ Contains uppercase letter")

# Check lowercase letters
if any(letter.islower() for letter in password):
    print("✓ Contains lowercase letter")
    score += 1
else:
    print("✗ Contains lowercase letter")

# Check numbers
if any(letter.isdigit() for letter in password):
    print("✓ Contains number")
    score += 1
else:
    print("✗ Contains number")

# Check special characters
special_characters = "!@#$%^&*"

if any(letter in special_characters for letter in password):
    print("✓ Contains special character")
    score += 1
else:
    print("✗ Contains special character")

# Determine password strength
if score <= 2:
    strength = "Weak"
elif score <= 4:
    strength = "Medium"
else:
    strength = "Strong"

print("Password Strength:", strength)