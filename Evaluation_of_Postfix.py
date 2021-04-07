def main(postfix):
    operators=["+", "-", "/", "*", "^"]
    Postfix=[]
    stack=[]
    for i in postfix:
        Postfix.append(i)
    for i in Postfix:
        print("**************NEXT STEP********************\n")
        print(stack)
        print("Next item\t",i)
        if i in operators:
            x=int(stack.pop())
            y=int(stack.pop())
            if i=="*":
                z=y*x
                print("",y, i, x)
                stack.append(z)
            elif i=="-":
                z=y-x
                print("",y, i, x)
                stack.append(z)
            elif i=="/":
                z=y/x
                print("",y, i, x)
                stack.append(z)
            elif i=="+":
                z=y+x
                print("",y, i, x)
                stack.append(z)
            else:
                z=y**x
                print("",y, i, x)
                stack.append(z)
        else:
            stack.append(i)
    print(stack)
main("623+-382/+*2^3+")

    