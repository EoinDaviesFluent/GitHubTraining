#class ExampleClass:
#    attribute_1 = 'somedate'
#    attribute_2 = 123
#    def examplefunction(self, inputvar): # always need the self
#        <example_code>

class Addanumber:
    the_number=1
    def add_the_number(self,input_var):
        output_var = input_var+self.the_number
        return output_var

object1=Addanumber()
object2=Addanumber()
object3=Addanumber()

object2.the_number = 2
object3.the_number = 3

print (object1.the_number)
print (object2.the_number)
print (object3.the_number)

print (object1.add_the_number(5))
print (object2.add_the_number(5))
print (object3.add_the_number(5))