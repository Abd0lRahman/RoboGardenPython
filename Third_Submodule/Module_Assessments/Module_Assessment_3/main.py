num = int(input("Please enter the number : "))

if(num==1 or num==0):  
    print("Please start from 2")
else: 
    for i in range(2,num+1):
        Prim =True
        for j in range(2,i):
            if(i%j==0):
                Prim = False
        if(Prim == True):
            print(i,end=" ")
