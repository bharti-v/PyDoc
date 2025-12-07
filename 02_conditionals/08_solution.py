# Password Strength Checker
# Problem: Check if a password is "Weak', "Medium", or "Strong•. Criteria: < 6 chars (Weak), 6-10 chars (Medium), >10 chars (Strong).

password = "Sure3P@ss"

if len(password) < 6:
    strength = "Weak"
if len(password) <= 10:
    strength = "Medium"
else:
    strength = "Strong"

print("Password strength is:", strength)