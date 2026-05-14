import art

def add(n1, n2):
    return n1 + n2

def mult(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2

def sub(n1, n2):
    return n1 - n2


print(art.logo)

while True:
    n1 = float(input("What's the first number?: "))

    opr = input("""
/
*
-
+
Enter the operator: """)

    n2 = float(input("What is the second number?: "))

    if opr == "/":
        ans1 = div(n1, n2)
    elif opr == "*":
        ans1 = mult(n1, n2)
    elif opr == "-":
        ans1 = sub(n1, n2)
    elif opr == "+":
        ans1 = add(n1, n2)
    else:
        print("Please enter the given operator!!")
        break

    print(f"{n1} {opr} {n2} = {ans1}")

    usi = input(f"Type 'y' to continue calculating with {ans1}, or type 'n' to start a new calculation: ")

    while usi == "y":
        opr = input("""
/
*
-
+
Enter the operator: """)

        n2 = float(input("What is the next number?: "))

        old_ans = ans1

        if opr == "/":
            ans1 = div(ans1, n2)
        elif opr == "*":
            ans1 = mult(ans1, n2)
        elif opr == "-":
            ans1 = sub(ans1, n2)
        elif opr == "+":
            ans1 = add(ans1, n2)
        else:
            print("Please enter the given operator!!")
            break

        print(f"{old_ans} {opr} {n2} = {ans1}")

        usi = input(f"Type 'y' to continue calculating with {ans1}, or type 'n' to start a new calculation: ")
