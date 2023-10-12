def Input():
    Operation=input(print("Enter Operation (OR,XOR,NOT,AND)")) #Lazy inputs
    Var1=input(print("Enter Binary1"))
    Var2=input(print("Enter Binary2"))
    Validate(Var1,Var2,Operation)

def Validate(Var1,Var2,Operation):
    for i in range(len(Var1)): #Checks input is only comprised of 0&1
        if Var1[i] != "1" and Var1[i] != "0": #Could of used regex but this works
            print("Input 1 not Binary.")
            Input()
    for i in range(len(Var2)):
        if Var2[i] != "1" and Var2[i] != "0":
            print("Input 2 not Binary.")
            Input()
    Var1=Var1.zfill(8) #Make all variables 8 bit length.
    Var2=Var2.zfill(8)
    if(Operation=="OR"): #Lazy validation on input
        OR(Var1,Var2) #Calls appropriate function
    if(Operation=="XOR"):
        XOR(Var1,Var2)
    if(Operation=="AND"):
        AND(Var1,Var2)
    if(Operation=="NOT"):
        NOT(Var1,Var2)
    print("Operation Not valid")
    Input()

def NOT(Var1,Var2):
    NewVar1=""
    NewVar2=""
    for i in range(len(Var1)): #Inverts values of each variable
        if Var1[i]=="1":
            NewVar1=NewVar1+"0"
        else:
            NewVar1=NewVar1+"1"
    if len(Var2) !=0: 
        for i in range(len(Var2)):
            if Var2[i]=="1":
                NewVar2=NewVar2+"0"
            else:
                NewVar2=NewVar2+"1"
    print("Not Result is: ",NewVar1,NewVar2)

def XOR(Var1,Var2):
    NewVar=""
    for i in range(len(Var1)): #Breaking down the operation to not use AND or OR
        if (int(Var1[i])==int(Var2[i])):
            NewVar=NewVar+"0"
        else:
            NewVar=NewVar+"1"
    print("XOR Result: ",NewVar)

def AND(Var1,Var2):
    NewVar=""
    for i in range(len(Var1)): #Breaking down operation to not use any AND checks (defeats the point)
        if (int(Var1[i])==1): 
            if(int(Var2[i])==1):
                NewVar=NewVar+"1"
        else:
            NewVar=NewVar+"0"
    print("AND Result: ",NewVar)

def OR(Var1,Var2):
    NewVar=""
    for i in range(len(Var1)): #Breaking down operation to not use any OR checks (defeats the point)
        if (int(Var1)==1):
            NewVar=NewVar+"1"
        elif (int(Var2)==1):
            NewVar=NewVar+"1"
        else:
            NewVar=NewVar+"0"
    print("OR Result: ",NewVar)

Input()