print '''
1. Write a program to implement a method which takes a list as an argument and returns second largest number.
   read from standard input and write to standard output. 
'''

print "Option 1"
print "========="
print "To find Out Second Largest Number Using Array Sort"
print '---------------------------------------------------'
numbers=[1,4,3,6,5]
print "\nArray Values is = " + str(numbers)

numbers.sort()
print "\nAfter Sorting the Array Value is = " +str(numbers)

print "\nThe Second Largest Number is = " + str(numbers[-2])

numbers.sort(reverse=True)
print "\nAfter Reverse Sorting the Array Value is = " +str(numbers)

print "\nThe Second Largest Number is = " + str(numbers[1]) + "\n"

print "Option 2"
print "========"
print "To find Out Second Largest Number without Array Sort"
print '-----------------------------------------------------'

numbers=[6,4,3,3,8,-6]
print "\nArray Values is = " + str(numbers)
SLN = max(n for n in numbers if n!=max(numbers))
print "\nThe Second Largest Number is = " + str(SLN) + "\n"






