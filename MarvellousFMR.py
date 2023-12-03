def filterX(Task, Elements):
    Result = []
    for no in Elements:
         if (Task(no) == True):
              Result.append(no)
    return Result 

def mapX(Task1, Elements1):
     Result = []
     for no in Elements1:
          Ret = Task1(no)
          Result.append(Ret)
     return Result 

def reduceX(Task2, Elements2):
     Sum = 0
     for no in Elements2:
        Sum = Task2(Sum,no)
     return Sum 