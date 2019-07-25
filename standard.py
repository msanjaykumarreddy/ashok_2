"""
basic arithametic operations
"""


class Standardmathemeticaloperations:
    """
    simple operations
    """

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        """
         adding two numbers
        :return:
        """
        result_add = self.a + self.b
        # print("result_add :",result_add)
        return result_add

    def multiplication(self):
        """
        multiplying two numbers
        :return:
        """
        result_mul = self.a * self.b
        # print("Multiplication :",result_mul)
        return result_mul

    def division(self):
        """
        dividing two numbers
        :return:
        """
        result_div = self.a / self.b
        # print("Division :",result_div)
        return result_div

    def substraction(self):
        """
        substracting two numbers
        :return:
        """
        result_sub = self.a - self.b
        # print("Substarction :",result_sub)
        return result_sub


"""
    obj=Standardmathemeticaloperations(27,2)
    obj.addition()
    obj.multiplication()
    obj.division()
    obj.substraction()
  """
