#numbers between 7 and 19
loop = 6
while (loop<19):
    loop= loop+1
    print (loop)




#even numbers
start=input("please enter the starting point => ")
i=int(start)

end=input("please enter the end range => ")
n = int (end)

while (i<n):
    i=i+1
    if (i<n and i%2==0):
        print (i)
        
        




#reverse even numbers
start=input("please enter the starting point => ")
i=int(start)

end=input("please enter the end of range => ")
n = int (end)

while (n>i):
    n=n-1
    if (n>i and n%2==0):
        print (n)
