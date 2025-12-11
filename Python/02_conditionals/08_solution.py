password = "Secure3P@ss"
password_length = len(password)

if len(password) < 6:
    strength = "Weak"
elif len(password) <= 10:
    strength = "Moderate"
else:
    strength = "Strong"

print("Your password strength is:", strength)