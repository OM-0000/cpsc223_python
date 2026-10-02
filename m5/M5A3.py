# Name: Ossama Mostafa
# Student ID: 871567681
# Section: 18254
# Assignment: Module 5 Assignment 3

triviabank_dict = {}
question_str = ""
answer_str = ""

print("Welcome to the trivia builder 3000")
while True:
    question_str = input("Enter the next question: ")
    #Stripping whitespace to ensure that we don't get fooled by spaces or tabs
    question_str = question_str.rstrip()
    question_str = question_str.lstrip()
    if len(question_str) == 0:
        print("You did not enter a question, let's try again.")
    elif question_str == "Done":
        print("We will stop entering questions now")
        break
    else:
        answer_str = input("Enter the correct answer for that question: ")
        triviabank_dict[question_str] = answer_str

print("Here is the final trivia dictionary:")
for question, answer in triviabank_dict.items():
    print(f"The question is: {question}")
    print(f"And the answer is: {answer}")
