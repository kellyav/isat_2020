#FIZZBUZZ PROGRAM 1: 2/5/2020
# Alexa Kelly 

#program that prints the numbers from 1 to 100. 
#But for multiples of three print “Fizz” instead of the number 
#and for the multiples of five print “Buzz”. 
#For numbers which are multiples of both three and five print “FizzBuzz”.

# checking n :
#n= 76

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
