def main(infix):
    
    Infix=[]
    prefix=[]
    stack=[]
    operators=["+", "-", "/", "*", "^"]
    for i in infix:
        Infix.append(i)
    while True:
        if len(Infix)==0:
            break
        else:
            element=Infix.pop()
            if element==")":
                stack.append(element)
            elif element=="(":
                while True:
                    if stack[-1]==")":
                        stack.pop()
                        break
                    else:
                        opr=stack.pop()
                        prefix.append(opr)
            elif 
                    

            
main("this")


























