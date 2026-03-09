"""
============================================================
Q1. Quiz Auto-Marker
============================================================
You are building an auto-marker system for a multiple-choice quiz.
The program must compare a student's answers with the answer key.
It should calculate the score, identify which questions were wrong, and assign a grade.

- Write 3 functions:
    1) score_quiz(key, ans)
    2) wrong_questions(key, ans)
    3) grade(score, total)
- Do not change the function names or parameters.
- After writing your functions, uncomment the test code at the bottom to test.

============================================================
"""

# ============================================================
# Step 1: Write function score_quiz(key, ans)
# ============================================================
# - key and ans are lists of equal length
# - Compare answers at the same position
# - Return total number of correct answers
# ============================================================


def score_quiz(answer_key, student_ans):
    score = 0
    num = answer_key
    for answers in student_ans:
        
        if student_ans == answer_key:
            score += 1
    return score



answer_key = ["B","D","A","A","C","B","C","D","B","A"]
student_ans = ["B","D","C","A","C","B","C","A","B","A"]


# ============================================================
# Step 2: Write function wrong_questions(key, ans)
# ============================================================
# - Return a list of question numbers (starting from 1) that are wrong
# - If all answers are correct, return an empty list
# ============================================================



# ============================================================
# Step 3: Write function grade(score, total)
# ============================================================
# - Compute percentage = (score / total) * 100
# - Return:
#     "A" if percentage >= 80
#     "B" if percentage >= 70
#     "C" if percentage >= 60
#     "D" otherwise
# ============================================================



# ============================================================
# Step 4: Main Code Testing
# ============================================================
# Uncomment after writing your functions

# score = score_quiz(answer_key, student_ans)
# wrong = wrong_questions(answer_key, student_ans)
# final_grade = grade(score, len(answer_key))

# print("Score:", score)
# print("Wrong Questions:", wrong)
# print("Grade:", final_grade)



