#Made with luv by k6r <3
class calc():

    def add():
        add1 = int(input("input first number: "))
        add2 = int(input("what do you want to add? "))
        addData = add1 + add2
        print("the answer is", addData)

    def sub():
        sub1 = int(input("input first number: "))
        sub2 = int(input("what do you want to subtract? "))
        subData  = sub1 - sub2
        print("the answer is", subData)

    def mul():
        mul1 = int(input("input first number: "))
        mul2 = int(input("what do you want to multiply? "))
        mulData = mul1 * mul2
        print("the answer is", mulData)

    def div():
        div1 = int(input("input first number: "))
        div2 = int(input("what do you want to divide? "))
        divData = div1 / div2
        print("the answer is", divData)

asd = None
while asd not in {"+", "-", "*", "/"}:
    print("Choose Addition (+), subtraction (-), multiplication (*), division (/) only.")
    asd = input("Please choose: ")
        
    if asd == ("+"):
        calc.add()
    elif asd == ("-"):
        calc.sub()
    elif asd == ("*"):
        calc.mul()
    elif asd == ("/"):
        calc.div
    else:
        print("Please choose Addition (+), subtraction (-), multiplication (*), division (/) only.")
        asd




        





