print("Welcome to the million dollar quiz, 100k for each question.")

Questions = [
    "1. Which data type is immutable in Python?\nA. List\nB. Dictionary\nC. Set\nD. Tuple",
    "2. What does CPU stand for?\nA. Central Process Unit\nB. Central Processing Unit\nC. Computer Personal Unit\nD. Control Processing Unit",
    "3. Which keyword is used to define a function in Python?\nA. func\nB. define\nC. def\nD. function",
    "4. What is the output of 2 ** 3 in Python?\nA. 6\nB. 8\nC. 9\nD. 5",
    "5. Which of the following is a loop structure in Python?\nA. repeat\nB. iterate\nC. for\nD. loop",
    "6. Which symbol is used for comments in Python?\nA. //\nB. \nC. #\nD. **",
    "7. Which data structure uses key–value pairs?\nA. List\nB. Tuple\nC. Dictionary\nD. String",
    "8. What is the capital of Japan?\nA. Beijing\nB. Seoul\nC. Tokyo\nD. Bangkok",
    "9. Which operator is used for equality comparison in Python?\nA. =\nB. ==\nC. !=\nD. <=",
    "10. Which of these is NOT a programming language?\nA. Python\nB. Java\nC. HTML\nD. C++"
]
Answers = ["D", "B", "C", "B", "C", "C", "C", "C", "B", "C"]

for i in range(len(Questions)):
    print("\n" + Questions[i])
    
    a = input("Choose an option: ").upper()
    
    if a == Answers[i]:
        # Using .format() instead of f-string
        prize = (i + 1) * 100
        print("Correct answer! You win {}k so far.".format(prize))
        
        if i + 1 < len(Questions):
            print("Now let's move to the next question...")
        else:
            print("Congratulations! You won the Million Dollars!")
    else:
        print("Oops! You lost.")
        break