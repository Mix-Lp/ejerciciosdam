from datetime import datetime
from sys import argv
from time import time

script, user_name, location = argv
prompt = '> '

print("Hi %s, I'm the %s script." % (user_name, script))
print("I'd like to ask you a few questions.")
print("Do you live in %s?" % location)
answer = input(prompt)
if answer.lower() == "yes":
    print("I trust you %s." % user_name)
else:
    print("You are lying to me, %s" % user_name)

print("Do you like me %s?" % user_name)
likes = input(prompt)
print("Alright %s, so you said %r about liking me" % (user_name, likes))
print("Now, how old are you, %s?" % user_name)
age = input(prompt)
age = int(age)
year = 2021-age
print("So... you were born in %d, right %s?" % (year, user_name))


