class A:
    def __init__(self, a):
        self.a = a
    def __lt__(self, other):
        if(self.a < other.a):
            return "a is less b"
        else:
            return "a is greater than b"
    def __eq__(self, other):
        if(self.a == other.a):
            return "Both are equal"
        else:
            return "They are not Equal"
o1 = A(2)
o2 = A(3)
print("Passed values :",o1.a, o2.a)
print(o1 < o2)

o3 = A(4)
o4 = A(4)
print("Passed values :", o3.a, o4.a)
print(o3==o4)