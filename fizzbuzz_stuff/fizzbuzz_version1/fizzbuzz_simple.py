#FIZZBUZZ PROGRAM 1: 2/5/2020
# Alexa Kelly 

#program that checks for mutliples of 3, 5 and 15. 
#for multiples of three print “Fizz” instead of the number, for the multiples of five print “Buzz”. 
#for a number that is a multiple of both three and five print “FizzBuzz”, otherwise return the input.

# user inputs n:
print("Enter a value for n between 1 and 100:")
n= int(input())

if n % 15 ==0:
    print('fizzbuzz')
else: 
    if n % 5 ==0:
        print('buzz')
    else: 
        if n % 3 ==0:
            print('fizz')
        else:
            print(n)

# run in command line by typing: python fizzbuzz1.py. then input a number 
