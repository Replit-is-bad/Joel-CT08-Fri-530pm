import random

def generate_password(length):
    password = ""
    
    for i in range(int(length)):
        random_num = random.randint(1,4)
        if random_num == 1:
            uppercase = chr(random.randint(65,90))
            password += uppercase
        elif random_num == 2:
            lowercase = chr(random.randint(97,122))
            password += lowercase
        elif random_num == 3:
            number = chr(random.randint(48,57))
            password += number
        elif random_num == 4:
            symbol = chr(random.randint(33,47))
            password += symbol
    return password
def create_new_user(user_db):
    username = input("ENTER USER")
    while True:
        password_length = input("PASSWORD LENGTH?")
        if password_length.isdigit():
            erejim = generate_password(password_length)
            print(erejim)
            break
        else:
            print("HA......HA.....HA......HA.......")
            print("NOSYMBOLNOSYMBOLNOSYMBOLNOSYMBOLNOSYMBOLNOSYMBOLNOSYMBOLNOSYMBOLNOSYMBOLNOSYMBOLNOSYMBOLNOSYMBOL")
    user_db[username] = erejim
    return user_db

def login(user_db):
    auth_status = False
    username = input("enter user:")
    password = input("enter password:")
    if username in user_db:
        password = input("enter password:")
        if user_db[username] == password:
            print("login :)")
            auth_status = True
    else:
        print("SACMMER")
    return auth_status


user_db = {}
user_db = create_new_user(user_db)
log_in = login(user_db)
print(log_in)