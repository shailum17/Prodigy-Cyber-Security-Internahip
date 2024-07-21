# Password complexity checker
import re
def password_check(password):
    length = len (password)>= 7
    uppercase = bool(re.search(r'[A-Z]', password))
    lowercase = bool(re.search(r'[a-z]', password))
    number = bool(re.search(r'[0-9]', password))
    special_char = bool(re.search(r'[@_!#$%^&*()<>?/\|]', password))
    total = length + uppercase + lowercase + number + special_char
    if total == 5:
        return "Strong password"
    elif total == 4:
        return "Medium password"
    else:
        return "Weak password"
    
password = input("Enter your password: ")
strength = password_check(password)
print(f"The strength of your entered password is {strength}")