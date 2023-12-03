def Addition(No1, No2):
    Ans = 0
    Ans = No1 + No2
    return Ans
#7588945488

def Substraction(No1, No2):
    Ans = 0
    Ans = No1 - No2
    return Ans

def main():
    Value1 = int(input("Enter the first number : "))
    Value2 = int(input("Enter the second number : "))
  
    Ret = Addition(Value1,Value2)
    print("addition is  :",Ret)

    Ret = Substraction(Value1,Value2)
    print("addition is  :",Ret)
    
if __name__ == "__main__":
    main()