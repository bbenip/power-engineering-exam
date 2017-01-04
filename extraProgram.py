import itertools
import random

# MENU FUNCTION
def process_4B():
    '''
    () -> None
    Creates an interactive environment which allows users to
    search a large database comprised of 4B Questions
    using a menu-driven interface
    '''
    
    print("Hello, Bhagwant! Let's study for the 4B. The following is a list of topics for the 4B Exam: \n")
    
    questionList = open("4B Q ORIGINAL.txt", encoding = "utf-8").read().splitlines()
    questionList = [list(x[1]) for x in itertools.groupby(questionList, lambda x: x=='//') if not x[0]]
    for i in range(len(questionList)):
        print(str(i + 1) + " " + questionList[i][0])
    print()
    checkUser = int(input("Select a number to see questions about the associated topic: ")) - 1
    print()

    print(questionList[checkUser][0])

    topicList = questionList[checkUser][:]
    
    topicList.pop(checkUser)
    
    topicList = [list(x[1]) for x in itertools.groupby(topicList, lambda x: x=='--') if not x[0]]
    random.shuffle(topicList)

    for item in topicList:
        for el in item:
            print(el)

# MAIN
process_4B()
    
