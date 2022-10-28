    #METHOD RESOLUTION ORDER

class A:
    def myage(age):
        print("My age is 19")
class B(A):
    def myage(age):
        print("My age is 20")
class C(A):
    def rmyage(age):
        print("My age is 21")
    
class D(B, A):
        pass

jlmp = D()
jlmp.myage()