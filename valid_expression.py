def isValid(exp):
    stack = []
    f=0
    for i in range(len(exp)):
        if exp[i] in ("(", "{", "["):
            stack.append(exp[i])

        elif exp[i] == ")":
            if stack and stack[-1] != "("  or not stack:        
                f=1
                break
            stack.pop()
        
        elif exp[i] == "}":
            if stack and stack[-1] != "{"  or not stack:        
                f=1
                break
            stack.pop()

        elif exp[i] == "]":
            if stack and stack[-1] != "["  or not stack:        
                f=1
                break
            stack.pop()
    
    print("Expression: ",exp)
    if stack or f==1:
        print("Invalid Expression")
    else:
        print("Valid Expression")

exp = input("enter expression: ")
isValid(exp)