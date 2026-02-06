def persentage_attendance(total_days, attended_days):
    if total_days == 0:
        return 0
    return (attended_days / total_days) * 100

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

def cal_attendance_persent(attendance_dictonary, student_name):
    if student_name in attendance_dictionary:
        attendance_dictionary[student_name]
    else:
        print(f'{student_name} not in class')


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

print(attendance_dictionary)
attendance_dictionary = take_attendance(attendance_dictionary)
print(attendance_dictionary)