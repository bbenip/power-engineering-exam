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

    # Print an initial greeting to the user
    print("Hello, let's study for the 4B exam!")
    
    # Create a list with each item corresponding to a line of a text file
    topicList = open("4B Q ORIGINAL.txt", encoding = "utf-8").read().splitlines()
    
    # Create sublists for separate topics based on the indicator '//'
    topicList = [list(x[1]) for x in itertools.groupby(topicList, lambda x: x=='//') if not x[0]]
    
    while (True):
        print("The following is a list of topics for the 4B Exam: \n")

        # Print a numbered list of all topics
        for i in range(len(topicList)):
            print(str(i + 1) + " " + topicList[i][0])

        # Prompt user for input
        print()
        checkUser = int(input("Select a number to see questions about the associated topic: ")) - 1
        print()

        # Print the title of the selected topic
        print(topicList[checkUser][0].upper())

        # Create a copy of the selected topic list, without the title
        questionList = topicList[checkUser][:]
        questionList.pop(0)

        # Create sublists for each question of the topic
        questionList = [list(x[1]) for x in itertools.groupby(questionList, lambda x: x=='--') if not x[0]]

        # Randomly shuffle all questions
        random.shuffle(questionList)
        print()
        
        for question in questionList:
            # Number used to display letter options to users
            conv = 97

            # Prints and removes question
            print()
            question.pop(0)
            print(question.pop(0))

            # Continues to print until options are encountered
            while "@@" not in question[0]:
                if question[0] == "":
                    question.pop(0)
                else:
                    print(question.pop(0))
            print()

            # Combine remaining elements consisting of options
            fullQuestion = "".join(question)

            # Create a list for the options, then randomly shuffle the list
            options = fullQuestion.split("@@-")
            random.shuffle(options)

            # Ensure "-  all of the above" is the last option if it exists
            if "-  all of the above" in options:
                options.append(options.pop(options.index("-  all of the above")))
            
            # Print the options for a question in a readable format
            for i in range(len(options)):
                if options[i] != "":
                    print(chr(i + conv) + ") " + options[i])
                else:
                    conv -= 1

        # Prompt user to return to main menu
        pause = input("\nPress enter to return to the main menu")

# MAIN
process_4B()
    
