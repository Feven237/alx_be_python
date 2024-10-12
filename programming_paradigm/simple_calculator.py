class SimpleCalculator () :
 try:
   def add (self, a , b):
    return a+ b
   def substract (self, a, b):
    return a-b
   def multiply (self, a, b):
    return a * b
   def divide (self, a, b):
    return a / b
 except ZeroDivisionError:
    print ("None")