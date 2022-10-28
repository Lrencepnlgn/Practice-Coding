#Single Inheritance

class Myself:
  def __init__(self, myname, myage, myaddr):
    self.myname = myname
    self.myage = myage
    self.myaddress = myaddr
    
  def myfunction(rence):
    print("Hi my name is " + rence.myname + rence.myage + rence.myaddress)

      
m1 = Myself("John Laurence Mendoza Panaligan.\n", "and I am 20 years old.\n", 
                "I  live in Wawa, Batangas City")
m1.myfunction()

