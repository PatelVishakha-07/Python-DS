def evaluate(exp):
    stack = []
    no = 0
    for i in range(len(exp)):    
        if exp[i].isdigit():
            ch = int(exp[i])            

            no = (no*10) + ch
            if len(exp) == i+1 or not exp[i+1].isdigit():
                stack.append(no)
                no = 0
        
        elif exp[i] != " ":
            n2 = stack.pop()
            n1 = stack.pop()
            stack.append(calculate(n1,n2,exp[i]))

    print("Ans:", stack.pop())


def calculate(n1, n2, ch):
    if ch == "+":
        return n1+n2
    elif ch == "-":
        return n1-n2
    elif ch == "*":
        return n1*n2
    elif ch == "/":
        return n1/n2


exp = input("enter postfix expression: ")
evaluate(exp)