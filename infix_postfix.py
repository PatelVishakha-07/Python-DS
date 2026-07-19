def postfix(infix):
    stack = []
    postfix = ""

    for i in range(len(infix)):
        ch = infix[i]

        if ch in ("(", "^"):
            stack.append(ch)

        elif ch ==")":
            while stack and stack[-1] != "(":
                postfix += stack.pop()
            stack.pop()

        elif ch in ("*", "/"):
            if stack:
                while stack and stack[-1] in ("*", "/", "^"):
                    postfix += stack.pop()
            stack.append(ch)

        elif ch in ("+", "-"):
            if stack:
                while stack and stack[-1] in ("*", "/", "^", "+", "-"):                    
                    postfix += stack.pop()
            stack.append(ch)

        else:
            postfix += ch
    
    while stack:
        postfix += stack.pop()

    print("Infix exp: ", infix)
    print("Postfix exp: ", postfix)


infix = input("enter infix expression: ")
postfix(infix)