import roman

class Rome:
    def num(self, x):
        return roman.toRoman(x)


n = Rome()

while True:
    num = int(input("Enter a number: "))
    result = n.num(num)
    print("Roman:", result)

    i = int(input("Enter 1 to exit, any other number to continue: "))
    if i == 1:
        break