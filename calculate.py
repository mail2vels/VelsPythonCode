print '''
    4. Create a package folder which contains a Mads class whith methods of addition, Muliplication, devision and subtraction.
    Use the package in another file to do  addition, Muliplication, devision and subtraction.
'''

def calculate_vals(val1, val2):

    import mathclass as mc

    mcobj = mc.MathFunctions(val1, val2)

    mcobj.add_val()
    mcobj.subtract_val()
    mcobj.multiply_val()
    mcobj.divide_val()


val1 = raw_input("Enter First Value : ")

val2 = raw_input("Enter Second Value : ")

print '\nThe Result is below'
print '====================\n'

calculate_vals(val1, val2)
