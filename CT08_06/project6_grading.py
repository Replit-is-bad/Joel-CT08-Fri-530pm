
#functions
def grade_quiz(student_answers, answer_key):
    quiz_score = {}
    score = 0
    for name, answers, in student_answers.items():
        for i in range (len(answers)):
            score += 1
    quiz_score[name] = score
    return quiz_score

def calculate_average_scores(quiz_score):
    total_score = 0

    for name , score in quiz_score.items():
        total_score += score

    #calculate average
    average_score = total_score / len(student_answers)
    return average_score

def find_the_highest_scorer(quiz_score):
    highest_score = 0
    highest_scorers = []
    for name, score in quiz_score.items():

        if score > highest_score:
            highest_score = score

    for name, score in quiz_score.items():
        if score == highest_score:
            highest_scorers.append(name) 
    
    return highest_scorers

def display_results(quiz_score):
    print('---CLASS RESULTS ---')
    for name , score in quiz_score.items():
        print(f"{name}' s score is {score}")

def menu_system():
    print('--- QUIZ GRADING SYSTEM MENU ---')
    while True:
        print('1. Grade all students')
        print('2. Calculate class average')
        print('3. find highest scorer')
        print('4. Display results')
        print('5. Exit program')

        user_input = input('Select: ')
        if user_input == "1":
            grade_quiz(student_answers ,answer_key)
        elif user_input == "2":
            calculate_average_scores(quiz_scores)
        elif user_input == "3":
            find_the_highest_scorer(quiz_scores)
        elif user_input == "4":
            display_results(quiz_scores)
            break
        elif user_input == "5":
            print('---BYE---')
            break
        else:
            print("❌ Invalid choice.")


# Predefined data
answer_key = ["A", "B", "B", "D"]  # Correct answers for the quiz
student_answers = {
    "john": ["A", "C", "B", "D"],
    "jane": ["A", "B", "B", "D"],
    "alice": ["A", "C", "C", "D"],
    "bob": ["A", "B", "B", "D"]
}


