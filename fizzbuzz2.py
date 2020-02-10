
#FIZZBUZZ PROGRAM (2)

#program that prints the numbers from 1 to 100. 
#But for multiples of three print “Fizz” instead of the number 
#and for the multiples of five print “Buzz”. 
#For numbers which are multiples of both three and five print “FizzBuzz”.
    


# LOOP for checking NUMBERS 1 THRU 100.
# creates a list of numbers from 1-100 with the respective numbers replaced by "fizzbuzz", etc.

n=100
for i in range(1,n):
    if i % 15 ==0:
        print('fizzbuzz')
    else: 
        if i % 5 ==0:
            print('buzz')
        else: 
            if i % 3 ==0:
                print('fizz')  
            else:
                print(i)
