from MarvellousFMR import *


CheckEven = lambda No: (No % 2 == 0)
Increase = lambda No: No + 2 
Add = lambda A,B:   A + B

#Task : Name of function
#Elements : Lists of data elements
            
    
def main():
    Data = []

    print("Enter the number of elements :")
    Size = int(input())

    print("Enter the elements : ")
    for i in range(Size):
         Value = int(input())
         Data.append(Value)

    output = list(filterX(CheckEven,Data))
    print("Output after filter",output)

    moutput = list(mapX(Increase,output))
    print("Output after Map ",moutput)

    result = reduceX(Add,moutput)
    print("Output after Reduce",result)
    
if __name__ == "__main__":
     main()

CheckEven = lambda No: (No % 2 == 0)
Increase = lambda No: No + 2 
Add = lambda A,B:   A + B

#Task : Name of function
#Elements : Lists of data elements
            
    
def main():
    Data = []

    print("Enter the number of elements :")
    Size = int(input())

    print("Enter the elements : ")
    for i in range(Size):
         Value = int(input())
         Data.append(Value)

    output = list(filterX(CheckEven,Data))
    print("Output after filter",output)

    moutput = list(mapX(Increase,output))
    print("Output after Map ",moutput)

    result = reduceX(Add,moutput)
    print("Output after Reduce",result)
    
if __name__ == "__main__":
     main()