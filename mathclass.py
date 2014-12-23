


class MathFunctions:

    def __init__(self, val1, val2):
        self.val1 = val1
        self.val2 = val2

    def add_val(self):
        print 'Addition of ' + str(self.val1) + '+' + str(self.val2) + ' = ' + str((int(self.val1)+int(self.val2)))

    def subtract_val(self):
        print 'Subtraction ' + str(self.val1) + '-' + str(self.val2) + ' = ' + str(int(self.val1)-int(self.val2))

    def multiply_val(self):
        print 'Multiplication ' + str(self.val1) + '*' + str(self.val2) + ' = ' + str(int(self.val1)*int(self.val2))

    def divide_val(self):
        print 'Division ' + str(self.val1) + '/' + str(self.val2) + ' = ' + str(float(self.val1)/float(self.val2))

