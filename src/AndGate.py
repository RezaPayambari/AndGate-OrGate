__version__ = '1.0'
__author__ = 'Reza Payambari (reza.payambari@students.tbs1.de)'

class AndGate:

# Initialize the object with 2 parameters
# The default value of the given parameteres ist False.
    def __init__(self,value=False,value1=False):
        self.__Input0 = value
        self.__Input1 = value1
        self.__Output = False
        self.__Name = "YaAndKlasse"


# Execute function will do the And between two boolean values
#
# @return
# True: when both given values are true.
# False: when any of the given values is False.
    def execute(self):
        if self.__Input0 == True and self.__Input1 == True:
            self.__set_output(True)
        else:
            self.__set_output(False)



# Shows the Output value on the screen
    def show(self):
        print("Output() = " + str(self.__get_output()))

# Shows the value of all variables and
# other iformation like, author, version and the class name.
    def showInfo(self):
        print("Name = " + str(self.__Name) + "\n")
        print("Version = " + str(__version__) + "\n")
        print("Author = " + str(__author__) + "\n")
        print("Input0 = " + str(self.__get_input0()) + "\n")
        print("Input1 = " + str(self.__get_input1()) + "\n")
        print("Output() = " + str(self.__get_output()))


# Overrides __str__ method in Object
    def __str__(self):
        return (str(self.__get_name()) + ' ' + str(self.__get_output()))


# Setter and Getter of Input0
    def __set_input0(self, value):
        self.__Input0 = value

    def __get_input0(self):
        return self.__Input0


# Setter and Getter of Input1
    def __set_input1(self, value):
        self.__Input1 = value

    def __get_input1(self):
        return self.__Input1


# Setter and Getter of Name
    def __set_name(self, value):
        self.__Name = value

    def __get_name(self):
        return self.__Name


# Setter and Getter of Output
    def __set_output(self, value):
        self.__Output = value

    def __get_output(self):
        return self.__Output

    Name = property(__get_name, __set_name)
    Input0 = property(__get_input0, __set_input0)
    Input1 = property(__get_input1, __set_input1)
    Output = property(__get_output, None)
