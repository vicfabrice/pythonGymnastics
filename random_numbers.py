# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 18:51:11 2020

@author: VicFabrice
"""

import random
import secrets

print("Print a random number using random.random()")
print(random.random()) #returns random floating number in the range [0.0, 1.0)


# Random numbers generation
# Generate 3 randoms integers between 100 and 999 which is divisible by 5

random.randint(100,999)
count = 0
while (count != 3):
    number = random.randint(100,999)
    if number % 5 == 0:
        print("Random integer number is ",number)
        count += 1

#Esa fue mi solución pero la web donde leí el ejercicio da otra más cortita

print("Generating 3 random integer number between 100 and 999 divisible by 5")
for num in range(3):
    print(random.randrange(100,999,5), end=", ")

# Random Lottery Pick. Generate 100 random lottery tickets and pick two lucky 
# tickets from it as a winner.
# The lottery number must be 10 digits long.
# All 100 ticket number must be unique.

tickets = set([]) #best way to avoid repeat numbers
for num in range(100):
    tickets.add(random.randrange(0000000000,1000000000))
print("\nAnd the winner is ", random.sample(tickets,2), end=", ")
print("\nLenght of tickets set is ", len(tickets))

#Generate 6 digit random secure OTP

#Getting systemRandom class instance out of secrets module
secretsGenerator = secrets.SystemRandom()

randomSecureNumber = secretsGenerator.randint(111111,999999)
print("6 digit random secure OTP ", randomSecureNumber)

# Pick a random charcter from a given String

example = "random character from a given string"
randomChar = random.choice(example)
print("Random char from given string ", randomChar)