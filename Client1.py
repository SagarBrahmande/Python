
import Demo
def main():
    Value1= int(input("Enter first number : "))
    Value2= int(input("Enter second number : "))

    Result=0
    
    Result =Demo.Addition(Value1,Value2)
    print("Addition is :",Result)

    Result =Demo.Substraction(Value1,Value2)
    print("Substraction is :",Result)

    
    Result =Demo.Multiplication(Value1,Value2)
    print("Multiplication is :",Result)

if __name__=="__main__":
     main()

