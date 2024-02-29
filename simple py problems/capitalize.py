# You are asked to ensure that the first and last names of people begin with a capital letter in their passports. For example, alison heck should be capitalised correctly as Alison Heck.

# Given a full name, your task is to capitalize the name appropriately.
def solve(s):
   
    parts = s.split()
    
    capitalized_name_parts = [part[0].upper() + part[1:].lower() for part in parts]
    # Join the parts back together with spaces
    capitalized_name = ' '.join(capitalized_name_parts)

    return capitalized_name

print(solve("132 456 Wq  m e"))
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()