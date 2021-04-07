
array=[0, 12, 345,6789,1234  ]
Passes=1
for i in range(4):
    print("*************************************************************")
    print("*************************************************************")
    power=10**i
    zero=[]
    one=[]
    two=[]
    three=[]
    four=[]
    five=[]
    six=[]
    seven=[]
    eight=[]
    nine=[]
    for element in array:
        if power==1:
            if element<10:
                if element==0:
                    zero.append(element)
                elif element==1:
                    one.append(element)
                elif element==2:
                    two.append(element)
                elif element==3:
                    three.append(element)
                elif element==4:
                    four.append(element)
                elif element==5:
                    five.append(element)
                elif element==6:
                    six.append(element)
                elif element==7:
                    seven.append(element)
                elif element==8:
                    eight.append(element)
                else:
                    nine.append(element)
            else:
                if element%10==0:
                    zero.append(element)
                elif element%10==1:
                    one.append(element)
                elif element%10==2:
                    two.append(element)
                elif element%10==3:
                    three.append(element)
                elif element%10==4:
                    four.append(element)
                elif element%10==5:
                    five.append(element)
                elif element%10==6:
                    six.append(element)
                elif element%10==7:
                    seven.append(element)
                elif element%10==8:
                    eight.append(element)
                else:
                    nine.append(element)
        elif power==10:
            if element/10<1:
                zero.append(element)
            else:
                remainder=element//10
                if remainder<10:
                    if remainder==0:
                        zero.append(element)
                    elif remainder==1:
                        one.append(element)
                    elif remainder==2:
                        two.append(element)
                    elif remainder==3:
                        three.append(element)
                    elif remainder==4:
                        four.append(element)
                    elif remainder==5:
                        five.append(element)
                    elif remainder==6:
                        six.append(element)
                    elif remainder==7:
                        seven.append(element)
                    elif remainder==8:
                        eight.append(element)
                    else:
                        nine.append(element)
                else:
                    remainder=remainder%10
                    if remainder==0:
                        zero.append(element)
                    elif remainder==1:
                        one.append(element)
                    elif remainder==2:
                        two.append(element)
                    elif remainder==3:
                        three.append(element)
                    elif remainder==4:
                        four.append(element)
                    elif remainder==5:
                        five.append(element)
                    elif remainder==6:
                        six.append(element)
                    elif remainder==7:
                        seven.append(element)
                    elif remainder==8:
                        eight.append(element)
                    else:
                        nine.append(element)
        elif power==100:
            if element//100<1:
                zero.append(element)
            elif element//100<10:
                remainder=element//10
                remainder=remainder%10
                if remainder==0:
                    zero.append(element)
                elif remainder==1:
                    one.append(element)
                elif remainder==2:
                    two.append(element)
                elif remainder==3:
                    three.append(element)
                elif remainder==4:
                    four.append(element)
                elif remainder==5:
                    five.append(element)
                elif remainder==6:
                    six.append(element)
                elif remainder==7:
                    seven.append(element)
                elif remainder==8:
                    eight.append(element)
                else:
                    nine.append(element)
            else:
                remainder=element//100
                remainder=remainder%10
                if remainder==0:
                    zero.append(element)
                elif remainder==1:
                    one.append(element)
                elif remainder==2:
                    two.append(element)
                elif remainder==3:
                    three.append(element)
                elif remainder==4:
                    four.append(element)
                elif remainder==5:
                    five.append(element)
                elif remainder==6:
                    six.append(element)
                elif remainder==7:
                    seven.append(element)
                elif remainder==8:
                    eight.append(element)
                else:
                    nine.append(element)
        else:
            if element%1000==0:
                zero.append(element)
            else:
                remainder=element//1000
                if remainder==0:
                    zero.append(element)
                elif remainder==1:
                    one.append(element)
                elif remainder==2:
                    two.append(element)
                elif remainder==3:
                    three.append(element)
                elif remainder==4:
                    four.append(element)
                elif remainder==5:
                    five.append(element)
                elif remainder==6:
                    six.append(element)
                elif remainder==7:
                    seven.append(element)
                elif remainder==8:
                    eight.append(element)
                else:
                    nine.append(element)

                

    print("0=====",zero), print("1====",one), print("2====",two), print("3====",three), print("4====",four), print("5====",five), print("6====",six), print("7====",seven), print("8====",eight), print("9====",nine)
    Pass1=[]
    for i in zero:
        Pass1.append(i)
    for i in one:
        Pass1.append(i)
    for i in two:
        Pass1.append(i)
    for i in three:
        Pass1.append(i)
    for i in four:
        Pass1.append(i)
    for i in five:
        Pass1.append(i)
    for i in six:
        Pass1.append(i)
    for i in seven:
        Pass1.append(i)
    for i in eight:
        Pass1.append(i)
    for i in nine:
        Pass1.append(i)
    array=Pass1
    
    print("Pass",Passes)
    print(array)
    Passes+=1
                

        

                

    
