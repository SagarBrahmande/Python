def main():
    print("Enter the number of that you want to store :")
    Length = int(input())

    Arr = list()

    print("Enter the elements :")
    for i in range(Length):
        value = int(input())
        Arr.append(value)


    print("Elements from list are : ")
    for i in range(Length):
        print(Arr[i])
        
if __name__ == "__main__":
    main()