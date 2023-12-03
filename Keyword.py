
def Display(Name, Age, Marks):
    print ("Name is :",Name)
    print("Age is :",Age)
    print("Marks are :",Marks)


def main():
    print("Demonstration of Positional Arguments ")

    Display(Name = "Amit",Age = 25,Marks = 89)

    Display(Age = 21, Name = "Sagar",Marks = 78)

if __name__ == "__main__":
    main()
