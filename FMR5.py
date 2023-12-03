from functools import reduce

CheckEven = lambda No: (No % 2 == 0)
     
Increase = lambda No: No + 2
    
Add = lambda A,B:   A + B

def main():
    Data = []

    print("Enter the number of elements :")
    Size = int(input())

    print("Enter the elements : ")
    for i in range(Size):
         Value = int(input())
         Data.append(Value)

    output = list(filter(CheckEven,Data))
    print("Output after filter",output)

    moutput = list(map(Increase,output))
    print("Output after Map ",moutput)

    result = reduce(Add,moutput)
    print("Output after Reduce",result)
    
if __name__ == "__main__":
     main()