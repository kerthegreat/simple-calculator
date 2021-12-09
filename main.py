#Made with luv by k6r <3
res = None
while res not in {"addition", "subtraction", "multiplication", "division"}:
    print("Choose Addition, subtraction, multiplication, division only.")
    res = input("c h o o s e  y o u r  f a t e. ")
    if res == "addition":
        add1 = int(input("input first number: "))
        add2 = int(input("what do you want to add? "))
        addData = add1 + add2
        print("the answer is", addData)
    elif res == "subtraction":
        sub1 = int(input("input first number: "))
        sub2 = int(input("what do you want to subtract? "))
        subData  = sub1 - sub2
        print("the answer is", subData)
    elif res == "multiplication":
        mul1 = int(input("input first number: "))
        mul2 = int(input("what do you want to multiply? "))
        mulData = mul1 * mul2
        print("the answer is", mulData)
    elif res == "division":
        div1 = int(input("input first number: "))
        div2 = int(input("what do you want to divide? "))
        divData = div1 / div2
        print("the answer is", divData)

input("Press enter to close program")