def main(infix):
    stack = []
    postfix = []
    operators = {
        "+": 0, "-": 0,
        "*": 1, "/": 1,
        "(": "braket", ")": "braket",
        "^": 3
    }
    starting = 1
    for i in infix:
        print("***********NEXT LEVEL**********************")
        print("step \t\t", starting)
        print("Stack\t\t", stack)
        print("postfix\t\t", postfix)
        if i in operators:
            if len(stack) == 0 or i == "(":
                stack.append(i)
            elif i == ")":
                while True:
                    if stack[-1] == "(":
                        stack.pop()
                        break
                    else:
                        x = stack.pop()
                        postfix.append(x)
            else:
                while True:
                    if len(stack) == 0:
                        stack.append(i)
                        break
                    elif stack[-1] == "(":
                        stack.append(i)
                        break
                    elif operators[i] <= operators[stack[-1]]:
                        x = stack.pop()
                        postfix.append(x)
                    else:
                        stack.append(i)
                        break
        else:
            postfix.append(i)
        starting += 1
    if len(stack) != 0:
        for i in range(len(stack)):
            x = stack.pop()
            postfix.append(x)
    print(postfix)

main("(((A+B)*(C-E))/(F+G))")


















