
def take_attendance(attendance_dictionary):
    for name,attendance_list in attendance_dictionary.items():
        while True:
            attendance = input(f"Is {name} here? (y/n): ")
            if attendance.lower().strip() == 'y':
                attendance_list.append(True)
                break
            elif attendance.lower().strip() =='n':
                attendance_list.append(False)
                break
            else:
                print('invalid')
    return attendance

def cal_attendance_percent(attendance_dictionary, student_name):
    days_attended = 0
    if student_name in attendance_dictionary:
        for attendance in attendance_dictionary[student_name]:
            if attendance == True:
                days_attended += 1 
        return days_attended / len(attendance_dictionary[student_name]) * 100
    else:
        print(f'{student_name} not in class')

def notify_low_attendance(attendance_dictionary, threshold):
    low_attendance_student = []
    for attendance in attendance_dictionary:
        percent = cal_attendance_percent(attendance_dictionary, attendance)
        if percent <= threshold:
            print(f'WARNING {attendance} IS {percent}')
            low_attendance_student.append(attendance)
    return low_attendance_student

attendance_dictionary = {
    "Matthew" : [],
    "Jayden" : [],
    "Isaac" : [],
    "Ayden" : [],
    "Noah" : [],
    "Sam" : [],
    "Ryan" : [],
    "Elim" : [],
    "Angeline" : [],
    "Youmi" : [],
    "Artemis" : [],
    "Edgar" : [],
    "Soda" : [],
    "Isabelle" : []
}

while True:
    print('SCHOOL ATTENDANCE SYSTEM')
    print('1. Take Attendance')
    print('2. CAlculate Attendance percent')
    print('3. Notify Low attendance')
    print('4. Exit program')
    user_input = input('Select: ')
    if user_input == "1":
        take_attendance(attendance_dictionary)
    elif user_input == "2":
        student = input('Which student? ')
        cal_attendance_percent(attendance_dictionary,student)
    elif user_input == "3":
        threshold1 = float(input('What is the threshold for low attendance? eg 10 :'))
        notify_low_attendance(attendance_dictionary,threshold1)
    elif user_input == "4":
        print('im playing bloxed io')
        break
    else:
        print("❌ Invalid choice.")