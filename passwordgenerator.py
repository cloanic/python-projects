import random
#print Hello and what the program is
print('Hello From Your Password Generator')
#collects characters (it can be any character you add)
chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$%^&*().,?0123456789"
#input the amount of passwords to generate and makes sure they are converted to an int
number = input('Amount of passwords to generate: ')
number = int(number)
#input the length of each password to generate and makes sure they are converted to an int
length = input('Password length: ')
length = int(length)
#prints your passwords
print('\nhere are your passwords: ')
#for loop password in range of amount of passwords to generate
for pwd in range(number):
    passwords = ''
#for loop password in range of length of passwords you want to generate
    for c in range(length):
        #randomized choice based on the chars variable we set earlier
        passwords += random.choice(chars)
    print(passwords)



