password = input("Enter your password: ")

include = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", ";", ":", "'", '"', ",", ".", "<", ">", "/", "?", "|"]

if len(password) < 8:
    print("Password is too short. It must be at least 8 characters long.")
if password.islower() or password.isupper():
    print("Password must have both upper and lower case.")
else:
    print("Please add an uppercase and lowercase in your password with a min 8.")

for special_charecter in include:
    if special_charecter not in password:
        print("Password must have at least one special character like !, @, #, $, %, ^ ")
        break
