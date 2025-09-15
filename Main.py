import random
lengthx = 0
character = "#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
print("Welcome to the Password Generator!")
lengthx = int(input("Enter the length of the password: "))
password = "".join(random.sample(character, lengthx))
print("Generated password:", password)
