import os

def main():
    print("PID fo current process is : ",os.getpid())
    print("PID of parent process is : ",os.getppid())

if __name__ == "__main__":
    main()