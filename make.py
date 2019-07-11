num = input("please enter the first number : ")
num1 = input("please enter the second number : ")

a= float (num)
b= float (num1)

calculate = input("in caps, enter ADD, MULTIPLY, SUBTRACT or DIVIDE =>")

if calculate == "ADD":
    operation= a +b
elif calculate == "MULTIPLY":
    operation= a *b
elif calculate == "SUBTRACT":
    operation= a -b
elif  calculate == "DIVIDE":
    operation= a /b
   
result = str (operation)
print ("your result for "+ num + " "+calculate+ " "+num1+" is "+result)