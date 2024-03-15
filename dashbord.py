###multi level inheritance

class A:
    varA= "welcome to class A"

class B:
    varB = "welcome to class B"

class C(A,B):
    varC = "welcome to class c"

class D(C):
    varD = "welcome to class D"

class E(D):
    varE = "welcome boss "

d1 = E()
print(d1.varD)
print(d1.varC)
print(d1.varB)
print(d1.varA)
print(d1.varE)
