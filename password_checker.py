password = input("Please enter a password")

while 6 > len(password) or 12 < len(password):
    print("Invalid password, must be between 6 and 12 characters")
    password = input("Please enter a password")
print("Password accepted: {}".format("*" * (len(password))))
