#globalvariables
param1=1
param2=1
op="?"

#function definition
def intro():
    print("Welcome i am a robot built to assist you in MATH")
    return

def inputBoi():
    global param1
    global param2
    global op
    #input first peram
    param1=input("WHAT IS YOUR FIRST NUMBER")
    param2=input("WHAT IS YOUR SECOND NUMBER")
    op=input("WHAT DO YOU WANT ME TO DO +,-,*,/")
    return
    
def calculate():
    global op
    global param1
    global param2
    if (op == "*"):
        print(int(param1)*int(param2))
    elif (op == "/"):
        print(int(param1)/int(param2))
    elif (op == "+"):
        print(int(param1)+int(param2))
    elif (op == "-"):
        print(int(param1)-int(param2))
    return

def redo():
    print ("press f5 if you like to restart")
#executable code
intro()
inputBoi()
calculate()
redo()
